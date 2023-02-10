# -*- coding: utf-8 -*-
{
    'name': "anita_dark_theme",

    'summary': """
        Dark mode theme for odoo""",

    'description': """
        Dark mode theme for odoo, free, free, free!
    """,

    'author': "Fuenec Odoo Team",
    'website': "https://www.funenc.com/?fw=1",

    'category': 'Theme/Backend',
    'version': '16.0.0.1',
    'license': 'OPL-1',

    'depends': ['base', 'anita_theme_base', 'anita_login'],

    'images': [
        'static/description/anita_description.png',
        'static/description/anita_screenshot.png'],

    'data': [],

        'assets': {
        'web.assets_backend': [
            'anita_dark_theme/static/css/style.scss',
        ],
        
        'web.assets_qweb': []
    }
}
