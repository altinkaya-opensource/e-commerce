# Copyright 2020 Tecnativa - Ernesto Tejeda
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from datetime import datetime, timedelta

from odoo.tests.common import Form, HttpCase, tagged


@tagged("post_install", "-at_install")
class WebsiteSaleStockProvisioningDate(HttpCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        product = cls.env["product.product"].create(
            {
                "name": "product test - provisioning date",
                "type": "product",
                "website_published": True,
                "show_next_provisioning_date": True,
            }
        )
        incoming_picking_type = cls.env["stock.picking.type"].search(
            [
                ("code", "=", "incoming"),
                "|",
                ("warehouse_id.company_id", "=", cls.env.user.company_id.id),
                ("warehouse_id", "=", False),
            ],
            limit=1,
        )
        picking_form = Form(
            recordp=cls.env["stock.picking"].with_context(
                default_picking_type_id=incoming_picking_type.id
            ),
            view="stock.view_picking_form",
        )
        with picking_form.move_ids_without_package.new() as move:
            move.product_id = product
            move.product_uom_qty = 10
        picking = picking_form.save()
        picking_form = Form(picking)
        picking_form.scheduled_date = datetime.now() + timedelta(days=2)
        picking = picking_form.save()
        picking.action_confirm()

    def test_ui_website(self):
        """Test frontend tour."""
        self.start_tour(
            "/shop",
            "website_sale_stock_provisioning_date",
            login="admin",
        )
