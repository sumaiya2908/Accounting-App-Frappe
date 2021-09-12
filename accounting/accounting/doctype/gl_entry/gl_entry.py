# Copyright (c) 2021, summayya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GLEntry(Document):
	def before_submit(self):
		self.balance = get_account_balance(self.account, self.company)



def create_gl_entry(object, voucher_type, pay_from_account, pay_to_account):
	frappe.get_doc({
        	"doctype": "GL Entry",
        	"posting_date": object.posting_date,
        	"company": object.company,
        	"account": pay_from_account,
        	"credit": object.amount,
        	"against_account": pay_to_account,
        	"voucher_type": voucher_type,
        	"voucher_no": object.name,
    		}).submit()

	frappe.get_doc({
        	"doctype": "GL Entry",
        	"posting_date": object.posting_date,
        	"company": object.company,
        	"account":pay_to_account,
        	"debit": object.amount,
        	"against_account": pay_from_account,
        	"voucher_type": voucher_type,
        	"voucher_no": object.name,
    		}).submit()

# @frappe.whitelist()
def get_account_balance(account, company):
	balance = 0
	entries = frappe.get_all("GL Entry", filters = {'account': account, 'company': company})
	for entry in entries:
		gl_entry = frappe.get_doc("GL Entry", entry)
		balance = balance - int(gl_entry.credit)
		balance = balance + int(gl_entry.debit)
	return balance

