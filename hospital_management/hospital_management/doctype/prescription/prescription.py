# Copyright (c) 2026, Elie and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Prescription(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		date: DF.Date
		doctor: DF.Link
		patient: DF.Link
		prescription: DF.SmallText
	# end: auto-generated types
	def validate(self):
		self.set_date()
	def set_date(self):
		self.date = frappe.utils.getdate(frappe.utils.today())
	pass
