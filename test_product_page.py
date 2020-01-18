from .pages.product_page import ProductPage

def add_in_basket_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_in_basket_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()