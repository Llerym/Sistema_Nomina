# -*- coding: utf-8 -*-
# from odoo import http


# class CinepolisRrhh(http.Controller):
#     @http.route('/cinepolis_rrhh/cinepolis_rrhh', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cinepolis_rrhh/cinepolis_rrhh/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cinepolis_rrhh.listing', {
#             'root': '/cinepolis_rrhh/cinepolis_rrhh',
#             'objects': http.request.env['cinepolis_rrhh.cinepolis_rrhh'].search([]),
#         })

#     @http.route('/cinepolis_rrhh/cinepolis_rrhh/objects/<model("cinepolis_rrhh.cinepolis_rrhh"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cinepolis_rrhh.object', {
#             'object': obj
#         })

