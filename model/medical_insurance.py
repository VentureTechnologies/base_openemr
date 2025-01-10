# -*- coding: utf-8 -*-
# Part of Venture Technologies. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_insurance(models.Model):
    _name = 'medical.insurance'
    _description = 'medical insurance'
    _rec_name = 'policy_number'

    number = fields.Char(string='Internal ID', readonly=True)
    policy_number = fields.Char(string='Policy number')
    certificate_number = fields.Char(string='Certificate number')
    medical_insurance_partner_id = fields.Many2one('res.partner','Owner',domain="[('is_insurance_company','=',False)]",required=True)
    type =  fields.Selection([('state','State'),('private','Private')],default="private",string='Insurance Type')
    member_since= fields.Date('Member Since')
    insurance_compnay_id = fields.Many2one('res.partner',domain="[('is_insurance_company','=',True)]",string='Insurance Company')
    notes= fields.Text('Extra Info')
    member_exp = fields.Date('Expiration Date')
    medical_insurance_plan_id = fields.Many2one('medical.insurance.plan','Plan')


    @api.model
    def create(self, vals_list):
        vals_list['number'] = self.env['ir.sequence'].next_by_code('medical.insurance_id')
        return super(medical_insurance, self).create(vals_list)


