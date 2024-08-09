# -*- coding: utf-8 -*-
################################################################################
#
#    Venture Technologies, LLC.
#
#    Copyright (C) 2024-TODAY Venture Technologies, LLC.(<https://www.venturetech.site>).
#    Author: Jose Artavia (jartavia@venturetech.site)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
{
    "name": "Open EMR Odoo 17",
    "version": "17.0.1.0.0",
    "category": "Services",
    "summary": """This Module Helps to Manage Patients Records, Doctors Details,
     Lab Management , Employee Management etc.""",
    "description": """The hospital management module can be used to handle 
     the day-to-day activities of the hospital. Managing patient scheduling, 
     making patient ID cards, creating patient lab test results, and adding 
     doctors, patients, prescriptions, vaccines, etc. are all made easier 
     with the help of this module. This app offers a different dashboards for 
     different users.""",
    "author": "Venture Technologies",
    "company": "Venture Technologies",
    "maintainer": "Venture Technologies",
    "website": "https://www.venturetech.site",
    "depends": ["website", "hr", "stock", "sale_management"],
    "data": [
        "security/base_openemr_groups.xml",
        "security/doctor_allocation_security.xml",
        "security/doctor_slot_security.xml",
        "security/patient_lab_test_security.xml",
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        "data/ir_cron_data.xml",
        "data/website_data.xml",
        "views/menu_views.xml",
        "views/inpatient_surgery_views.xml",
        "views/hospital_bed_views.xml",
        "views/blood_bank_views.xml",
        "views/contra_indication_views.xml",
        "views/booking_success_templates.xml",
        "views/hospital_building_views.xml",
        "views/hospital_degree_views.xml",
        "views/doctor_allocation_views.xml",
        "views/hr_employee_views.xml",
        "views/hospital_inpatient_views.xml",
        "views/hospital_insurance_views.xml",
        "views/hospital_laboratory_views.xml",
        "views/patient_lab_test_views.xml",
        "views/lab_test_views.xml",
        "views/lab_test_result_views.xml",
        "views/medicine_brand_views.xml",
        "views/menu_views.xml",
        "views/hospital_outpatient_views.xml",
        "views/res_partner_views.xml",
        "views/patient_portal_templates.xml",
        "views/hospital_vaccination_views.xml",
        "views/product_template_views.xml",
        "views/room_facility_views.xml",
        "views/patient_card_templates.xml",
        "views/booking_success_templates.xml",
        "views/doctor_specialization_views.xml",
        "views/hospital_pharmacy_views.xml",
        "views/hospital_ward_views.xml",
        "views/patient_booking_templates.xml",
        "views/patient_room_views.xml",
        "views/lab_test_line_views.xml",
        "report/res_partner_reports.xml",
        "report/lab_test_line_reports.xml",
    ],
    "demo": ["demo/hr_job_demo.xml"],
    "assets": {
        "web.assets_frontend": [
            "base_openemr/static/src/js/prescription.js",
            "base_openemr/static/src/js/website_page.js",
        ],
        "web.assets_backend": [
            "base_openemr/static/src/css/doctor_dashboard.css",
            "base_openemr/static/src/css/reception_dashboard.css",
            "base_openemr/static/src/css/lab_dashboard.css",
            "base_openemr/static/src/css/pharmacy_dashboard.css",
            "base_openemr/static/src/xml/lab_dashboard_templates.xml",
            "base_openemr/static/src/xml/doctor_dashboard_templates.xml",
            "base_openemr/static/src/js/lab_dashboard.js",
            "base_openemr/static/src/js/doctor_dashboard.js",
            "base_openemr/static/src/xml/pharmacy_orderlines.xml",
            "base_openemr/static/src/js/pharmacy_orderlines.js",
            "base_openemr/static/src/xml/pharmacy_dashboard_templates.xml",
            "base_openemr/static/src/js/pharmacy_dashboard.js",
            "base_openemr/static/src/xml/reception_dashboard_templates.xml",
            "base_openemr/static/src/js/reception_dashboard.js",
        ],
    },
    "external_dependencies": {"python": ["python-barcode"]},
    "images": ["static/description/banner.jpg"],
    "license": "AGPL-3",
    "installable": True,
    "auto_install": False,
    "application": True,
}