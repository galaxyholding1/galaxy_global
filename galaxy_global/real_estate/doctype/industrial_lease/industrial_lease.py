# Copyright (c) 2025, Galaxy DevOps Team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate


class IndustrialLease(Document):
	def validate(self):
		"""Validate the industrial lease"""
		# End date must be after start date
		if self.end_date and getdate(self.end_date) < getdate(self.start_date):
			frappe.throw("End date cannot be before start date")
