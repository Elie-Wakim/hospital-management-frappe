// Copyright (c) 2026, Elie and contributors
// For license information, please see license.txt

function load_free_rooms(frm) {
    if (!frm.doc.name) return;

    frappe.call({
        method: "hospital_management.hospital_management.doctype.hospital.hospital.get_free_rooms",
        args: { hospital: frm.doc.name },
        callback(r) {
            if (!r.message) return;
            frm.clear_table("free_rooms");
            r.message.forEach(row => {
                let child = frm.add_child("free_rooms");
                child.room_no = row.room_no;
                child.hospital = row.hospital;
                child.free_beds = row.free_beds;
            });
            frm.refresh_field("free_rooms");
        }
    });
}

frappe.ui.form.on("Hospital", {
    refresh(frm) {
        load_free_rooms(frm);
    }
});