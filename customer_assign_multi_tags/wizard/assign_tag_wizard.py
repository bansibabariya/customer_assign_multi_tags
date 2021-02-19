from odoo import api, fields, models, _

class AssignTags(models.TransientModel):
    _name = 'assign.tags'

    partner_ids = fields.Many2many(comodel_name="res.partner", string="Partner")
    tag_ids = fields.Many2many(comodel_name="res.partner.category", string="Tags")

    def action_assign_tags(self):
        if self.partner_ids:
            for partner in self.partner_ids:
                for tag in self.tag_ids:
                    partner.sudo().write({
                        'category_id': [(4, tag.id)],
                    })
        """ close wizard"""
        return {'type': 'ir.actions.act_window_close'}

















#       message_id = self.env['message.wizard'].create({'message': _("Invitation is successfully sent")})
#     def action_ok(self):
#         """ close wizard"""
#         return {'type': 'ir.actions.act_window_close'}
#
#         return {
#             'name': _('Successfull'),
#             'type': 'ir.actions.act_window',
#             'view_mode': 'form',
#             'res_model': 'message.wizard',
#             # pass the id
#             'res_id': message_id.id,
#             'target': 'current'
#                       ''
#         }