from odoo import api, models, fields
class FootballManager(models.Model):
    _inherit = 'football.person'
    _name = 'football.manager'
    team_id = fields.Many2one('football.team', string="Club")