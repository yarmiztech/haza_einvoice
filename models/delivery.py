from odoo import fields,models,api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    dc_no = fields.Char('DC-No')
    driver_id = fields.Many2one('res.partner')
    driver_mobile = fields.Char('Driver Mobile')
    truck_no = fields.Char('Truck No')


    @api.onchange('driver_id')
    def onchange_driver_mobile(self):
        self.driver_mobile = self.driver_id.mobile
        self.dc_no = self.driver_id.dc_no


class ResPartner(models.Model):
    _inherit = 'res.partner'

    dc_no = fields.Char('DC-No')


