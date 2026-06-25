# Copyright (c) 2026, Elie and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class PatientReason(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		is_emergency: DF.Check
		medical_reason: DF.TextEditor | None
		patient: DF.Link | None
	# end: auto-generated types
	pass
