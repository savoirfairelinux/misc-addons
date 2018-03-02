# -*- coding: utf-8 -*-
# © 2018 Savoir-faire Linux
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from openupgradelib import openupgrade


def migrate(cr, version):
    """
    Inverse columns (product, product_tag) of the relation
    product_product_tag_rel.
    """
    openupgrade.logged_query(cr, """
        ALTER TABLE product_product_tag_rel
        RENAME COLUMN product_id to product_tmpl_id
    """)

    openupgrade.logged_query(cr, """
        ALTER TABLE product_product_tag_rel
        RENAME COLUMN tag_id to product_id;
    """)

    openupgrade.logged_query(cr, """
        ALTER TABLE product_product_tag_rel
        RENAME COLUMN product_tmpl_id to tag_id;
    """)
