from odoo import api, models, fields
class FootballTeam(models.Model):
    _name = 'football.team' #IMPORTANTE poner el name con minúsculas.
    name = fields.Char(string="Name", required=True)
    country = fields.Char(string="Country")
    year = fields.Integer(string="Foundation Year")
    player_ids = fields.One2many('football.player', 'team_id', string="Lineup")
    manager_ids = fields.One2many('football.manager', 'team_id', string="Manager")
    match_ids = fields.Many2many('football.match', 'football_teams_match_rel', 'team_id', 'match_id', string="Matches")