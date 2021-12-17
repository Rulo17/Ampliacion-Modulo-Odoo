#Creo esta clase exclusivamente para que me hereden sus atributos tanto player como manager.
from odoo import api, models, fields
class FootballPerson(models.Model):
    _name = 'football.person'
    name = fields.Char(string="Name", required=True)
    lastname = fields.Char(string="Last Name", required=True)
    age = fields.Integer(string="Age")
    country = fields.Char(string="Country")