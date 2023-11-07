"""
    Modulo de libros
"""

from odoo import models, fields

class Book(models.Model):
    """ Clase de libros """
    _name = 'book'
    _description = 'Book'
    _rec_name = 'author'

    author = fields.Char(string='Author')
    release_date = fields.Date(string='Fecha de lanzamiento',default=fields.Date.today)
    summary = fields.Char(string='Resumen')
    total_pages = fields.Char(string='Total de paginas')
    author_continues_writing = fields.Boolean(string='¿El autor sigue escribiendo?')
