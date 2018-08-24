# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.constrains('phone', 'mobile', 'fax')
    def _check_number_format(self):
        try:
            phone = int(self.phone)
        except ValueError:
            raise ValueError(_('Attention !! Phone number %s , should contains only numbers ' % (self.phone)))
        try:
            mobile = int(self.mobile)
        except ValueError:
            raise ValueError(_('Attention !! Mobile number %s , should contains only numbers ' % (self.mobile)))
        try:
            fax = int(self.fax)
        except ValueError:
            raise ValueError(_('Attention !! Fax number %s , should contains only numbers ' % (self.fax)))