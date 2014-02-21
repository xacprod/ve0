# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContactMessage'
        db.create_table(u'etudevet_contactmessage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prenom', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('mail', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('form_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['etudevet.CategorieMessage'])),
        ))
        db.send_create_signal(u'etudevet', ['ContactMessage'])

        # Adding model 'CategorieMessage'
        db.create_table(u'etudevet_categoriemessage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('categorie', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'etudevet', ['CategorieMessage'])

        # Adding model 'Ville'
        db.create_table(u'etudevet_ville', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom_ville', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('pop_ville', self.gf('django.db.models.fields.IntegerField')()),
            ('classt_pop_ville', self.gf('django.db.models.fields.IntegerField')()),
            ('departement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['etudevet.Departement'])),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['etudevet.Region'])),
            ('depenses', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['etudevet.Depenses'])),
            ('tops', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['etudevet.Tops'])),
        ))
        db.send_create_signal(u'etudevet', ['Ville'])

        # Adding model 'Animal'
        db.create_table(u'etudevet_animal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_al', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('nombre_al', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre_med', self.gf('django.db.models.fields.IntegerField')()),
            ('ville', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['etudevet.Ville'])),
        ))
        db.send_create_signal(u'etudevet', ['Animal'])

        # Adding model 'Depenses'
        db.create_table(u'etudevet_depenses', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('indice', self.gf('django.db.models.fields.IntegerField')()),
            ('depense_cn', self.gf('django.db.models.fields.IntegerField')()),
            ('depence_ct', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'etudevet', ['Depenses'])

        # Adding model 'Tops'
        db.create_table(u'etudevet_tops', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_top', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('range_top', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('rank_top', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'etudevet', ['Tops'])

        # Adding model 'Region'
        db.create_table(u'etudevet_region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom_region', self.gf('django.db.models.fields.IntegerField')(max_length=60)),
        ))
        db.send_create_signal(u'etudevet', ['Region'])

        # Adding model 'Departement'
        db.create_table(u'etudevet_departement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom_departement', self.gf('django.db.models.fields.IntegerField')(max_length=60)),
        ))
        db.send_create_signal(u'etudevet', ['Departement'])


    def backwards(self, orm):
        # Deleting model 'ContactMessage'
        db.delete_table(u'etudevet_contactmessage')

        # Deleting model 'CategorieMessage'
        db.delete_table(u'etudevet_categoriemessage')

        # Deleting model 'Ville'
        db.delete_table(u'etudevet_ville')

        # Deleting model 'Animal'
        db.delete_table(u'etudevet_animal')

        # Deleting model 'Depenses'
        db.delete_table(u'etudevet_depenses')

        # Deleting model 'Tops'
        db.delete_table(u'etudevet_tops')

        # Deleting model 'Region'
        db.delete_table(u'etudevet_region')

        # Deleting model 'Departement'
        db.delete_table(u'etudevet_departement')


    models = {
        u'etudevet.animal': {
            'Meta': {'object_name': 'Animal'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_al': ('django.db.models.fields.IntegerField', [], {}),
            'nombre_med': ('django.db.models.fields.IntegerField', [], {}),
            'type_al': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'ville': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['etudevet.Ville']"})
        },
        u'etudevet.categoriemessage': {
            'Meta': {'object_name': 'CategorieMessage'},
            'categorie': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'etudevet.contactmessage': {
            'Meta': {'object_name': 'ContactMessage'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'form_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['etudevet.CategorieMessage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'etudevet.departement': {
            'Meta': {'object_name': 'Departement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom_departement': ('django.db.models.fields.IntegerField', [], {'max_length': '60'})
        },
        u'etudevet.depenses': {
            'Meta': {'object_name': 'Depenses'},
            'depence_ct': ('django.db.models.fields.IntegerField', [], {}),
            'depense_cn': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indice': ('django.db.models.fields.IntegerField', [], {})
        },
        u'etudevet.region': {
            'Meta': {'object_name': 'Region'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom_region': ('django.db.models.fields.IntegerField', [], {'max_length': '60'})
        },
        u'etudevet.tops': {
            'Meta': {'object_name': 'Tops'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'range_top': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'rank_top': ('django.db.models.fields.IntegerField', [], {}),
            'type_top': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'etudevet.ville': {
            'Meta': {'object_name': 'Ville'},
            'classt_pop_ville': ('django.db.models.fields.IntegerField', [], {}),
            'departement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['etudevet.Departement']"}),
            'depenses': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['etudevet.Depenses']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom_ville': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'pop_ville': ('django.db.models.fields.IntegerField', [], {}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['etudevet.Region']"}),
            'tops': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['etudevet.Tops']"})
        }
    }

    complete_apps = ['etudevet']