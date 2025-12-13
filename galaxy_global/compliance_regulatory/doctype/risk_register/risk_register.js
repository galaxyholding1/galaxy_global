// Copyright (c) 2025, Galaxy DevOps Team and contributors
// For license information, please see license.txt

frappe.ui.form.on('Risk Register', {
	refresh: function(frm) {
		// Color-code risk score
		if (frm.doc.risk_score) {
			if (frm.doc.risk_score >= 15) {
				frm.dashboard.add_comment(__('High Risk (Score: ' + frm.doc.risk_score + ')'), 'red', true);
			} else if (frm.doc.risk_score >= 8) {
				frm.dashboard.add_comment(__('Medium Risk (Score: ' + frm.doc.risk_score + ')'), 'yellow', true);
			} else {
				frm.dashboard.add_comment(__('Low Risk (Score: ' + frm.doc.risk_score + ')'), 'green', true);
			}
		}
	},
	
	probability: function(frm) {
		calculate_risk_score(frm);
	},
	
	impact: function(frm) {
		calculate_risk_score(frm);
	}
});

function calculate_risk_score(frm) {
	if (frm.doc.probability && frm.doc.impact) {
		frm.set_value('risk_score', frm.doc.probability * frm.doc.impact);
	}
}
