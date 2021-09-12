# Copyright (c) 2021, summayya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


default_accounts = {

    "Application of Funds": ["Debitors",
                             "Bank Account",
                             "Cash",
                             "Stock In Hand"],


    "Source of Funds":
        ["Creditors", "Stock Liablities"],


    "Expense":
        ["Direct Expense"],



    "Income":
        ["Sales"]
}

root_type = {"Application of Funds": "Assest", "Source of Funds" : "Liability", "Expense" : "Expense", "Income" : "Income" }

class Company(Document):


    def create_accounts(self):
        for account in default_accounts:
            root_account = frappe.get_doc({
                "doctype": "Account",
                "account_name": account + " - " + self.abbrevation,
                "is_group": 1,
                "root_type": root_type[account],
                "company": self.company_name,

            })
            root_account.insert()
            for child in default_accounts[account]:
                chile_account = frappe.get_doc({
                    "doctype": "Account",
                    "account_name": child + " - " + self.abbrevation,
                    "parent_account": root_account.account_name,
                    "company": self.company_name,
                    "is_group": 0,
                    "root_type": root_type[account],
                    "company": self.company_name,
                })
                chile_account.insert()

    def before_save(self):
        abbr_exist = frappe.db.exists({
            "doctype" : "Company",
            "abbrevation" : self.abbrevation
        })
        if(abbr_exist):
            frappe.throw("Abbrevation already used ! ")

    def after_insert(self):
        self.create_accounts()


@frappe.whitelist()
def default_company():
	return frappe.db.sql('select name from tabCompany limit 1')