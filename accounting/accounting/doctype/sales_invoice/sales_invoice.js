// Copyright (c) 2021, summayya and contributors
// For license information, please see license.txt

frappe.ui.form.on("Sales Invoice", {
	refresh: function (frm) {
		frm.trigger("set_total");
	},

	company: function (frm) {
		frm.set_query("credit_account", () => {
			return {
				filters: {
					name: `Sales - ${frm.doc.abbr}`,
					company: frm.doc.company,
				},
			};
		}),
			frm.set_query("debit_account", () => {
				return {
					filters: {
						name: `Debitors - ${frm.doc.abbr}`,
						company: frm.doc.company,
					},
				};
			});
	},

	set_total: function (frm) {
		let total_amount = 0;
		let total_quantity = 0;
		if (frm.doc.item) {
			frm.doc.item.forEach((item) => {
				total_amount += item.amount;
				total_quantity += item.quantity;
			});
		}
		frm.set_value("amount", total_amount);
		frm.set_value("total_quantity", total_quantity);
		frm.refresh_fields();
	},
});

frappe.ui.form.on("Invoice Item", {
	rate: function (frm, cdn, cdt) {
		let item = frappe.get_doc(cdn, cdt);
		item.amount = item.rate * item.quantity;
		frm.trigger("set_total");
		frm.refresh_field("item");
	},
	quantity: function (frm, cdn, cdt) {
		let item = frappe.get_doc(cdn, cdt);
		item.amount = item.rate * item.quantity;
		frm.trigger("set_total");
		frm.refresh_field("item");
	},
});
