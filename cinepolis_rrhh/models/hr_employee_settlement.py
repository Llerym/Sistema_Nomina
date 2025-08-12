from odoo import models, fields, api

class EmployeeSettlement(models.Model):
    _name = 'hr.employee.settlement'
    _description = 'Liquidación de Empleado'

    employee_id = fields.Many2one('hr.employee', string='Empleado', required=True)
    exit_date = fields.Date(string='Fecha de Salida', required=True)
    reason = fields.Selection([
        ('resignation', 'Renuncia'),
        ('dismissal', 'Despido'),
        ('termination', 'Terminación por Mutuo Acuerdo'),
    ], string='Motivo', required=True)
    notes = fields.Text(string='Notas')

    # Campos relacionados con la liquidación
    pending_vacation_days = fields.Float(string='Días de Vacaciones Pendientes')
    severance_pay = fields.Monetary(string='Pago por Cesantía')
    currency_id = fields.Many2one('res.currency', string='Moneda', default=lambda self: self.env.company.currency_id)

    # Campos adicionales
    last_working_day = fields.Date(string='Último Día Laborado')
    notice_given = fields.Boolean(string='Aviso Previo Otorgado')
    notice_period_days = fields.Integer(string='Días de Aviso Previo')
    rehire_eligible = fields.Boolean(string='Elegible para Recontratación')
    exit_interview_done = fields.Boolean(string='Entrevista de Salida Realizada')
    exit_document_signed = fields.Boolean(string='Documento de Salida Firmado')
    settlement_date = fields.Date(string='Fecha de Liquidación')
    unpaid_salary = fields.Monetary(string='Salario Pendiente')
    bonuses = fields.Monetary(string='Bonificaciones')
    deductions = fields.Monetary(string='Deducciones')
    other_compensations = fields.Monetary(string='Otras Compensaciones')
    total_settlement = fields.Monetary(string='Total de Liquidación', compute='_compute_total_settlement')

    state = fields.Selection([
        ('draft', 'Borrador'),
        ('confirmed', 'Pago pendiente'),
        ('paid', 'Pagado'),
    ], string='Estado', default='draft')

    @api.depends('severance_pay', 'unpaid_salary', 'bonuses', 'deductions', 'other_compensations')
    def _compute_total_settlement(self):
        for record in self:
            record.total_settlement = (
                (record.severance_pay or 0.0)
                + (record.unpaid_salary or 0.0)
                + (record.bonuses or 0.0)
                + (record.other_compensations or 0.0)
                - (record.deductions or 0.0)
            )
