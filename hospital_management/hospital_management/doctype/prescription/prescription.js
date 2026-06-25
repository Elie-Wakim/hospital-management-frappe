// Copyright (c) 2026, Elie and contributors
// For license information, please see license.txt

frappe.ui.form.on("Prescription", {
	refresh(frm) {
		// refresh logic here
	},
	onload(frm) {
    if (frm.is_new()) {
        frm.set_value("date", frappe.datetime.get_today());
    }
}
});
