from odoo import models, fields, api

class patient_attachment(models.Model):
    _inherit = 'ir.attachment'

    def action_delete_attachment(self):
        self.unlink()