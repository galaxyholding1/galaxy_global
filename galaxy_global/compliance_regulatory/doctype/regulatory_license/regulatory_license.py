# Copyright (c) 2025, Galaxy DevOps Team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate


class RegulatoryLicense(Document):
	def validate(self):
		"""Validate the regulatory license"""
		# Check if expiry date is after issue date
		if self.expiry_date and getdate(self.expiry_date) < getdate(self.issue_date):
			frappe.throw("Expiry date cannot be before issue date")
		
		# Auto-deactivate if expired
		if self.expiry_date and getdate(self.expiry_date) < getdate():
			self.is_active = 0
			self.status = "Expired"
