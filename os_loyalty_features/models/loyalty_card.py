from odoo import _, api, exceptions, fields, models
from datetime import datetime, timedelta


class LoyaltyCard(models.Model):
    _inherit = 'loyalty.card'

    season_ticket = fields.Boolean(
        related='program_id.season_ticket',
    )

    @api.model
    def default_get(self, fields):
        defaults = super(LoyaltyCard, self).default_get(fields)

        active_model = self.env.context.get('active_model')
        if active_model == 'loyalty.program' and len(self.env.context.get('active_ids', [])) <= 1:
            program = self.env[active_model].browse(self.env.context.get('active_id')).exists()
            if program and program.season_ticket:
                defaults.update(
                    points=999,
                    expiration_date=datetime.now() + timedelta(days=365),
                )

        return defaults

    @api.model_create_multi
    def create(self, vals):
        res = super(LoyaltyCard, self).create(vals)
        for rec in res:
            if rec.season_ticket:
                rec.points = 999
            if rec.season_ticket and not rec.expiration_date:
                rec.expiration_date=datetime.now() + timedelta(days=365)
        return res

    def write(self, vals):
        for rec in self:
            if rec.season_ticket:
                vals.update(
                    points=999,
                )
                if (not rec.expiration_date
                        or ('expiration_date' in vals and not vals.get('expiration_date'))):
                    vals.update(
                        expiration_date=rec.create_date + timedelta(days=365),
                    )
        res = super(LoyaltyCard, self).write(vals)
        return res
