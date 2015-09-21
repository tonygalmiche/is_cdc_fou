# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import time
import pooler
from osv import fields, osv
from tools.translate import _
import netsvc

class is_specification(osv.osv):
    _name = 'is.specification'
    _description = 'Specifications'

    #    #Fonction copiée de base.py
    #    def _get_directory_link(self, cr, uid, ids, field_name, args, context=None):
    #        """
    #        Compute Directories
    #        on filesystem
    #        """
    #        res = {}
    #        path_ext1 = ''
    #        path_ext2 = ''
    #        for partner in self.browse(cr, uid, ids, context=context):
    #            path_ext1 = partner.section_id and partner.section_id.code or ''
    #            path_ext2 = partner.internal_name or partner.name or ''
    #            user = self.pool.get('res.users').browse(cr, uid, uid)
    #            company = user.company_id
    #            res[partner.id] = {
    #                'link': 'file://' + os.path.join(company.supplier_files_server_path or '', '', path_ext2),
    #            }
    #        return res

    
    _columns = {
        'type_specification': fields.selection([('spec_product_part1', 'Specification product - Part 1 General Specifications'),
                                                ('spec_product_part2', 'Specification product - Part 2 Particular Specifications'),
                                                ('spec_delivery', 'Specification delivery'),
                                                ('spec_prod_sheet', 'Product Specification Sheets'),
                                                ('spec_transp', 'Specification Transport'),
                                                ('spec_consom', 'Specification Consumables'),
                                                ('term_sale', 'Terms of Sales')], 'Type specifications', required=True),
        'product_id': fields.many2one('product.product', 'Product Concerned'),
        'num_version': fields.char('N° release or index', size=5),
        'date_application': fields.date('Date of application'),
        'date_send': fields.date('Sending date'),
        'date_sign_supp': fields.date('Date Signature Supplier'),
        'comment': fields.text('Comment'),
        #'link': fields.char('Link', size=255),
        'link': fields.char('Link', size=255),
        'partner_id': fields.many2one('res.partner', 'Supplier', domain=[('supplier', '=', True)]),
        'state': fields.selection([('progress', 'In progress'),
                                   ('sent', 'Sent'),
                                   ('signed', 'Signed'),
                                   ('archived', 'Archived')], 'Status'),

    }
    

    #        'directory_link': fields.function(_get_directory_link, method=True, multi='link', store=True, string='Customer Directory', type='char', size=255),





    
    def duplicate_specification_line(self, cr, uid, ids, context=None):
        default = {'product_id': False}
        return self.copy(cr, uid, ids[0], default, context=context)
  
  
is_specification()


class res_partner(osv.osv):
    _inherit = 'res.partner'
    
    _columns = {
        'specification_ids': fields.one2many('is.specification', 'partner_id', 'Supplier Specifications'),
    }
    
res_partner()
