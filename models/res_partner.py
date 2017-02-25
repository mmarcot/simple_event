# -*- coding: utf-8 -*-

from openerp import models, fields, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.depends('registration_ids')
    def _compute_registration_count(self):
        for record in self:
            record.registration_count = self.env['simple.event.registration'].search([
                ('partner_id', '=', record.id),
            ], count=True)

    registration_ids = fields.One2many('simple.event.registration', 'partner_id')
    registration_count = fields.Integer(compute=_compute_registration_count)
