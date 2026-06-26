# Copyright (c) 2026, Elie and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class InvoiceItems(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		currency: DF.Link | None
		item: DF.Data
		value: DF.Currency
	# end: auto-generated types
	pass
