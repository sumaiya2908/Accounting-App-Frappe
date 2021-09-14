// Copyright (c) 2016, summayya and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["General Legder"] = {
	"filters": [
		{
			"label": ("Company"),
            "fieldname": "company",
            "fieldtype": "Link",
			"default": frappe.defaults.get_user_default("Company"),
            "options": "Company",
		},
		{
			"label": ("Account"),
            "fieldname": "account",
            "fieldtype": "Link",
            "options": "Account",
			get_data: function(text) {
				console.log(text)
				return frappe.db.get_link_options('Account', text, {
				company: frappe.query_report.get_filter_value("company")})	}
		},
		{
			"label": ("Posting Date"),
			"fieldname": "posting_date",
			"fieldtype": "Date",
		},
	]
};
