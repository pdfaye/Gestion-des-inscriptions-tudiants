# -*- coding: utf-8 -*-

from odoo import models, fields, _, api

class Etablissement(models.Model):
    _name ='tp.etablissement.pdfaye'
    _description=u'Etablissement'
    _rec_name='nom_eta'

    nom_eta= fields.Char(string="Etablissement ", required=True)
    etudiant_ids=fields.One2many('tp.etudiant.pdfaye', 'etablissement_id', string="Etudiants")
    faculte_ids= fields.One2many('tp.faculte.pdfaye', 'etablissement_id', string="Faculté")



class Faculte(models.Model):
    _name ='tp.faculte.pdfaye'
    _description=u'Liste facultés'
    _rec_name='nom_fac'

    nom_fac= fields.Char(string="Faculté ", required=True)
    etablissement_id=fields.Many2one(comodel_name='tp.etablissement.pdfaye', required=True)
    etudiant_ids=fields.One2many('tp.etudiant.pdfaye', 'faculte_id', string="Etudiants")
    departement_ids=fields.One2many(comodel_name='tp.departement.pdfaye', inverse_name='faculte_id')



class Departement(models.Model):
    _name ='tp.departement.pdfaye'
    _description=u'Liste départements'
    _rec_name='nom_dep'

    nom_dep= fields.Char(string="Département :", required=True)
    faculte_id=fields.Many2one(comodel_name='tp.faculte.pdfaye', required=True)
    etudiant_ids=fields.One2many('tp.etudiant.pdfaye', 'departement_id', string="Etudiants")
    filliere_ids=fields.One2many(comodel_name='tp.filliere.pdfaye', inverse_name='departement_id')



class Filliere(models.Model):
    _name ='tp.filliere.pdfaye'
    _description=u'Liste fillières'
    _rec_name='nom_fil'

    nom_fil= fields.Char(string="Fillière :", required=True)
    etudiant_ids=fields.One2many('tp.etudiant.pdfaye', 'filliere_id', string="Etudiants")
    classe_ids=fields.One2many('tp.classe.pdfaye', 'filliere_id',  string="Etudiants")
    departement_id=fields.Many2one(comodel_name='tp.departement.pdfaye', required=True)


class Classe(models.Model):
    _name ='tp.classe.pdfaye'
    _description=u'Liste des classes'
    _rec_name='nom_clas'

    nom_clas= fields.Char(string="Nom de la classe ", required=True)
    filliere_id=fields.Many2one(comodel_name='tp.filliere.pdfaye', required=True)
    etudiant_ids=fields.One2many('tp.etudiant.pdfaye', 'classe_id' , string="Etudiants")
    eu_ids=fields.One2many(comodel_name='tp.ue.pdfaye', inverse_name='classe_id')


class UE(models.Model):
    _name ='tp.ue.pdfaye'
    _description=u'Liste des UE'
    _rec_name='nom_ue'

    nom_ue= fields.Char(string="Nom de l'UE ", required=True)
    classe_id=fields.Many2one(comodel_name='tp.classe.pdfaye', required=True)
    ec_ids=fields.One2many(comodel_name='tp.ec.pdfaye', inverse_name='ue_id')
    etudiant_ids=fields.Many2many(comodel_name='tp.etudiant.pdfaye',
                           relation='ue_etudiant_rel',
                           column1='nom_ue',
                           column2='first_name')

class EC(models.Model):
    _name ='tp.ec.pdfaye'
    _description=u'Liste des EC'
    _rec_name='nom_ec'

    nom_ec= fields.Char(string="Nom de l'EC ", required=True)
    ue_id=fields.Many2one(comodel_name='tp.ue.pdfaye', required=True)
