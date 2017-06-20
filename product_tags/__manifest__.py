# -*- coding: utf-8 -*-
# © 2013 Julius Network Solutions SARL <contact@julius.fr>
# © 2015 credativ ltd. <info@credativ.co.uk>
# © 2017 Savoir-faire Linux
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Product Tags",
    "version": "10.0.1.0.0",
    "author": "Julius Network Solutions, Savoir-faire Linux",
    "website": "http://julius.fr",
    "category": "Sales Management",
    "summary": "Product Tags",
    "depends": [
        'product',
        'sale',
    ],
    "demo": [],
    "data": [
        'security/ir.model.access.csv',
        'views/product_tag_view.xml',
        'views/product_template_view.xml',
    ],
    'installable': True,
}
