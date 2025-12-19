# Copyright (c) 2025, Galaxy DevOps Team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate


class IntercompanyLoan(Document):
	def validate(self):
		"""Validate the intercompany loan"""
		# Lender and borrower cannot be the same
		if self.lender == self.borrower:
			frappe.throw("Lender and borrower cannot be the same entity")
		
		# Maturity date must be after loan date
		if getdate(self.maturity_date) <= getdate(self.loan_date):
			frappe.throw("Maturity date must be after loan date")
		
		# Initialize outstanding amount
		if not self.outstanding_amount:
			self.outstanding_amount = self.principal_amount
