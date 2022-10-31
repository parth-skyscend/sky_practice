from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for rec in self.picking_ids:
            rec.action_confirm()
            rec.action_assign()
            rec.action_set_quantities_to_reservation()
            rec.button_validate()
            rec._pre_action_done_hook()
            rec._action_done()
        return res
