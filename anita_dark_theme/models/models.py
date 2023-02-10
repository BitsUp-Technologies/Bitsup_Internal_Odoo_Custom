# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class anita_dark_theme(models.Model):
#     _name = 'anita_dark_theme.anita_dark_theme'
#     _description = 'anita_dark_theme.anita_dark_theme'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
