# -*- coding: utf-8 -*-

from openerp import models, fields, api


class ResPartnerRegisterEvent(models.TransientModel):
    _name = 'res.partner.register.event'

    event_id = fields.Many2one('simple.event.event', required=True)

    @api.multi
    def button_register(self):
        registration_obj = self.env['simple.event.registration']
        partner_obj = self.env['res.partner']
        for partner_id in self.env.context.get('active_ids', []):
            partner = partner_obj.browse(partner_id)
            registration_obj.create({'event_id': self.event_id.id, 'partner_id': partner.id})
