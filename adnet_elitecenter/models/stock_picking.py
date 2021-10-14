# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models,api
from odoo.tools.translate import _ #IMPORTACION PARA MENSAJES DE ERROR

import logging

logger = logging.getLogger(__name__)



class StockPicking(models.Model):
    _inherit = 'stock.picking'
    

    user_pack_id = fields.Many2one(
        "res.users",
        compute="_compute_user_pack_id"
    )

    """
    location_pack_id = fields.Char(
        related="user_pack_id.location_pack_id.name"
    )
    """


    @api.depends('user_pack_id')
    def _compute_user_pack_id(self):
        for record in self:
            record.user_pack_id = self.env.user.id

    def action_confirm(self):
        res = super(StockPicking, self).action_confirm()
        logger.info(">>>>>>ADNETWORKS: action_confirm ")
        for pick in self:
            logger.info(">>>>>>ADNETWORKS: {}".format(pick))
            for lines in pick.move_line_ids:
                lines.onchange_location_dest_id()

        return res

    def button_validate(self):
        res = super(StockPicking, self).button_validate()
        logger.info(">>>>>>ADNETWORKS: button_validate ")

        for pick in self:
            logger.info(">>>>>>ADNETWORKS: {}".format(pick))
            for lines in pick.move_line_ids:
                lines.onchange_location_dest_id()

        return res
