from odoo import _, api, exceptions, fields, models
from datetime import datetime, timedelta


class LoyaltyCard(models.Model):
    _inherit = 'loyalty.card'

    activation_date = fields.Date()

    season_ticket = fields.Boolean(
        related='program_id.season_ticket',
    )

    validity_period = fields.Integer(
        related='program_id.validity_period',
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
                    expiration_date=datetime.now() + timedelta(days=program.validity_period),
                )

        return defaults

    @api.model_create_multi
    def create(self, vals):
        res = super(LoyaltyCard, self).create(vals)
        for rec in res:
            if rec.season_ticket:
                #if rec.points < 100:
                #    rec.points = 999
                if not rec.expiration_date:
                    rec.expiration_date = datetime.now() + timedelta(days=rec.validity_period)
                if not rec.partner_id and rec.source_pos_order_id:
                    rec.partner_id = rec.source_pos_order_id.partner_id
                if not rec.partner_id and rec.order_id:
                    rec.partner_id = rec.order_id.partner_id
        return res

    def write(self, vals):
        for rec in self:
            if rec.season_ticket:
                if (rec.points < 100
                        or ('points' in vals and (vals.get('points') > 999 or vals.get('points') < 100))):
                    vals.update(
                        points=999,
                    )
                if (not rec.expiration_date
                        or ('expiration_date' in vals and not vals.get('expiration_date'))):
                    vals.update(
                        expiration_date=rec.create_date + timedelta(days=rec.validity_period),
                    )
                if ((rec.points == 998 or ('points' in vals and vals.get('points') == 998))
                        and (not rec.activation_date or ('activation_date' in vals and not vals.get('activation_date')))):
                    vals.update(
                        activation_date=datetime.today(),
                        expiration_date=datetime.today() + timedelta(days=rec.validity_period),
                    )
                if not rec.partner_id and rec.source_pos_order_id:
                    vals.update(
                        partner_id=rec.source_pos_order_id.partner_id,
                    )
                if not rec.partner_id and rec.order_id:
                    vals.update(
                        partner_id=rec.order_id.partner_id,
                    )

        res = super(LoyaltyCard, self).write(vals)
        return res
