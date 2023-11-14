"""
    Modulo de libros
"""

from odoo import models, fields

class Book(models.Model):
    """ Clase de libros """
    _name = 'book'
    _description = 'Book'

    name = fields.Char(string='Titulo del libro', required=True)
    author = fields.Many2one(string='Author', comodel_name='res.partner', ondelete="cascade", required=True)
    book_copies = fields.One2many(string='Ejemplares', comodel_name='book_copy', ondelete="cascade", inverse_name="book_id")
    books_category_ids = fields.Many2many(string='Categorias', comodel_name='books_category')
    release_date = fields.Date(string='Fecha de lanzamiento',default=fields.Date.today)
    summary = fields.Char(string='Resumen')
    total_pages = fields.Char(string='Total de paginas', required=True)
    price = fields.Monetary(string='Precio',currency_field='currency_id', required=True)
    currency_id = fields.Many2one('res.currency',string='Moneda', required=True)
    author_continues_writing = fields.Boolean(string='¿El autor sigue escribiendo?')

