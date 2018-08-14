# -*- coding: utf-8 -*-
from odoo import api, fields, models, SUPERUSER_ID, tools,  _

class DynamicField(models.TransientModel):
    _name = 'dynamic.field'
    _description = 'Add Custom Field'

    name = fields.Char(string='Field Name', default='x_', required=True, help='Mension this name in salary rule')
    complete_name = fields.Char('Field Label')

    @api.multi
    def add_field(self):
        model_id = self.env['ir.model'].search([('model', '=', 'hr.contract')], limit=1)
        field = self.env['ir.model.fields'].create({
            'model_id':model_id.id,
            'name': self.name,
            'field_description': self.complete_name+'('+self.name+')',
            'ttype': 'float',
        })
        arch_base = _('<?xml version="1.0"?>'
                      '<data>'
                      '<field name="job_id" position="after">'
                      '<field name="%s"/>'
                      '</field>'
                      '</data>') % (self.name)
        inherit_id = self.env.ref('hr_contract.hr_contract_view_form')
        self.env['ir.ui.view'].sudo().create({'name': model_id.model,
                                              'type': 'form',
                                              'model': model_id.model,
                                              'mode': 'extension',
                                              'inherit_id': inherit_id.id,
                                              'arch_base': arch_base,
                                              'active': True})
        return {'type': 'ir.actions.client',
                    'tag': 'reload',
                     }