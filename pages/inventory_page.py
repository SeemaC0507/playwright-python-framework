class InventoryPage:
    def __init__(self,page):
        self.page = page

    def get_product_count(self):
        return self.page.locator(".inventory_item").count()

    def get_product_names(self):
        return self.page.locator(".inventory_item_name").all_text_contents()


    def add_first_product_to_cart(self):
        self.page.locator("button.btn_primary").first.click()

