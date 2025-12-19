# Copyright (c) 2025, Galaxy DevOps Team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate


class RegulatoryObligation(Document):
	def validate(self):
		"""Validate the regulatory obligation"""
		# Auto-mark as overdue if past deadline
		if self.next_deadline and getdate(self.next_deadline) < getdate():
			if self.status not in ["Completed", "N/A"]:
				self.status = "Overdue"
