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
		hospital: DF.Link | None
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
		if not self.assigned_room or not self.is_new():
			return
		room = frappe.get_doc("Room", self.assigned_room)
		if room.used_beds < room.number_of_beds:
			room.used_beds += 1
			room.save()
		else:
			frappe.throw("No available beds in the assigned room.")
      
    
    
    
    
    
	pass
