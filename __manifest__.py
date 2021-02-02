# -*- coding: utf-8 -*-

##############################################################################

{
    'name' : 'Gestion des Inscriptions étudiants',
    'version': '1.0',
	'sequence': 5,
    'author' : 'Papa Daouda Faye',
    'website' : 'papadaoudafaye995@gmail.com',
    'category': 'Scool',
    'images': ['images/icone.png'],
    'depends' : ['base'],
    'description': """
        Ce module a été dévéloppé lors d' un tp sur la gestion des inscriptions des étudiants 
    """,
    'data': [
        'views/etudiant.xml',
        'views/etablissement.xml',
        'views/sequence.xml',
        'views/rapport.xml',
        'views/etudiant_rapport_carte.xml',
        'views/etudiant_rapport_liste.xml',
        'views/etudiant_rapport_inscription.xml',
        'menu/menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}

##############################################################################
