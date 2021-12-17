from odoo import api, models, fields
class FootballPlayer(models.Model):
    _inherit = 'football.person'
    _name = 'football.player'
    team_id = fields.Many2one('football.team', string="Club")

    pace = fields.Integer(string="Pace")
    strength = fields.Integer(string="Strength")
    shot = fields.Integer(string="Shot")
    defense = fields.Integer(string="Defense")
    rating = fields.Integer(string="Rating", compute='_get_rating')

    @api.depends('pace', 'strength', 'shot', 'defense')
    def _get_rating(self):
        for record in self:
            record.rating = (record.pace + record.strength + record.shot + record.defense) / 4