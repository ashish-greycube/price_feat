from distutils.log import debug
import frappe

@frappe.whitelist()
def fetch_latest_customer_price(doctype,item_code):
    if doctype=='Sales Invoice':
        return frappe.db.sql("""SELECT child_item.rate  from `tabSales Invoice` as main inner join `tabSales Invoice Item` as child_item 
                on main.name=child_item.parent where child_item.item_code = %s 
                and main.docstatus = 1  order by main.posting_date  Desc limit 1""",(item_code),as_dict=1)
    elif doctype=='Sales Order':
        return frappe.db.sql("""SELECT child_item.rate  from `tabSales Order` as main inner join `tabSales Order Item` as child_item 
                on main.name=child_item.parent where child_item.item_code = %s 
                and main.docstatus = 1  order by main.transaction_date  Desc limit 1""",(item_code),as_dict=1)
    elif doctype=='Quotation':
        return frappe.db.sql("""SELECT child_item.rate  from `tabQuotation` as main inner join `tabQuotation Item` as child_item 
                on main.name=child_item.parent where child_item.item_code = %s 
                and main.docstatus = 1  order by main.transaction_date  Desc limit 1""",(item_code),as_dict=1)                