# Copyright (c) 2025, Galaxy DevOps Team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate


class GreenBond(Document):
	def validate(self):
		"""Validate the green bond"""
		# Maturity date must be after issue date
		if getdate(self.maturity_date) <= getdate(self.issue_date):
			frappe.throw("Maturity date must be after issue date")
		
		# Calculate totals from projects
		self.calculate_totals()
	
	def calculate_totals(self):
		"""Calculate total allocated amount and total CO2 avoided"""
		self.total_allocated = 0
		self.total_co2_avoided = 0
		
		for project in self.projects:
			if project.allocated_amount:
				self.total_allocated += project.allocated_amount
			if project.co2_avoided_tons:
				self.total_co2_avoided += project.co2_avoided_tons
