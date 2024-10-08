# -*- coding: utf-8 -*-
# Part of Venture Technologies. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_prescription_order(models.Model):
    _name = "medical.prescription.order"
    _description = 'medical Prescription order'

    name = fields.Char('Prescription ID')
    patient_id = fields.Many2one('medical.patient','Patient Name')
    prescription_date = fields.Datetime('Prescription Date', default=fields.Datetime.now)
    user_id = fields.Many2one('res.users','Login User',readonly=True, default=lambda self: self.env.user)
    no_invoice = fields.Boolean('Invoice exempt')
    inv_id = fields.Many2one('account.move', 'Invoice')
    invoice_to_insurer = fields.Boolean('Invoice to Insurance')
    doctor_id = fields.Many2one('medical.physician','Prescribing Doctor')
    medical_appointment_id = fields.Many2one('medical.appointment','Appointment')
    state = fields.Selection([('invoiced','To Invoiced'),('tobe','To Be Invoiced')], 'Invoice Status')
    pharmacy_partner_id = fields.Many2one('res.partner',domain=[('is_pharmacy','=',True)], string='Pharmacy')
    prescription_line_ids = fields.One2many('medical.prescription.line','name','Prescription Line')
    invoice_done= fields.Boolean('Invoice Done')
    notes = fields.Text('Prescription Note')
    appointment_id = fields.Many2one('medical.appointment',string="appointment")
    is_invoiced = fields.Boolean(copy=False,default = False)
    insurer_id = fields.Many2one('medical.insurance', 'Insurer')
    is_shipped = fields.Boolean(default  =  False,copy=False)


    @api.model_create_multi
    def create(self , vals_list):
        for vals in vals_list:
            vals['name'] = self.env['ir.sequence'].next_by_code('medical.prescription.order') or '/'
        return super(medical_prescription_order, self).create(vals_list)


    def prescription_report(self):
        return self.env.ref('base_openemr.report_print_prescription').report_action(self)

    @api.onchange('name')
    def onchange_name(self):
        ins_obj = self.env['medical.insurance']
        ins_record = ins_obj.search([('medical_insurance_partner_id', '=', self.patient_id.patient_id.id)])
        self.insurer_id = ins_record.id or False

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
