// Copyright (c) 2025, Galaxy DevOps Team and contributors
// For license information, please see license.txt

frappe.ui.form.on('Galaxy Legal Entity', {
	refresh: function(frm) {
		// Add custom buttons or logic here
		if (!frm.is_new()) {
			frm.add_custom_button(__('View Hierarchy'), function() {
				frappe.set_route('Tree', 'Galaxy Legal Entity');
			});
		}
	}
});
