
import frappe
from frappe import _
from frappe.desk.reportview import get_match_cond
import json
from datetime import datetime





@frappe.whitelist()
def load_data():
    """Loads Devices list in `__onload`"""
    #Get devices
    vdict = {}
    employee = frappe.db.sql("SELECT name,store,employee_name,company FROM `tabEmployee` ;", as_dict=1)
    storelist = frappe.db.sql("SELECT name FROM `tabStore` ;", as_list=1)
    shiftlist = frappe.db.sql("SELECT shift_name FROM `tabShift Time` ;", as_list=1)
    employeenamedata=frappe.db.sql("SELECT employee_name FROM `tabEmployee` ;", as_list=1)
    namewithspace=[]
    for i in range(0,len(employeenamedata)):
        a=' ' in str(employeenamedata[i])
        frappe.msgprint(employeenamedata[i])
        frappe.msgprint(str(a))
        w=str(employeenamedata[i]).replace(" ","");
        frappe.msgprint(str(w))
        


    # frappe.throw(lastweekdetails)
    # if lastweekdetails:
    #     for i in range(0,len(lastweekdetails)):
    #         a = lastweekdetails[i]["attendance_date"]
    #         b = str(a)
    #         lastweekdetails[i]["attendance_date"]=b
        # frappe.throw(str(lastweekdetails)

        
    
    
    #{'emp': [['test'], ['Pranali'], ['suvarna'], ['suresh']], 'store': [['andheri'], ['dadar'], ['ghatkopar']], 'shift': [['Morning'], ['night']]}
    vdict["emp"] = employee
    vdict["store"] = storelist
    vdict["shift"] = shiftlist
    #frappe.msgprint(str(len(vdict["emp"])))
    #frappe.msgprint(str(vdict["emp"][0]["employee_name"]));
    return vdict



