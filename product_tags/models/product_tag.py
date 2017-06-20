# -*- coding: utf-8 -*-
# © 2013 Julius Network Solutions SARL <contact@julius.fr>
# © 2015 credativ ltd. <info@credativ.co.uk>
# © 2017 Savoir-faire Linux
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class ProductTag(models.Model):

    _description = 'Product Tags'
    _name = "product.tag"

    name = fields.Char(
        'Tag Name',
        required=True,
        translate=True,
    )

    active = fields.Boolean(
        help='The active field allows you to hide the tag without '
             'removing it.',
        default=True,
    )

    parent_id = fields.Many2one(
        string='Parent Tag',
        comodel_name='product.tag',
        index=True,
        ondelete='cascade',
    )

    child_ids = fields.One2many(
        string='Child Tags',
        comodel_name='product.tag',
        inverse_name='parent_id',
    )

    parent_left = fields.Integer(
        'Left Parent',
        index=True,
    )

    parent_right = fields.Integer(
        'Right Parent',
        index=True,
    )

    image = fields.Binary(
        'Image',
    )

    _parent_store = True
    _parent_order = 'name'
    _order = 'parent_left'

    @api.multi
    def name_get(self):
        """ Return the tags' display name, including their direct parent. """
        res = {}
        for record in self:
            current = record
            name = current.name
            while current.parent_id:
                name = '%s / %s' % (current.parent_id.name, name)
                current = current.parent_id
            res[record.id] = name

        return res.items()

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        if name:
            # Be sure name_search is symetric to name_get
            name = name.split(' / ')[-1]
            args = [('name', operator, name)] + args
        tags = self.search(args, limit=limit)
        return tags.name_get()
