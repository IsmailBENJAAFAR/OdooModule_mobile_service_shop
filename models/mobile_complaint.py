from odoo import fields, models


class MobileComplaint(models.Model):
    """This model represents for the mobile Complaint type managing"""
    _name = 'mobile.complaint'
    _description = 'Mobile Complaint'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'complaint_type'

    complaint_type = fields.Char(string="Complaint Type", required=True,
                                 help="This field specifies the type of the "
                                      "complaint.")
