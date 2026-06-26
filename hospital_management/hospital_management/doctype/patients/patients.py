# Copyright (c) 2026, Elie and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Patients(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		age: DF.Data | None
		allergies_info: DF.SmallText | None
		assigned_doctor: DF.Link
		assigned_room: DF.Link
		date_of_birth: DF.Date
		fathers_name: DF.Data
		first_name: DF.Data
		full_name: DF.Data | None
		have_allergies: DF.Check
		hospital: DF.Link
		last_name: DF.Data
		mothers_name: DF.Data
		patients_health_problem: DF.SmallText | None
	# end: auto-generated types

	def validate(self):
		self.set_full_name()
		self.set_age()
		self.set_used()

	def set_full_name(self):
		self.full_name = self.first_name + " " + self.last_name

	def set_age(self):
		dob = frappe.utils.getdate(self.date_of_birth)
		today_date = frappe.utils.getdate(frappe.utils.today())
		years = today_date.year - dob.year
		if (today_date.month, today_date.day) < (dob.month, dob.day):
			years -= 1
		self.age = str(years)

	def set_used(self):
		if not self.assigned_room:
			return

		if self.is_new():
			room = frappe.get_doc("Room", self.assigned_room)
			if room.used_beds < room.number_of_beds:
				room.used_beds += 1
				room.save()
			else:
				frappe.throw("No available beds in the assigned room.")
		else:
			old_doc = self.get_doc_before_save()
			old_room = old_doc.assigned_room if old_doc else None

			if old_room != self.assigned_room:
				if old_room:
					old_room_doc = frappe.get_doc("Room", old_room)
					old_room_doc.used_beds = max(0, old_room_doc.used_beds - 1)
					old_room_doc.save()

				new_room_doc = frappe.get_doc("Room", self.assigned_room)
				if new_room_doc.used_beds < new_room_doc.number_of_beds:
					new_room_doc.used_beds += 1
					new_room_doc.save()
				else:
					frappe.throw("No available beds in the assigned room.")

	def on_trash(self):
		if self.assigned_room:
			room = frappe.get_doc("Room", self.assigned_room)
			room.used_beds = max(0, room.used_beds - 1)
			room.save()