from odoo import api, fields, models

class HrCinepolisEmployee(models.Model):
    _inherit = 'hr.employee'
    _description = 'Employee Cinepolis'

    has_capacity = fields.Boolean("Capacidad Limitada")
