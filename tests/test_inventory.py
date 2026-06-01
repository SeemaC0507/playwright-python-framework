from pages.inventory_page import InventoryPage

def test_count(logged_in_page):
    inventory_count = InventoryPage(logged_in_page)
    count = inventory_count.get_product_count()
    assert count == 6

def test_product_name(logged_in_page):
    product_name = InventoryPage(logged_in_page)
    name = product_name.get_product_names()
    assert len(name) == 6
    assert name[0] == "Sauce Labs Backpack"     

def test_product_cart(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_first_product_to_cart()
    cart_count = logged_in_page.locator(".shopping_cart_badge").text_content()
    assert cart_count == "1"    