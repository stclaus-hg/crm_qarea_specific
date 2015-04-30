from openerp import fields, models

class crm_qarea_specific(models.Model):
  _inherit = 'crm.lead'
  qarea_budget_bool = fields.Boolean('Budget available', default=False)
  qarea_budget_size = fields.Integer('Budget size', default=False)
  qarea_nda = fields.Boolean('NDA', default=False, select=True)
  qarea_project_name = fields.Char('Project name', default=False)
  qarea_redmine_project_link = fields.Char('Redmine project', default=False)
  qarea_redmine_est_link = fields.Char('Redmine estimation', default=False)
  skype = fields.Char('Skype', default=False)
  categ_ids = fields.Many2many(select=True)
  source_id = fields.Many2one(select=True, required=True)
  description = fields.Text(required=True)
  partner_id = fields.Many2one(required=True)

#  qarea_main_contact = fields.Many2one('crm.lead.main.contact', required=True)

class CrmLeadMainContact(models.Model):
    _name = 'crm.lead.main.contact'
    _description = 'Main Contact'

    name = fields.Char('Main Contact', required=True)
