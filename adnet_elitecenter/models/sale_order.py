# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models,api
from odoo.tools.translate import _ #IMPORTACION PARA MENSAJES DE ERROR


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    

    state_op = fields.Selection([
        ('draft', 'Borrador'),
        ('sac', 'SAC'),        
        ('rma', 'RMA')], default='draft',
        copy=False, track_visibility='onchange', required=True, string="Estado Operativo")

    sac_type = fields.Selection([
        ('draft', 'Borrador'),
        ('cancel', 'Cancelada'),
        ('change_delivery', 'Cambio de direccion'),        
        ('change_line', 'Cambio de lines del pedido')], default='draft',
        copy=False, track_visibility='onchange', required=True, string="Tipo SAC")