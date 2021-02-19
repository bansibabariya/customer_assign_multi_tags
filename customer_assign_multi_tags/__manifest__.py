# Copyright 2020 Odoo Helper
# See LICENSE file for full copyright and licensing details.
#
##############################################################################
{
    'name': 'Customer Assign Multi Tags',
    'category': 'Customer',
    'version': '14.0.1',

    'summary': 'We select multiple customer in tree view and then we will go to action and click "ASSIGN TAGS" and '
               'then open wizard and select one or multiple tags and apply so, reflect tags on which select customer.',

    'description': """
We select multiple customer in tree view and then we will go to action and click "ASSIGN TAGS" and then open wizard and 
select one or multiple tags and apply so, reflect tags on which select customer.
        """,

    'author': 'Odoo Helper',
    'license': 'AGPL-3',

    'depends': ['base', 'web', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/assign_tag_wizard.xml',

    ],

    'images': ['images/OdooHelper.jpg'],

    'price': 11.17,
    'currency': 'USD',

    'installable': True,
    'application': False
}
