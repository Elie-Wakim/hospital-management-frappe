// Copyright (c) 2026, Elie and contributors
// For license information, please see license.txt

frappe.ui.form.on("Patients", {
    hospital(frm) {
        frm.set_query("assigned_room", () => ({
            filters: { hospital: frm.doc.hospital }
        }));
    }
});

