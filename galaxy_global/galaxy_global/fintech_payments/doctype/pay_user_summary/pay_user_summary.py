# Copyright (c) 2025, Galaxy DevOps Team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PayUserSummary(Document):
	def validate(self):
		"""Calculate statistics"""
		if self.monthly_tx_volume and self.total_transactions and self.total_transactions > 0:
			self.average_tx_size = self.monthly_tx_volume / self.total_transactions
