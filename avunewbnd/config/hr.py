from frappe import _

def get_data():
	return [
{
			"label": _("Reports"),
			"icon": "fa fa-list",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Attendance Sheet",
					"doctype": "Attendance"
				},
				
			]
		}
]
