# -*- coding:utf-8 -*-


from openerp import models, fields, api, _


class EventType(models.Model):
    _name = 'simple.event.event.type'
    _description = _('Event type')

    name = fields.Char()

