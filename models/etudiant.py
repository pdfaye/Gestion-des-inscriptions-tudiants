# -*- coding: utf-8 -*-

from odoo import models, fields, _, api

class Etudiant(models.Model):
    _name ='tp.etudiant.pdfaye'
    _description=u'Etudiant'
    _rec_name='numero_seq'

    photo=fields.Binary(string="Photo", required=False)
    first_name= fields.Char(string="Prénom ")
    last_name= fields.Char(string="Nom de famille ", required=True)
    lieu_naissance= fields.Char(string="Lieu de naissance ", required=True)
    date_naissance= fields.Date(string="Date de naissance ", required=True)
    telephone_etudiant= fields.Char(string="Téléphone étudiant ", required=True)
    email_personnel= fields.Char(string="Email Personnel: ", required=True)
    sexe= fields.Selection([('m', 'Masculin'),('f', 'Féminin')], required=False)
    adresse= fields.Char(string="Adresse ", required=False)
    categorie_socioprofessionnelle=fields.Char(string="Catégorie Socioprofessionnelle ", required=False)
    statut_etudiant = fields.Selection([('rn', 'Régime Normale'),('rs','Régime salarié'),('rp', 'Régime Particulier'),('mps','Mise en position de stage ')],string="Statut de l'Etudiant", required=False)
    situation_matrimoniale= fields.Selection([('c', 'Célibataire'),('m','Marié(e)'),('d', 'Divorcé(e)')],string="Situation Matrimoniale", required=False)
    nombre_enfant=fields.Integer(string="Nombre d'enfant ", required=False)
    annee_bac= fields.Char(string="Année Obtention Bac ", required=True)
    mention=fields.Selection([('p', 'Passable'),('ab','Assez Bien'),('b', 'Bien'),('tb', 'Très Bien')],string="Mention au bac", required=False)
    serie_bac= fields.Char(string="Série Bac ", required=False)
    lieu= fields.Char(string="Lieu ", required=False)
    boursier=fields.Boolean(string="Boursier ", default=False, required=False)
    type_bourse= fields.Selection([('demi', 'Demi Bourse'),('entier','Bourse Entier')],string="Type de Bourse :", required=False)
    region_naissance=fields.Selection([('dk', 'Dakar'),('th','Thiès'),('sl', 'Saint Luis'),('lg', 'Louga'),
        ('mt', 'Matam'),('db','Diourbel'),('ft', 'Fatick'),('kl', 'Kaolack'),('kg', 'Kédougou'),
        ('z', 'Zinguichor'),('kf', 'Kafrine'),('kd','Kolda'),('sd', 'Sedhiou'),('tm', 'Tambacoinda')],string="Région :", required=False)
    nationality_id=fields.Many2one('res.country',string="Pays de naissance",required=False   )
    montant_bourse= fields.Char(string="Montant de la Bourse", required=False)
    tuteur= fields.Selection([('father', 'Père'),('mother', 'Mére'),('uncle', 'Oncle'),('other', 'Autres')],string="Tuteur :", required=False)
    nom_tuteur=fields.Char(string="Nom :", required=False)
    prenom_tuteur=fields.Char(string="Prénom :", required=False)
    telephone_tuteur= fields.Char(string="Téléphone : ", required=False)
    numero_seq=fields.Char(string="Dossier : ", required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    cycle=fields.Selection([('l','Licence'),('m', 'Master'),('d', 'Doctorat')], string="Cycle :", required=False)
    licence=fields.Selection([('l1', 'Licence 1'),('l2', 'Licence 2'),('l3', 'Licence 3')], string="Licence :", required=False)
    master=fields.Selection([('m1', 'Master 1'),('m2', 'Master 2')],string="Master :", required=False)
    doctorat=fields.Selection([('d1', '1er année'),('d2', '2eme année'),('d3', '3eme année')], string="Doctorat :", required=False)
    etablissement_id=fields.Many2one('tp.etablissement.pdfaye', string="Etablissement", required=False)
    faculte_id=fields.Many2one('tp.faculte.pdfaye', string="Faculte", required=False)
    departement_id=fields.Many2one('tp.departement.pdfaye', string="Departement", required=False)
    filliere_id=fields.Many2one('tp.filliere.pdfaye', string="Filliere", default=None, required=False)
    classe_id=fields.Many2one('tp.classe.pdfaye', string="Classe", default=None, required=False)
    ue_ids=fields.Many2many(comodel_name='tp.ue.pdfaye', 
                     relation='etudiant_ue_rel', 
                     column1='first_name', 
                     column2='nom_ue')

    @api.model
    def create(self, vals):
        if vals.get('numero_seq', _('New')) == _('New'):
            vals['numero_seq'] = self.env['ir.sequence'].next_by_code('pdfaye_etudiant_sequence') or _('New')
        result = super(Etudiant, self).create(vals)
        return result

    @api.multi
    @api.onchange('type_bourse')
    def on_change_state_bourse(self):
        if self.type_bourse=='demi':
            self.montant_bourse = '20000'
        elif self.type_bourse=='entier':
            self.montant_bourse = '40000'

    @api.multi
    @api.onchange('filliere_id')
    def on_change_state(self):
        if self.filliere_id!='':
            self.departement_id = self.filliere_id.departement_id
            self.faculte_id=self.filliere_id.departement_id.faculte_id
            self.etablissement_id=self.filliere_id.departement_id.faculte_id.etablissement_id
            self.ue_ids=self.filliere_id.classe_ids.eu_ids



