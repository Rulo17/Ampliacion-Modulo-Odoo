from odoo import api, models, fields
class FootballMatch(models.Model):
    _name = 'football.match'
    startTime = fields.Date(string="Start Time")
    endTime = fields.Date(string="End Time")
    duration = fields.Char(string="Match Length")
    team_ids = fields.Many2many('football.team', 'football_teams_match_rel', 'match_id', 'team_id', string="Teams")
