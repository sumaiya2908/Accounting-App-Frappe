# Copyright (c) 2021, summayya and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Company(Document):
	pass

	def before_save(self):
		self.abbrevation =  "".join(e[0] for e in self.company_name.split()).capitalize()
		
