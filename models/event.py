# -*- coding: utf-8 -*-

from openerp import models, fields, api, _


class Event(models.Model):
    _name = 'simple.event.event'
    _description = _('An event')


    @api.depends('registration_ids')
    def _compute_nb_place(self):
        '''
        Calcule le nombre de place invité, confirmé et présent
        '''
        for record in self:
            inv, conf, pres, total = 0, 0, 0, 0
            for registration in record.registration_ids:
                total += 1
                if registration.state == 'invite':
                    inv += 1
                elif registration.state == 'confirm':
                    conf += 1
                elif registration.state == 'present':
                    pres += 1
            record.nb_invite = inv
            record.nb_confirm = conf
            record.nb_present = pres
            record.nb_total = total


    @api.onchange('date_start')
    def _on_change_date_start(self):
        for record in self:
            record.date_stop = record.date_start


    @api.multi
    def button_done(self):
        for record in self:
            record.state = 'done'

    @api.multi
    def button_confirm(self):
        for record in self:
            record.state = 'confirm'


    name = fields.Char(string=_('Event'), required=True)
    description = fields.Text(string=_('Description'))
    type_id = fields.Many2one('simple.event.event.type', string=_('Event type'), ondelete='set null')
    date_start = fields.Datetime(string=_('Begin date'))
    date_stop = fields.Datetime(string=_('End date'))
    registration_ids = fields.One2many('simple.event.registration', 'event_id')
    nb_invite = fields.Integer(compute=_compute_nb_place, string=_('Invited'))
    nb_confirm = fields.Integer(compute=_compute_nb_place, string=_('Confirmed'))
    nb_present = fields.Integer(compute=_compute_nb_place, string=_('Attended'))
    nb_total = fields.Integer(compute=_compute_nb_place, string=_('Total'), store=True)
    state = fields.Selection(selection=[
        ('confirm', _('Confirmed')),
        ('done', _('Done')),
    ], string=_('State'), default='confirm', readonly=True, copy=False)
