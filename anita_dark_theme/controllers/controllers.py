# -*- coding: utf-8 -*-
# from odoo import http


# class AnitaDarkTheme(http.Controller):
#     @http.route('/anita_dark_theme/anita_dark_theme', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/anita_dark_theme/anita_dark_theme/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('anita_dark_theme.listing', {
#             'root': '/anita_dark_theme/anita_dark_theme',
#             'objects': http.request.env['anita_dark_theme.anita_dark_theme'].search([]),
#         })

#     @http.route('/anita_dark_theme/anita_dark_theme/objects/<model("anita_dark_theme.anita_dark_theme"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('anita_dark_theme.object', {
#             'object': obj
#         })
