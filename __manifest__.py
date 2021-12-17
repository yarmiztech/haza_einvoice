# -*- coding: utf-8 -*-
{
    'name': "Haza E-Invoice Report",
    'author':
        'ENZAPPS',
    'summary': """
This module is for printing E-Invoice report for Masar Arabia.
""",

    'description': """
        This module is for printing E-Invoice report for Masar Arabia.
    """,
    'website': "",
    'category': 'base',
    'version': '12.0',
    'depends': ['base','account','uom_unece','base_unece','account_tax_unece','base_vat_sanitized','onchange_helper','base_iban','base_bank_from_iban','base_business_document_import','account_invoice_import','base_ubl_payment','account_payment_partner','account_invoice_import_ubl','account_invoice_ubl','sale','purchase','stock',],
    'data': [
            'views/account_invoice.xml',
            # 'views/delivery.xml',
            'reports/reports.xml',
            # 'reports/report_view.xml',
            # 'reports/report_1.xml',
            # 'reports/report_1_view.xml',
            'reports/report_view_1.xml',
            # 'reports/delivery_note.xml',
            # 'reports/debit_note.xml',
            # 'reports/credite_note.xml',



    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
}
