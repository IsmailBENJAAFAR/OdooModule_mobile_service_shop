from odoo import fields, models


class MobileBrand(models.Model):
    """This model represents the Mobile Brand"""
    _name = 'mobile.brand'
    _description = 'Mobile Brand'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'brand_name'

    brand_name = fields.Char(string="Mobile Brand", required=True,
                             help="Mobile Brand name")
