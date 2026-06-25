# Copyright (c) 2026, Elie and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Room(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		hospital: DF.Link
		number_of_beds: DF.Int
		room_name: DF.Data
		used_beds: DF.Int
	# end: auto-generated types
	pass
