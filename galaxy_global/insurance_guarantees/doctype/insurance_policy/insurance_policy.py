# Copyright (c) 2025, Galaxy DevOps Team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate


class InsurancePolicy(Document):
	def validate(self):
		"""Validate the insurance policy"""
		# Check if end date is after start date
		if self.policy_end_date and getdate(self.policy_end_date) < getdate(self.policy_start_date):
			frappe.throw("Policy end date cannot be before start date")
