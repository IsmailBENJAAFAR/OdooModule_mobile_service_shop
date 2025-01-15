from odoo import fields, models


class MobileComplaintTree(models.Model):
    """Model for managing complaint details in mobile services."""
    _name = 'mobile.complaint.tree'
    _description = 'Mobile Complaint Tree'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'complaint_type_tree'

    complaint_id = fields.Many2one('mobile.service',
                                   string="Complaint ID",
                                   help="Complaint id associated with this "
                                        "record.")
    complaint_type_tree = fields.Many2one('mobile.complaint',
                                          string="Category",
                                          required=True,
                                          help="Complaint type tree records.")
    description_tree = fields.Many2one('mobile.complaint.description',
                                       string="Description",
                                       domain="[('complaint_type_template',"
                                              "'=',complaint_type_tree)]",
                                       help="Description field for the "
                                            "complaint.")
