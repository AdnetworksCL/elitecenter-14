# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models,api
from odoo.tools.translate import _ #IMPORTACION PARA MENSAJES DE ERROR

import logging

logger = logging.getLogger(__name__)



class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'
    

    @api.onchange('location_dest_id')
    def onchange_location_dest_id(self):
        sale_id = self.picking_id.sale_id.id
        logger.info(">>>>>>ADNETWORKS: WS FACTURA  METLIFE")
        logger.info(">>>>>>ADNETWORKS: PICKING_ID: {}".format(self.picking_id))
        logger.info(">>>>>>ADNETWORKS: SALE_ID: {}".format(self.picking_id.sale_id.id))
        logger.info(">>>>>>ADNETWORKS: PICKING_ID: {}".format(self.picking_id.id)) 
        logger.info(">>>>>>ADNETWORKS: NAME LOTACION: {}".format(self.location_dest_id.name)) 

        if self.location_dest_id.name == "Output":
            self.env.cr.execute(""" UPDATE stock_picking SET location_id=%s WHERE sale_id=%s AND picking_type_id=%s """,(11,sale_id,2))
        
        if self.location_dest_id.name == "Output2":
            self.env.cr.execute(""" UPDATE stock_picking SET location_id=%s WHERE sale_id=%s AND picking_type_id=%s """,(26,sale_id,2))

    