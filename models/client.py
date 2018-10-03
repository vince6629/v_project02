#-*- coding: utf-8 -*-

from odoo import models,fields,api

class gestion_client(models.Model):
	_name = 'client'
	_description= 'la gestion des clients'
	champg0 = fields.Boolean('Done?')
	champg1 = fields.Char('Raison sociale')
	champg2 = fields.Char('Adresse')
	champg3 = fields.Char('CP')
	champg4 = fields.Char('Ville')
	champg5 = fields.Integer('A')
	champg6 = fields.Integer('B')
	annotationthirdfield=fields.Float(compute='_compute_sum',string="SUM")
	is_done = fields.Boolean('Done?')
	active = fields.Boolean('Active?')

	@api.onchange('champg5','champg6')

	def _compute_sum(self):
		self.annotationthirdfield = self.champg5 + self.champg6


	@api.multi
	def do_clear_done1(self):
		for client1 in self:
			client1.active = False
		return True

#	@api.multi
#	def do_2_done(self):
#		for client in self:
#			client.is_done = not client.is_done
#		return True


	@api.multi
	def write(self, values):
	# Before write logic
		if 'active' not in values:
			values['active'] = True
		return super(gestion_client, self).write(values)


