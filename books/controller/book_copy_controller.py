import json
from odoo.http import Controller, request, route
import base64

class BookCoppyController(Controller):

    @route('/ejemplares', type='http', auth='public')
    def ejemplares(self):
        ejemplares = request.env['book_copy'].sudo().search([])

        if ejemplares:
            # Construir un diccionario con los datos que deseas exponer
            data = []
            data.append({
                'id': ejemplares.id,
                'book_id': ejemplares.book_id.name,
                'code': ejemplares.code,
                'estado': ejemplares.status,
                'date_finish': ejemplares.date_finish,
            })
            return request.make_response(json.dumps(data))
        else:
            return request.make_response(json.dumps({'error': 'Ejemplar no encontrado'}))
    
    @route('/ejemplares/<int:id>', type='http', auth='public', website=True)
    def ejemplar(self, id, **kwargs):
        ejemplar = request.env['book_copy'].sudo().search([('id', '=', id)])

        if ejemplar:
            # Construir un diccionario con los datos que deseas exponer
            data = {
                'id': ejemplar.id,
                'book_id': ejemplar.book_id.name,
                'code': ejemplar.code,
                'estado': ejemplar.status,
                'date_finish': ejemplar.date_finish,
                'res_partner_id': ejemplar.res_partner_id.name,
            }
            return request.make_response(json.dumps(data))
        else:
            return request.make_response(json.dumps({'error': 'Ejemplar no encontrado'}))
        
    @route('/report/pdf/report_book_copy/<int:record_id>', type='http', auth='user')
    def report_pdf(self, record_id, **kw):
        # Obtener el informe
        report = request.env['ir.actions.report'].search([('report_name', '=', 'report_book_copy')], limit=1)
        if not report:
            return request.not_found()

        # Obtener el registro
        record = request.env[report.model].browse(record_id)

        # Obtener el informe QWeb
        report_qweb = request.env['ir.ui.view'].search([('name', '=', report.report_name)], limit=1)

        # Renderizar el informe QWeb a PDF
        pdf_content, _ = request.env['report_book_copy'].sudo()._render_qweb_pdf([record.id], report_qweb.id)

        # Devolver el PDF como respuesta
        response = request.make_response(base64.b64decode(pdf_content), headers=[
            ('Content-Type', 'application/pdf'),
            ('Content-Disposition', 'attachment; filename=%s.pdf' % record.name)
        ])
        return response