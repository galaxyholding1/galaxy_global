# Copyright (c) 2025, Galaxy DevOps Team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GuaranteeFacility(Document):
	def validate(self):
		"""Validate the guarantee facility"""
		# Outstanding cannot exceed limit
		if self.outstanding_amount and self.limit_amount:
			if self.outstanding_amount > self.limit_amount:
				frappe.throw("Outstanding amount cannot exceed limit amount")
