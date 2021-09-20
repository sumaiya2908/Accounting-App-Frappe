# Copyright (c) 2013, summayya and contributors
# For license information, please see license.txt

import frappe
from frappe import _, _dict

def execute(filters=None):
	columns = get_columns()
	income_accounts = frappe.get_list("Account", pluck = "name", filters = {"root_type": "Income", "is_group": 0, "company": filters.company})
	expense_accounts = frappe.get_list("Account", pluck = "name", filters = {"root_type": "Expense", "is_group": 0, "company": filters.company})
	data, chart = get_pnl_data(income_accounts, expense_accounts, columns)
	print(chart)
	return columns, data, None, chart




def get_pnl_data(i_accounts, e_accounts, columns):
	# net_profit = 0
	i_accounts = tuple(i_accounts)
	income_accounts = ''.join(i_accounts)
	e_accounts = tuple(e_accounts)
	expense_accounts = ''.join(e_accounts)
	income = frappe.get_list("GL Entry", fields = ["account", "balance"], filters ={"account": income_accounts}, limit=1)
	expense = frappe.get_list("GL Entry", fields = ["account", "balance"], filters ={"account": expense_accounts})
	print(income)
	total_income = {
		'account': "Total Income",
		'balance': income[0]['balance'] if income else 0
	}
	total_expense = {
		'account': "Total Expense",
		'balance': expense[0]['balance'] if expense else 0
	}
	net_profit_loss = int(total_income['balance']) - int(total_expense['balance'])
	net_profit_or_loss = {
		'account': 'Net Profit' if net_profit_loss else 'Net Loss',
		'balance': net_profit_loss
	}

	chart = get_chart_data(net_profit_loss, total_income['balance'], total_expense['balance'], columns)
	

	return [net_profit_or_loss, total_income, total_expense], chart

def get_chart_data(net_pnl, income, expense, columns):
	data = []

	data.append({'name': 'Income', 'values': income})
	data.append({'name': 'Expense', 'values': expense})
	data.append({'name': 'Net Profit or Loss', 'values': net_pnl})
	chart = {
		"data": {
			'labels': ['Income', 'Expense', 'Net Profit or Loss'],
			'datasets': data
		}
	}

	chart["type"] = "bar"
	chart["fieldtype"] = "Currency"

	return chart

def get_columns():
	columns = [{
		"fieldname": "account",
		"label": _("Account"),
		"fieldtype": "Link",
		"options": "Account",
		"width": 300
	}, {
		"fieldname": "balance",
		"label": _("Balance"),
		"fieldtype": "data",
		"width": 300
	}]

	return columns

# def get_data(filters):
# 	company = filters.company
# 	data = frappe.db.sql(f"""SELECT account, balance from `tabGL Entry` where company = \'{company}\'""")
# 	return data

# def get_chart():
# 	chart = {
# 		"data": {
# 			'labels': ["2020-21"],
# 			"data": [22,45,67,456,23,46,23]

# 		}
# 	}

# 	chart["type"] = "bar"
# 	chart["fieldtype"] = "Currency"
