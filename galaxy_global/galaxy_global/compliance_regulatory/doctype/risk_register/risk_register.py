# Copyright (c) 2025, Galaxy DevOps Team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RiskRegister(Document):
	def validate(self):
		"""Validate the risk register"""
		# Validate probability and impact are between 1 and 5
		if self.probability and (self.probability < 1 or self.probability > 5):
			frappe.throw("Probability must be between 1 and 5")
		
		if self.impact and (self.impact < 1 or self.impact > 5):
			frappe.throw("Impact must be between 1 and 5")
		
		# Calculate risk score
		if self.probability and self.impact:
			self.risk_score = self.probability * self.impact
