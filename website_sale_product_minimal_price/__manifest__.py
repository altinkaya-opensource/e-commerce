# Copyright 2019 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Website Sale Product Minimal Price",
    "summary": "Display minimal price for products that has variants",
    "version": "16.0.1.0.0",
    "development_status": "Production/Stable",
    "maintainers": ["sergio-teruel"],
    "category": "Website",
    "website": "https://github.com/OCA/e-commerce",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["website_sale"],
    "data": ["views/templates.xml"],
    "assets": {
        "web.assets_frontend": [
            "/web/static/src/legacy/js/fields/field_utils.js",
            "/website_sale_product_minimal_price/static/src/xml/*.xml",
            "/website_sale_product_minimal_price/static/src/js/*.js",
        ],
        "web.assets_tests": [
            "/website_sale_product_minimal_price/static/src/js/tours/*.js"
        ],
    },
}
