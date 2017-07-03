# -*- coding: utf-8 -*-
# © 2013 Julius Network Solutions SARL <contact@julius.fr>
# © 2015 credativ ltd. <info@credativ.co.uk>
# © 2017 Savoir-faire Linux
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl-3.0).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    tag_ids = fields.Many2many(
        string='Tags',
        comodel_name='product.tag',
        relation='product_product_tag_rel',
        column1='product_id',
        column2='tag_id',
    )
