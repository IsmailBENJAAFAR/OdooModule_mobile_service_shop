from odoo import fields, models


class BrandModel(models.Model):
    """This class represents a mobile brand model"""
    _name = 'brand.model'
    _description = 'Brand Model'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'mobile_brand_models'

    mobile_brand_name = fields.Many2one('mobile.brand',
                                        string="Mobile Brand", required=True,
                                        help="Brand name of the mobile")
    mobile_brand_models = fields.Char(string="Model Name", required=True,
                                      help="Model name of the mobile")
    image_medium = fields.Binary(string='image', store=True, attachment=True,
                                 help="Mobile image space")
