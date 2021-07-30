

frappe.provide("frappe.treeview_settings")

frappe.treeview_settings["Accounts"] = {
	breadcrumbs: "Accounts",
	title: __("Charts of Accounts"),
	filters: [
		{
		  fieldname: "company",
		},
	  ],
	  onrender: function(node){
		  console.log(node)
	  }
}