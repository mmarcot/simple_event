# -*- coding: utf-8 -*-

{
    'name': "Simple Event",
    'version': '1.0',
    'depends': ['base'],
    'author': "mmarcot@gmail.com",
    'description': """
    Simple event management
    """,
    # data files always loaded at installation
    'data': [
        'security/simple_event_security.xml',
        'security/ir.model.access.csv',
        'views/registration.xml',
        'views/event.xml',
        'views/event_type.xml',
        'views/res_partner.xml',
        'wizards/res_partner_register_event_view.xml',
        'simple_event_data.xml',
        'simple_event_menuitem.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [],
}
