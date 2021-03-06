
from odoo import models, fields


class WizardOpStudent(models.TransientModel):
    _name = 'wizard.vm.student'
    _description = "Create User for selected Student(s)"

    def _get_students(self):
        if self.env.context and self.env.context.get('active_ids'):
            return self.env.context.get('active_ids')
        return []

    student_ids = fields.Many2many(
        'vm.student', default=_get_students, string='Students')

    def create_user(self):
        active_ids = self.env.context.get('active_ids', []) or []
        records = self.env['vm.student'].browse(active_ids)
        records.create_student_user()