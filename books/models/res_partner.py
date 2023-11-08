"""
    Modulo de libros
"""

from odoo import models, fields


class Books_Res_Partner(models.Model):
    """ Clase de Personas """

    _inherit = 'res.partner'
    books_ids = fields.One2many(string="Autor", comodel_name="book", inverse_name='author')
