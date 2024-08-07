from odoo import _, api, exceptions, fields, models


class Project(models.Model):
    _inherit = 'project.project'

    os_department_id = fields.Many2one(related='user_id.employee_id.department_id', string='Department', store=True, readonly=True)
