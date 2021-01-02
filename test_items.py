def test_guest_should_see_login_link(browser):
    browser.get(' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    browser.find_element_by_css_selector("button.btn:nth-child(3)")
