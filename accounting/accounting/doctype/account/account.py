# Copyright (c) 2021, summayya and contributors
# For license information, please see license.txt

import frappe
from frappe.utils.nestedset import NestedSet


class Account(NestedSet):
    pass


@frappe.whitelist()
def get_accounts(doctype,
                 parent=None,
                 is_root=False,
                 company=frappe.defaults.get_user_default("Company"),
                 ):

    filters = []

    if parent and not is_root:
        filters.append(["parent_account", "=", parent])
    else:
        filters.append(['ifnull(`parent_account`, "")', "=", ""])

    if company:
        filters.append(["company", "=", company])

    accounts = frappe.get_list(
        doctype,
        fields=["name as value", "is_group as expandable"],
        filters=filters,
        order_by="name",
    )

    return accounts
