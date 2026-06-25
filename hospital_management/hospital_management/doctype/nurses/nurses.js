// Copyright (c) 2026, Elie and contributors
// For license information, please see license.txt

frappe.ui.form.on("Nurse Room", {
    room(frm, cdt, cdn) {
        // filter applied when user clicks the room field
    }
});

frappe.ui.form.on("Nurses", {
    refresh(frm) {
        frm.set_query("room", "assigned_rooms", () => {
            return {
                filters: {
                    hospital: frm.doc.hospital
                }
            };
        });
    }
});