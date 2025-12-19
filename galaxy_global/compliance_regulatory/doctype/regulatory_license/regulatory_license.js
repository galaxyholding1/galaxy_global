// Copyright (c) 2025, Galaxy DevOps Team and contributors
// For license information, please see license.txt

frappe.ui.form.on('Regulatory License', {
	refresh: function(frm) {
		// Warning for licenses expiring soon (60 days)
		if (frm.doc.expiry_date && frappe.datetime.get_diff(frm.doc.expiry_date, frappe.datetime.now_date()) < 60 && frappe.datetime.get_diff(frm.doc.expiry_date, frappe.datetime.now_date()) >= 0) {
			frm.dashboard.add_comment(__('This license expires in less than 60 days'), 'yellow', true);
		}
		
		// Alert for expired licenses
		if (frm.doc.expiry_date && frappe.datetime.get_diff(frm.doc.expiry_date, frappe.datetime.now_date()) < 0) {
			frm.dashboard.add_comment(__('This license has expired'), 'red', true);
		}
	}
});
