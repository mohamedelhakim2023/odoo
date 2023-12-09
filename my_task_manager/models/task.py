from odoo import models, fields


class TodoTask(models.Model):
    _name = 'beginner_task.todo'
    _description = 'To-Do Task'

    name = fields.Char('Task Name', required=True)
    description = fields.Text('Description')
    priority = fields.Selection([('low', 'Low'), ('medium', 'Medium'), ('high', 'High')],
                                'Priority', default='medium')
    date_deadline = fields.Datetime('Deadline')
    user_id = fields.Many2one('res.users', 'Assigned To')
