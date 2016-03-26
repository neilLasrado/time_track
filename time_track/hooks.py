# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "time_track"
app_title = "Time Track"
app_publisher = "Neil Lasrado"
app_description = "track the time you work"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "nlasrado@gmail.com"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/time_track/css/time_track.css"
# app_include_js = "/assets/time_track/js/time_track.js"

# include js, css files in header of web template
# web_include_css = "/assets/time_track/css/time_track.css"
# web_include_js = "/assets/time_track/js/time_track.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "time_track.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "time_track.install.before_install"
# after_install = "time_track.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "time_track.notifications.get_notification_config"

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
# 		"time_track.tasks.all"
# 	],
# 	"daily": [
# 		"time_track.tasks.daily"
# 	],
# 	"hourly": [
# 		"time_track.tasks.hourly"
# 	],
# 	"weekly": [
# 		"time_track.tasks.weekly"
# 	]
# 	"monthly": [
# 		"time_track.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "time_track.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "time_track.event.get_events"
# }

