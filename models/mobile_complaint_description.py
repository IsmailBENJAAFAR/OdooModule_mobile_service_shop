from odoo import fields, models


class MobileComplaintDescription(models.Model):
    """This model represents description about the mobile Complaint"""
    _name = 'mobile.complaint.description'
    _description = "Mobile Complaint Description"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'description'

    complaint_type_template = fields.Many2one('mobile.complaint',
                                              string="Complaint Type",
                                              required=True,
                                              help="Complaint type template.")
    description = fields.Text(string="Description",
                              help="Complaint description.")
