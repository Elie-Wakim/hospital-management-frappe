# Copyright (c) 2026, Elie and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Doctor(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		first_name: DF.Data
		full_name: DF.Data | None
		hospital: DF.Link
		last_name: DF.Data
		name: DF.Int | None
		profession: DF.Data
	# end: auto-generated types
	def validate(self):
		self.set_full_name()     
     
	def set_full_name(self):
		self.full_name = self.first_name + " " + self.last_name
	pass
