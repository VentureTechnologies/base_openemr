# -*- coding: utf-8 -*-
# Part of Venture Technologies. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class psc_code(models.Model):
    _name  = 'psc.code'
    _description = 'psc code'
    
    name = fields.Char('Code', required =True) 
    description = fields.Text('Long Text', required =True)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:    