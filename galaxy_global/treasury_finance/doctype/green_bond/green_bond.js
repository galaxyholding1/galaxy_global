// Copyright (c) 2025, Galaxy DevOps Team and contributors
// For license information, please see license.txt

frappe.ui.form.on('Green Bond', {
	refresh: function(frm) {
		// Add custom buttons or logic here
	}
});

frappe.ui.form.on('Green Bond Project', {
	allocated_amount: function(frm, cdt, cdn) {
		// Recalculate totals when allocated amount changes
		frm.trigger('calculate_totals');
	},
	
	co2_avoided_tons: function(frm, cdt, cdn) {
		// Recalculate totals when CO2 avoided changes
		frm.trigger('calculate_totals');
	},
	
	projects_remove: function(frm) {
		// Recalculate totals when a project is removed
		frm.trigger('calculate_totals');
	}
});

frappe.ui.form.on('Green Bond', {
	calculate_totals: function(frm) {
		let total_allocated = 0;
		let total_co2_avoided = 0;
		
		frm.doc.projects.forEach(function(project) {
			total_allocated += project.allocated_amount || 0;
			total_co2_avoided += project.co2_avoided_tons || 0;
		});
		
		frm.set_value('total_allocated', total_allocated);
		frm.set_value('total_co2_avoided', total_co2_avoided);
	}
});
