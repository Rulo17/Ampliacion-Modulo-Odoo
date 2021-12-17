# -*- coding: utf-8 -*-
{
    'name': "FootballModule",
    'summary': """All clubs from La Liga""",
    'description': """Football module to manage teams:""",
    'author': "Raul Rodriguez",
    'website': "https://www.marca.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Rubricas',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/teams.xml',
        'views/manager.xml',
        'views/player.xml',
        'views/match.xml'
        ],
}