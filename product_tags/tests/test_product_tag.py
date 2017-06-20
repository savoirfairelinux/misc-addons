# -*- coding: utf-8 -*-
# © 2013 Julius Network Solutions SARL <contact@julius.fr>
# © 2015 credativ ltd. <info@credativ.co.uk>
# © 2017 Savoir-faire Linux
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.tests import common


class TestProductTag(common.SavepointCase):

    @classmethod
    def setUpClass(cls):
        super(TestProductTag, cls).setUpClass()

        cls.product_tag_grandparent = cls.env['product.tag'].create({
            'name': 'Vehicle',
        })

        cls.product_tag_parent = cls.env['product.tag'].create({
            'name': 'Car',
            'parent_id': cls.product_tag_grandparent.id,
        })

        cls.product_tag_child = cls.env['product.tag'].create({
            'name': 'Electric',
            'parent_id': cls.product_tag_parent.id,
        })

    def test_name_get(self):
        self.assertEqual(
            self.product_tag_child.display_name,
            'Vehicle / Car / Electric',
        )

    def test_name_search(self):
        tags = self.env['product.tag'].name_search(name='Car')
        self.assertEqual(tags[0][0], self.product_tag_parent.id)
        self.assertEqual(tags[0][1], 'Vehicle / Car')
