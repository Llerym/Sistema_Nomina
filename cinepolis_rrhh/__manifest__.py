# -*- coding: utf-8 -*-
{
    'name': "cinepolis_rrhh",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web', 'hr',
    'om_hr_payroll'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/hr_employee_settlement_views.xml',
    ],

'assets': {
    'web.assets_backend': [
        # aquí la ruta exacta a tu CSS
        'cinepolis_rrhh/static/src/css/employee_form.css',
    ],
},

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

