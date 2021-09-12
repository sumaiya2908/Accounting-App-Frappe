# Copyright (c) 2021, summayya and contributors
# For license information, please see license.txt

import frappe
from frappe.utils.nestedset import NestedSet

class Account(NestedSet):
	pass

@frappe.whitelist()
def get_accounts(doctype,
    parent='',
    is_root=False,
	company = None):
	accounts = frappe.get_list("Account", fields=["name as value", "is_group as expandable"], filters = {"company": company, 'parent_account': parent})
	print(accounts)
	return accounts
