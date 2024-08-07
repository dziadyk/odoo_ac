from odoo import _, api, exceptions, fields, models
from datetime import datetime, timedelta


class LoyaltyCard(models.Model):
    _inherit = 'loyalty.card'

#    points = fields.Float(
#        default=100,
#        tracking=True,
#    )
#    expiration_date = fields.Date(
#        default=datetime.now() + timedelta(days=365),
#    )

    @api.model
    def default_get(self, fields):
        defaults = super(LoyaltyCard, self).default_get(fields)
        defaults.update(
            points=100,
            expiration_date=datetime.now() + timedelta(days=365),
        )

        return defaults
