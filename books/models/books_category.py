"""
     s
"""

from odoo import models, fields

class Books_Category(models.Model):
    """ Clase de libros """
    _name = 'books_category'
    _description = 'Category of books'
    _rec_name = 'name'

    name = fields.Char(string='Nombre')