# -*- coding: utf-8 -*-
{
    'name': "anita_theme_base",

    'summary': """
        Base for themes, it support free login for odoo
    """,

    'description': """
        Odoo Login, 
        Odoo login page, 
        Odoo login theme
        Login, 
        Anita Theme Base,
        Anita Theme,
        Awesome Theme,
        Multi tab theme,
        Pop form theme
    """,

    'author': "openErpNext",

    'website': "https://base.openerpnext.com",
    'live_test_url': 'https://base.openerpnext.com',

    'license': 'OPL-1',
    'images': ['static/description/screen_shot.png', 'static/description/banner.png'],
    'support': 'codercrax@gmail.com',
    'maintainer': 'openErpNext',
    'category': 'Theme/Backend',
    'version': '16.0.0.2',

    'installable': True,
    'application': True,
    'auto_install': False,

    'depends': ['base', 'web', 'anita_login'],
    
    'data': [],

    'assets': {
        'web.assets_backend': [
            'anita_theme_base/static/css/anita_variables.scss',

            'anita_theme_base/static/css/mixins/_flex.scss',
            'anita_theme_base/static/css/mixins/_box_shadow.scss',
            'anita_theme_base/static/css/mixins/_clearfix.scss',
            'anita_theme_base/static/css/mixins/_float.scss',
            'anita_theme_base/static/css/mixins/_hover.scss',
            'anita_theme_base/static/css/mixins/_gradients.scss',
            'anita_theme_base/static/css/mixins/_buttons.scss',
            
            'anita_theme_base/static/css/anita_functions.scss',

            'anita_theme_base/static/css/anita_form_controls.scss',
            'anita_theme_base/static/css/anita_buttons.scss',

            'anita_theme_base/static/css/anita_form_view.scss',
            'anita_theme_base/static/css/anita_list_view.scss',
            'anita_theme_base/static/css/anita_scroll.scss',
            'anita_theme_base/static/css/anita_misc.scss',

            'anita_theme_base/static/src/**/*',
        ]
    }
}
