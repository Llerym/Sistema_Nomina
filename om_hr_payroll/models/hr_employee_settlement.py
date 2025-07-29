from odoo import models, fields, api

class EmployeeSettlement(models.Model):
    _name = 'hr.employee.settlement'
    _description = 'Employee Settlement'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    exit_date = fields.Date(string='Exit Date', required=True)
    reason = fields.Selection([
        ('resignation', 'Resignation'),
        ('dismissal', 'Dismissal'),
        ('termination', 'Termination by Agreement'),
    ], string='Reason', required=True)
    notes = fields.Text(string='Notes')

    # Campos relacionados con la liquidación
    pending_vacation_days = fields.Float(string='Pending Vacation Days')
    severance_pay = fields.Monetary(string='Severance Pay')
    final_payment = fields.Monetary(string='Final Payment')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('paid', 'Paid'),
    ], string='Status', default='draft')

