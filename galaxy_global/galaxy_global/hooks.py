from . import __version__ as app_version

app_name = "galaxy_global"
app_title = "Galaxy Global"
app_publisher = "Galaxy DevOps Team"
app_description = "Galaxy Global Group - Corporate ERP Layer"
app_email = "devops@galaxynp.holdings"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/galaxy_global/css/galaxy_global.css"
# app_include_js = "/assets/galaxy_global/js/galaxy_global.js"

# include js, css files in header of web template
# web_include_css = "/assets/galaxy_global/css/galaxy_global.css"
# web_include_js = "/assets/galaxy_global/js/galaxy_global.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "galaxy_global/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "galaxy_global.utils.jinja_methods",
#	"filters": "galaxy_global.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "galaxy_global.install.before_install"
# after_install = "galaxy_global.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "galaxy_global.uninstall.before_uninstall"
# after_uninstall = "galaxy_global.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "galaxy_global.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"galaxy_global.tasks.all"
#	],
#	"daily": [
#		"galaxy_global.tasks.daily"
#	],
#	"hourly": [
#		"galaxy_global.tasks.hourly"
#	],
#	"weekly": [
#		"galaxy_global.tasks.weekly"
#	],
#	"monthly": [
#		"galaxy_global.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "galaxy_global.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "galaxy_global.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "galaxy_global.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"galaxy_global.auth.validate"
# ]

# Fixtures
# --------
# Export following doctypes to fixtures

fixtures = [
    {
        "dt": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
                    # Add custom field names here when created
                ]
            ]
        ]
    }
]
