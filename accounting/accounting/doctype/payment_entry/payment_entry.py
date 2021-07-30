# Copyright (c) 2021, summayya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PaymentEntry(Document):
    pass

    def create_gl_entry(self):
            gl_entry = frappe.get_doc({
                "doctype": "GL Entry",
                "posting_date": self.posting_date,
                "company": self.company,
                "account": self.pay_from_account,
                "credit": self.amount,
                "against_account": self.pay_to_account,
                "voucher_type": "Payment Entry",
                "voucher_no": self.name

            })
            gl_entry.insert()
            gl_entry = frappe.get_doc({
                "doctype": "GL Entry",
                "posting_date": self.posting_date,
                "company": self.company,
                "account": self.pay_to_account,
                "debit": self.amount,
                "against_account": self.pay_from_account,
                "voucher_type": "Payment Entry",
                "voucher_no": self.name
            })
            gl_entry.insert()


    def on_submit(self):
        self.create_gl_entry()
