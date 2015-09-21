# -*- coding: utf-8 -*-

{
    'name': 'Eurogerm - Gestion des CDC Fournisseur',
    'version': '1.0',
    'description': """
Avoir un état des cahiers des charges disponibles pour chaque fournisseur / partenaire   """,
    'author': 'Tony GALMICHE',
    'website': 'http://www.infosaone.com',
    'images': [],
    'depends': ['eurogerm_profile'],
    'init_xml': [],
    'update_xml': ['is_fournisseur_view.xml',
                   'is_cdc_fou_view.xml',
                   'report/report_cdc_fournisseur_view.xml',
                   ],
    'demo_xml': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
