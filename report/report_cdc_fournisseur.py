# -*- coding: utf-8 -*-


import tools
from osv import fields,osv

class report_cdc_fournisseur(osv.osv):
    _name = "report.cdc.fournisseur"
    _description = "Report CDC"
    _auto = False
    _columns = {
        'date': fields.date('Date', readonly=True),
        'year': fields.char('Year', size=4, readonly=True),
        'day': fields.char('Day', size=128, readonly=True),
        'month':fields.selection([('01','January'), ('02','February'), ('03','March'), ('04','April'),
            ('05','May'), ('06','June'), ('07','July'), ('08','August'), ('09','September'),
            ('10','October'), ('11','November'), ('12','December')], 'Month',readonly=True),
        'partner_id': fields.many2one('res.partner', 'Supplier', readonly=True),
        'product_id': fields.many2one('product.product', 'Product', readonly=True),
        'nb_deliveries': fields.integer('#Nb Deliveries', readonly=True),
        'qty_deliveries': fields.float('#Qty Deliveries', readonly=True),
    }
    
    
    def init(self, cr):
        tools.drop_view_if_exists(cr, 'report_cdc_fournisseur')
        cr.execute("""
            create or replace view report_cdc_fournisseur as (
                 select
                     min(mov.id) as id,
                     mov.date as date,
                     to_char(mov.date, 'YYYY') as year,
                     to_char(mov.date, 'MM') as month,
                     to_char(mov.date, 'YYYY-MM-DD') as day,
                     spec.partner_id as partner_id, 
                     mov.product_id as product_id, 
                     count(mov.id) as nb_deliveries, 
                     sum(mov.product_qty) as qty_deliveries 
                     
                from stock_move mov INNER JOIN stock_picking picking ON picking.id = mov.picking_id
                                    LEFT OUTER JOIN is_specification spec ON mov.product_id = spec.product_id 
                                                    AND spec.type_specification = 'spec_product_part2' 
                WHERE mov.state = 'done' AND picking.type = 'out' AND mov.date>='2015-04-01 00:00:00' and spec.id is null 
                GROUP BY spec.partner_id, mov.product_id, mov.date
                ORDER BY spec.partner_id, mov.product_id, mov.date
            )
        """)
        
report_cdc_fournisseur()


# Cette requete avec le fournisseur fait planter Odoo
#            create or replace view report_cdc_fournisseur as (
#                 select
#                     min(mov.id) as id,
#                     mov.date as date,
#                     to_char(mov.date, 'YYYY') as year,
#                     to_char(mov.date, 'MM') as month,
#                     to_char(mov.date, 'YYYY-MM-DD') as day,
#                     sup.name as partner_id, 
#                     mov.product_id as product_id, 
#                     count(mov.id) as nb_deliveries, 
#                     sum(mov.product_qty) as qty_deliveries 
#                     
#                from stock_move mov INNER JOIN stock_picking picking ON picking.id = mov.picking_id
#                                    INNER JOIN product_supplierinfo sup   ON mov.product_id = sup.product_id
#                                    LEFT OUTER JOIN is_specification spec ON sup.product_id = spec.product_id and sup.name=spec.partner_id 
#                                                    AND spec.type_specification = 'spec_product_part2' 

#                WHERE mov.state = 'done' AND picking.type = 'out' AND mov.date>='2015-04-01 00:00:00' and spec.id is null 
#                GROUP BY sup.name, mov.product_id, mov.date
#                ORDER BY sup.name, mov.product_id, mov.date
#            )




