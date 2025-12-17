// Copyright (c) 2025, Galaxy DevOps Team and contributors
// For license information, please see license.txt

frappe.ui.form.on('Certification', {
	refresh: function(frm) {
		// Highlight expired certificates
		if (frm.doc.expiry_date && frappe.datetime.get_diff(frm.doc.expiry_date, frappe.datetime.now_date()) < 0) {
			frm.dashboard.add_comment(__('This certificate has expired'), 'red', true);
		}
		
		// Warning for certificates expiring soon (30 days)
		if (frm.doc.expiry_date && frappe.datetime.get_diff(frm.doc.expiry_date, frappe.datetime.now_date()) < 30 && frappe.datetime.get_diff(frm.doc.expiry_date, frappe.datetime.now_date()) >= 0) {
			frm.dashboard.add_comment(__('This certificate expires in less than 30 days'), 'yellow', true);
		}
	}
});
