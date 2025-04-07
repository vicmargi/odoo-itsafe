# -*- coding: utf-8 -*-
# from odoo import http


# class Itsafe(http.Controller):
#     @http.route('/itsafe/itsafe', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/itsafe/itsafe/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('itsafe.listing', {
#             'root': '/itsafe/itsafe',
#             'objects': http.request.env['itsafe.itsafe'].search([]),
#         })

#     @http.route('/itsafe/itsafe/objects/<model("itsafe.itsafe"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('itsafe.object', {
#             'object': obj
#         })

