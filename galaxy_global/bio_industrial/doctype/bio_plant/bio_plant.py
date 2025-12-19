# Copyright (c) 2025, Galaxy DevOps Team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class BioPlant(Document):
	def validate(self):
		"""Validate the bio plant"""
		# Ensure capacity is positive
		if self.capacity_tons_per_year and self.capacity_tons_per_year < 0:
			frappe.throw("Capacity must be a positive number")
