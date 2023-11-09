"""
    Modulo de libros
"""

from odoo import models, fields

class Book_Copy(models.Model):
    """ Clase de Ejemplares de libros """
    _name = 'book_copy'
    _description = 'Ejemplares'
    
    book_id = fields.Many2one(string='Ejemplar de libro', comodel_name='book')
    rented = fields.Boolean(string='Actualmente rentado', default=False)
    code = fields.Char(string='Codigo')
    res_partner_id = fields.Many2one(string='Quien lo tiene', comodel_name='res.partner', ondelete="cascade")
    status = fields.Selection([
            ('avaiable', "Esta en el estante"),
            ('rented', "Alquilado"),
            ('sold', "Vendido"),
        ], default='avaiable')
    
    def sale_wizard_status_action(self):
        return {
            'name': 'Sale Wizard Book Copy',
            'view_mode': 'form',
            'res_model': 'book.copy.wizard',
            'type': 'ir.actions.act_window',
            'context': {'default_book_copy_id': self.id,'default_book_id': self.book_id.id ,'default_status': self.status, 'default_res_partner_id': self.res_partner_id.id},
            'target': 'new'
        }