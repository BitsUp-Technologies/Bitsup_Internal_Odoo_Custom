# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Indian - UPI in Sales',
    'version': '1.0',
    'description': """
Sales with UPI QR code
=========================
This module adds QR code in sales quote/order report for UPI payment allowing to make payment via any UPI app.

To print UPI Qr code add UPI id in company and tick "QR Codes" in configuration
  """,
    'category': 'Accounting/Localizations',
    'depends': ['l10n_in','l10n_in_upi'],
    #'data': ['views/res_company_views.xml'],
    'license': 'LGPL-3',
    'auto_install': True,
}
