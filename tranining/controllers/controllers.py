# -*- coding: utf-8 -*-
from odoo import http

# class ./src/user/tranining(http.Controller):
#     @http.route('/./src/user/tranining/./src/user/tranining/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./src/user/tranining/./src/user/tranining/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('./src/user/tranining.listing', {
#             'root': '/./src/user/tranining/./src/user/tranining',
#             'objects': http.request.env['./src/user/tranining../src/user/tranining'].search([]),
#         })

#     @http.route('/./src/user/tranining/./src/user/tranining/objects/<model("./src/user/tranining../src/user/tranining"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./src/user/tranining.object', {
#             'object': obj
#         })