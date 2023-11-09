from odoo import models, fields

class BookCopyWizard(models.TransientModel):
    _name = 'book.copy.wizard'
    _description = 'Wizard for Book Copies'

    book_copy_id = fields.Many2one(string='Ejemplar de libro', comodel_name='book_copy')
    res_partner_id = fields.Many2one(string='Quien lo tiene', comodel_name='res.partner', ondelete="cascade")
    status = fields.Selection([
            ('avaiable', "Esta en el estante"),
            ('rented', "Alquilado"),
            ('sold', "Vendido"),
        ], default='avaiable')
    

    def change_book_copy_state(self):
        self.book_copy_id.write({'status': self.status, 'res_partner_id': self.res_partner_id})

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: