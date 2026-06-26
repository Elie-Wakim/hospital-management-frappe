# Copyright (c) 2026, Elie and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class MedicalInvoice(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from hospital_management.hospital_management.doctype.list_of_items.list_of_items import ListOfItems

		amended_from: DF.Link | None
		currency: DF.Link | None
		doctor: DF.Link
		hospital: DF.Link | None
		item_link: DF.Link | None
		items: DF.Table[ListOfItems]
		patient: DF.Link
		total_amount: DF.Currency
	# end: auto-generated types
	def validate(self):
		self.get_total()
	def get_total(self):
		self.total_amount =0
		for items in self.items:
			self.total_amount += items.value
	pass
