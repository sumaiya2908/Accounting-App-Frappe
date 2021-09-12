// Copyright (c) 2021, summayya and contributors
// For license information, please see license.txt

frappe.ui.form.on('Company', {
	company_name: function(frm) {
		if(frm.doc.__islocal) {
			// add missing " " arg in split method
			let parts = frm.doc.company_name.split(" ");
			let abbr = $.map(parts, function (p) {
				return p? p.substr(0, 1) : null;
			}).join("");
			frm.set_value("abbrevation", abbr);
		}
	},
});
