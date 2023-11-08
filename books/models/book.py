"""
    Modulo de libros
"""

from odoo import models, fields

class Book(models.Model):
    """ Clase de libros """
    _name = 'book'
    _description = 'Book'
    _rec_name = 'author'

    author = fields.Many2one(string='Author', comodel_name='res.partner', ondelete="cascade")
    book_copies = fields.One2many(string='Ejemplares', comodel_name='book_copy', ondelete="cascade", inverse_name="book_id")
    books_category_ids = fields.Many2many(string='Categorias', comodel_name='books_category')
    release_date = fields.Date(string='Fecha de lanzamiento',default=fields.Date.today)
    summary = fields.Char(string='Resumen')
    total_pages = fields.Char(string='Total de paginas')
    price = fields.Monetary(string='Precio',currency_field='currency_id')
    currency_id = fields.Many2one('res.currency',string='Moneda')
    author_continues_writing = fields.Boolean(string='¿El autor sigue escribiendo?')

