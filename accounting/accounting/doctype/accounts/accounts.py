# Copyright (c) 2021, summayya and contributors
# For license information, please see license.txt

# import frappe
from frappe.utils.nestedset import NestedSet

class Accounts(NestedSet):
	pass


	def before_save(self):
		
		if(self.root_type == 'Liability' or self.root_type == 'Equity' or self.root_type == 'Income' ):
			self.balance_type = 'Debit'
		else:
			self.balance_type = 'Credit'