// Copyright (c) 2025, Galaxy DevOps Team and contributors
// For license information, please see license.txt

frappe.ui.form.on('Regulatory Obligation', {
	refresh: function(frm) {
		// Warning for obligations due soon (15 days)
		if (frm.doc.next_deadline && frappe.datetime.get_diff(frm.doc.next_deadline, frappe.datetime.now_date()) < 15 && frappe.datetime.get_diff(frm.doc.next_deadline, frappe.datetime.now_date()) >= 0) {
			frm.dashboard.add_comment(__('Deadline is approaching (less than 15 days)'), 'yellow', true);
		}
		
		// Alert for overdue obligations
		if (frm.doc.next_deadline && frappe.datetime.get_diff(frm.doc.next_deadline, frappe.datetime.now_date()) < 0 && frm.doc.status !== 'Completed') {
			frm.dashboard.add_comment(__('This obligation is overdue'), 'red', true);
		}
	}
});
