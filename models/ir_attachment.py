# -*- coding: utf-8 -*-
################################################################################
#
#    Venture Technologies, LLC
#
#    Copyright (C) 2024-TODAY Venture Technologies(<https://www.venturetech.site>).
#    Author: Subina P (odoo@venturetech.site)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
from odoo import api, models


class IrAttachment(models.Model):
    """Inherited for making the attachments public"""
    _inherit = 'ir.attachment'

    @api.model
    def create(self, vals):
        """Inherited to make the attachments public"""
        vals['public'] = True
        return super().create(vals)
