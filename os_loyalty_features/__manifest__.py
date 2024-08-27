# -*- coding: utf-8 -*-
{
    'name': 'Loyalty (OSC Features)',
    'summary': 'Loyalty (OSC Features)',
    'description': 'Loyalty (OSC Features)',

    'author': 'Volodymyr Dziadyk',
    'website': 'https://oneservice-consulting.com/',
    'support': 'dvol@oneservice-consulting.com',

    'category': 'Sales',
    'license': 'LGPL-3',
    'version': '17.0.1.0',

    'depends': [
        'loyalty',
    ],

    'data': [
        'views/res_partner_views.xml',
        'views/loyalty_program_views.xml',
        'views/loyalty_card_views.xml',
    ],

    'demo': [
    ],

    'application': False,
    'installable': True,
    'auto_install': False,

}
