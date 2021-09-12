// Copyright (c) 2021, summayya and contributors
// For license information, please see license.txt

frappe.ui.form.on("Payment Entry", {
	// returns the company's accounts in account field
	payment_type: function (frm) {
		if (frm.doc.payment_type == "Pay") {
			frm.set_query("pay_to_account", function (frm) {
				if (frm.party_type == "Supplier") {
					return {
						filters: {
							company: frm.company,
							name: `Creditors - ${frm.abbr}`,
						},
					};
				}
				if (frm.party_type == "Customer") {
					return {
						filters: {
							company: frm.company,
							name: `Debitors - ${frm.abbr}`,
						},
					};
				}
			});

			frm.set_query("pay_from_account", function (frm) {
				return {
					filters: {
						company: frm.company,
						root_type: 'Assest',
						'is_group':0
					}
				}
			});

		}
			if (frm.doc.payment_type == "Receive") {
				frm.set_query("pay_to_account", function (frm) {
					return {
						filters: {
							company: frm.company,
							root_type: 'Assest',
							'is_group':0
						}
					}
				});

				frm.set_query("pay_from_account", function (frm) {
					if (frm.party_type == "Supplier") {
						return {
							filters: {
								company: frm.company,
								name: `Creditors - ${frm.abbr}`,
							},
						};
					}
					if (frm.party_type == "Customer") {
						return {
							filters: {
								company: frm.company,
								name: `Debitors - ${frm.abbr}`,
							},
						};
					}
				});
			}
	},
});
