from odoo import models, fields, api, _


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    @api.multi
    def action_assign_tags(self):
        no_data = []
        for rec in self.browse(self.env.context['active_ids']):
            no_data.append(rec.id)
        if no_data:
            wizard_id = self.env['assign.tags'].sudo().create({'partner_ids': [(6,0,no_data)]})
            view = self.env.ref('customer_assign_multi_tags.model_assign_tags_form')

            return {
                'name': _("Assign Tags"),
                'view_mode': 'form',
                'view_id': view.id,
                'context': {'default_partner_ids': [(6,0,no_data)]},
                'view_type': 'form',
                'res_model': 'assign.tags',
                'type': 'ir.actions.act_window',
                'target': 'new',

            }
