// Copyright (c) 2026, Elie and contributors
// For license information, please see license.txt

frappe.ui.form.on("Nurses", {
    hospital(frm) {
        frm.set_query("room", "assigned_rooms", () => {
            return {
                filters: {
                    hospital: frm.doc.hospital
                }
            };
        });
    }
});