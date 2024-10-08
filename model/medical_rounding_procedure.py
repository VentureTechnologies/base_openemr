# -*- coding: utf-8 -*-
# Part of Venture Technologies. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class medical_rounding_procedure(models.Model):
    _name = 'medical.rounding_procedure'
    _description = 'medical rounding procedure'

    notes = fields.Text(string="Notes") 
    medical_patient_rounding_procedure_id = fields.Many2one('medical.patient.rounding',string="Vaccines")