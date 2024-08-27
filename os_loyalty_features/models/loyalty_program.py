from odoo import _, api, exceptions, fields, models


class LoyaltyProgram(models.Model):
    _inherit = 'loyalty.program'

    season_ticket = fields.Boolean(
        default=False,
    )

    validity_period = fields.Integer(
        default=0,
    )
