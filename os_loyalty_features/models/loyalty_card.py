from odoo import _, api, exceptions, fields, models
from datetime import datetime, timedelta


class LoyaltyCard(models.Model):
    _inherit = 'loyalty.card'

    @api.model
    def default_get(self, fields):
        defaults = super(LoyaltyCard, self).default_get(fields)
        defaults.update(
            points=999,
            expiration_date=datetime.now() + timedelta(days=365),
        )

        return defaults

    def write(self, vals):
        if 'points' in vals:
            if vals['points'] == 1:
                vals['points'] = 999
        res = super(LoyaltyCard, self).write(vals)
        return res
