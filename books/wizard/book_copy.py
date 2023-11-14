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
    date_finish = fields.Date(string='Fecha de finalizacion')
    

    def change_book_copy_state(self):

        var_date_finish = self.date_finish
        if self.status != 'rented':
            var_date_finish = None

        self.book_copy_id.write({'status': self.status, 'res_partner_id': self.res_partner_id, 'date_finish': var_date_finish} )

        if self.status in ['rented','sold']:
            template = self.env['mail.template'].search([('name', '=', 'mail.template.book_copy')], limit=1)
            # Renderizamos la plantilla con los datos de cada destinatario
            template.with_context(lang=self.res_partner_id.lang).send_mail(self.book_copy_id.id, force_send=True)
        

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: