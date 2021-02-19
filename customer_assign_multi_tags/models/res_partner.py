from odoo import models, fields, api, _


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    def action_assign_tags(self):
        no_data = []
        for rec in self.browse(self.env.context['active_ids']):
            no_data.append(rec.id)
        if no_data:
            wizard_id = self.env['assign.tags'].sudo().create({'partner_ids': [(6,0,no_data)]})
            return {
                'name': _('Assign Tags'),
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'assign.tags',
                'res_id': wizard_id.id,
                'target': 'new'
            }
