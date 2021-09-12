# Copyright (c) 2021, summayya and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from ..gl_entry.gl_entry import create_gl_entry


class SalesInvoice(Document):

    def on_submit(self):
    	create_gl_entry(self, 'Sales Invoice', self.debit_account, self.credit_account)
