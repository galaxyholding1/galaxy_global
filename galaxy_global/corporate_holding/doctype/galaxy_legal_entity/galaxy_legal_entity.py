# Copyright (c) 2025, Galaxy DevOps Team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GalaxyLegalEntity(Document):
	def validate(self):
		"""Validate the legal entity"""
		# Prevent circular parent reference
		if self.parent_entity:
			if self.parent_entity == self.name:
				frappe.throw("An entity cannot be its own parent")
			
			# Check for circular references in hierarchy
			self.check_circular_reference()
	
	def check_circular_reference(self):
		"""Check if there's a circular reference in the parent hierarchy"""
		visited = set()
		current = self.parent_entity
		
		while current:
			if current in visited:
				frappe.throw("Circular reference detected in parent hierarchy")
			
			visited.add(current)
			parent_doc = frappe.get_doc("Galaxy Legal Entity", current)
			current = parent_doc.parent_entity
