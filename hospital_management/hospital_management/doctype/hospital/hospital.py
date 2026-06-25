# Copyright (c) 2026, Elie and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Hospital(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from hospital_management.hospital_management.doctype.doctor_list.doctor_list import DoctorList
		from hospital_management.hospital_management.doctype.free_rooms.free_rooms import FreeRooms

		address: DF.SmallText | None
		doctors: DF.Table[DoctorList]
		free_rooms: DF.Table[FreeRooms]
		hospital_name: DF.Data
	# end: auto-generated types
	def validate(self):
		self.show_docs()
	def show_docs(self):
		patient = frappe.get_all("Patients",filters={"hospital": self.name},fields=["assigned_doctor", "full_name"])
		self.set("doctors",[])
		for patients in patient:
			self.append("doctors",{
				"doctor": patients.assigned_doctor,
				"assigned_to": patients.full_name
			})


@frappe.whitelist()
def get_free_rooms(hospital):
	rooms = frappe.get_all(
		"Room",
		filters={"hospital": hospital},
		fields=["name", "number_of_beds", "used_beds"]
	)
	result = []
	for room in rooms:
		free = room.number_of_beds - room.used_beds
		if free > 0:
			result.append({
				"room_no": room.name,
				"hospital": hospital,
				"free_beds": str(free)
			})
	return result