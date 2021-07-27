# Copyright (c) 2021, summayya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


default_accounts = {

    "Application of Funds": ["Debtors",
                             "Bank Account",
                             "Cash",
                             "Stock In Hand"],


    "Source of Funds":
        ["Creditors"],


    "Expense":
        ["Direct Expense"],



    "Income":
        ["Income Account"]
}

root_type = {"Application of Funds": "Assest", "Source of Funds" : "Liability", "Expense" : "Expense", "Income" : "Income" }

class Company(Document):


    def create_accounts(self):
        for account in default_accounts:
            root_account = frappe.get_doc({
                "doctype": "Accounts",
                "account_name": account + " - " + self.abbrevation,
                "is_group": 1,
                "root_type": root_type[account],
                "company": self.company_name
            })
            root_account.insert()
            for child in default_accounts[account]:
                chile_account = frappe.get_doc({
                    "doctype": "Accounts",
                    "account_name": child + " - " + self.abbrevation,
                    "parent_accounts": root_account.account_name,
                    "company": self.company_name,
                    "is_group": 0,
                    "root_type": root_type[account]
                })
                chile_account.insert()

    def before_save(self):
        abbrevation = "".join(
            e[0] for e in self.company_name.split()).capitalize()
        abbr_exist = frappe.db.exists({
            "doctype" : "Company",
            "abbrevation" : abbrevation
        })

        if(abbr_exist):
            frappe.throw("Abbrevation already used ! ")

        else:
            self.abbrevation = abbrevation


    def on_update(self):
        self.create_accounts()
