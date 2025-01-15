from odoo import fields, models


class TermsConditions(models.Model):
    """Used to add the Mobile Service Terms and Conditions"""
    _name = 'terms.conditions'
    _description = 'Terms and Conditions'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'terms_id'

    terms_id = fields.Char(String="Terms and condition",
                           compute="_compute_terms_id", help="this will be "
                                                             "the terms id.")
    terms_conditions = fields.Text(string="Terms and Conditions",
                                   help="this will be the terms and "
                                        "conditions space.")

    def _compute_terms_id(self):
        """Return the terms ID"""
        self.terms_id = self.id or ''
