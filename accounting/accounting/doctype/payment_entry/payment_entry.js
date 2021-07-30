// Copyright (c) 2021, summayya and contributors
// For license information, please see license.txt

frappe.ui.form.on("Payment Entry", {
	// returns the company's accounts in account field
	setup: function (frm) {
		frm.set_query("pay_to_account", function (frm) {
			return {
				filters: {
					company: frm.company,
				},
			};
		});
		frm.set_query("pay_from_account", function (frm) {
			return {
				filters: {
					company: frm.company,
				},
			};
		});
	},


	refresh(frm) {
		frm.trigger("payment_type");
		// frm.trigger("party_type")
	},
	payment_type(frm){
		let a = frappe.db.get_single_value('Company', 'abbrevation')
		// let abbr = frm.doc.company.split(" ").map((n)=>n[0]).join(" ");
		// if(frm.doc.payment_type == "Pay"){
		// 	frm.set_query("pay_to_account"), () => {
		// 		return{
		// 			filters: {
		// 				"account_name" : `Creditors-${frm.doc.company}`
		// 			}
		// 		}
		// 	}
		// }
		console.log(a)
	}


});




