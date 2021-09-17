// Copyright (c) 2021, summayya and contributors
// For license information, please see license.txt
frappe.ui.form.on('Journal Entry', {
	refresh: function (frm) {
		frm.trigger("set_total_dr_cr");
	},

	company: function (frm) {
		frm.set_query("account", "account_entries", () => {
			return {
				filters: {
					company: frm.doc.company,
					is_group: 0
				}
			}
		})
	},

	set_total_dr_cr: function (frm) {
		let total_credit = 0;
		let total_debit = 0;
		if (frm.doc.account_entries) {
			frm.doc.account_entries.forEach((account) => {
				total_debit += account.debit;
				total_credit += account.credit;
			})
		}
		frm.set_value("total_debit", total_debit);
		frm.set_value("total_credit", total_credit);
		frm.refresh_fields();

	}
})

frappe.ui.form.on("Journal Account Entries", {
	debit: function (frm) {
		frm.trigger("set_total_dr_cr");
		frm.refresh_fields();
	},
	credit: function (frm) {
		frm.trigger("set_total_dr_cr");
		frm.refresh_fields();
	},
	account: function (frm, cdn, cdt) {
		let doc = frappe.get_doc(cdn, cdt);
		if(!frm.doc.company) {
			doc.account = "";
			frappe.throw(__("Please select a Company first"))	
			frm.refresh_field("account");
		}
		frm.refresh_field("account");
		
	},
	party: function (frm) {
		if(!frm.doc.company) {
			frappe.throw(__("Please select a Company first")
			)
		}
	}
})
