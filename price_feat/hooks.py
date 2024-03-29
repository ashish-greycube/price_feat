# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "price_feat"
app_title = "Price Feat"
app_publisher = "GreyCube Technologies"
app_description = "customization to get price based on last transaction"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "admin@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/price_feat/css/price_feat.css"
# app_include_js = "/assets/price_feat/js/price_feat.js"

# include js, css files in header of web template
# web_include_css = "/assets/price_feat/css/price_feat.css"
# web_include_js = "/assets/price_feat/js/price_feat.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Quotation" : "public/js/fetch_rates.js",
"Sales Order" : "public/js/fetch_rates.js",
"Sales Invoice" : "public/js/fetch_rates.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "price_feat.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "price_feat.install.before_install"
# after_install = "price_feat.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "price_feat.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"price_feat.tasks.all"
# 	],
# 	"daily": [
# 		"price_feat.tasks.daily"
# 	],
# 	"hourly": [
# 		"price_feat.tasks.hourly"
# 	],
# 	"weekly": [
# 		"price_feat.tasks.weekly"
# 	]
# 	"monthly": [
# 		"price_feat.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "price_feat.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"erpnext.stock.get_item_details.get_item_details": "price_feat.api.get_latest_price_for_get_item_details"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "price_feat.task.get_dashboard_data"
# }

