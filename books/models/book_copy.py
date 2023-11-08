"""
    Modulo de libros
"""

from odoo import models, fields

class Book_Copy(models.Model):
    """ Clase de Ejemplares de libros """
    _name = 'book_copy'
    _description = 'Ejemplares'
    
    book_id = fields.Many2one(string='Libro de ejemplar', comodel_name='book')
    rented = fields.Boolean(string='Actualmente rentado', default=False)
    code = fields.Char(string='Codigo')
