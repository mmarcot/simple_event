# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
from openerp.exceptions import ValidationError


class Registration(models.Model):
    _name = 'simple.event.registration'
    _description = _('Event\'s registration')

    _sql_constraints = [
        ('partner_reg_uniq', 'unique(event_id, partner_id)', 'Only one registration per partner to the same event')
    ]

    @api.onchange('event_id')
    def _on_change_event(self):
        for record in self:
            record.date_start_event = record.event_id.date_start
            record.date_stop_event = record.event_id.date_stop


    @api.onchange('partner_id')
    def _on_change_partner(self):
        for record in self:
            record.name = record.partner_id.name
            record.phone = record.partner_id.phone
            record.email = record.partner_id.email


    @api.constrains('event_id')
    def _check_event_id(self):
        for record in self:
            if record.event_id and record.event_id.state == 'done':
                raise ValidationError(_('The selected event is done, you cannot add a registration to it'))


    @api.multi
    def button_confirm(self):
        for record in self:
            record.state = 'confirm'


    @api.multi
    def button_present(self):
        for record in self:
            record.state = 'present'


    @api.multi
    def button_invite(self):
        for record in self:
            record.state = 'invite'


    name = fields.Char(related='partner_id.name')
    event_id = fields.Many2one('simple.event.event', string=_('Event'), required=True, ondelete='cascade')
    partner_id = fields.Many2one('res.partner', string=_('Partner'), required=True, ondelete='cascade')
    date_start_event = fields.Datetime(related='event_id.date_start', string=_('Event begin date'), readonly=True)
    date_stop_event = fields.Datetime(related='event_id.date_stop', string=_('Event end date'), readonly=True)
    state = fields.Selection(selection=[
        ('invite', _('Invited')),
        ('confirm', _('Confirmed')),
        ('present', _('Attended')),
    ], string=_('State'), default='invite', copy=False, readonly=True)
    phone = fields.Char(related='partner_id.phone', string=_('Phone'))
    email = fields.Char(related='partner_id.email', string=_('Email'))