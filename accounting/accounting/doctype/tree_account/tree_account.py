# Copyright (c) 2021, summayya and contributors
# For license information, please see license.txt

import frappe
from frappe.utils.nestedset import NestedSet

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


class treeaccount(NestedSet):


    def create_accounts(self, accounts):
            for i in accounts:
                root_account = frappe.get_doc({
                    "doctype": "tree account",
                    "acount_name": i,
                    "Is group": 1,
                })
                root_account.insert()
            
            for i in accounts:
                for f in accounts[i]:
                    chile_account = frappe.get_doc({
                        "doctype": "tree account",
                        "acount_name": f,
                        "Parent tree account": i
                    })
                    chile_account.insert()
                

                    


    def on_update(self):
        self.create_accounts(default_accounts)
