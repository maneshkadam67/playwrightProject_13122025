from playwright.sync_api import Playwright, expect, Page
from playwright.sync_api import sync_playwright,expect


# def test_basics(playwright:Playwright):
#     browser=playwright.chromium.launch(headless=False)
#     context1=browser.new_context()
#     context2 = browser.new_context()
#     page1=context1.new_page()
#     page2 = context2.new_page()
#
#     page1.goto("https://demo.nopcommerce.com/login?returnurl=%2Fsearch%3Fq%3Dmobile")
#     page2.goto("https://demowebshop.tricentis.com/")
#     page2.wait_for_timeout(8000)
#     page2.evaluate("window.scrollBy(0, 500)")
#     page2.wait_for_timeout(2000)
#     context2.close()
#     page2.close()
#     page1.wait_for_timeout(3000)
#     page1.evaluate("window.scrollBy(0, 500)")
#     page1.wait_for_timeout(3000)
#     context1.close()
#     page1.close()

# def test_basic(page:Page):
#     def test_basics(playwright: Playwright):
#         page.goto("https://demo.nopcommerce.com/login?returnurl=%2Fsearch%3Fq%3Dmobile")
#         page.wait_for_timeout(3000)
#         page.evaluate("window.scrollBy(0, 500)")
#         page.wait_for_timeout(3000)
#         page.close()

# def test_select_options(page:Page):
#     page.goto("https://rahulshettyacademy.com/loginpagePractise/")
#     page.locator("select.form-control").select_option(index=2)
#     page.wait_for_timeout(3000)
#     page.go_back()
#     page.wait_for_timeout(4000)
#     page.go_forward()
#     page.wait_for_timeout(3000)
#     page.close()

# def test_select_options(page:Page):
#     page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
#     page.get_by_role("button",name="Point Me").hover()
#     page.wait_for_timeout(4000)
#     page.mouse.move(100,200)
#     page.mouse.click(100,200)
#     page.wait_for_timeout(4000)
#     page.close()

# def test_select_options(page:Page):
#     page.goto("https://testautomationpractice.blogspot.com/")
#     page.locator("#singleFileInput").set_input_files("output_data.xlsx")
#     page.wait_for_timeout(4000)
#     page.get_by_role("button",name="Upload Single File").click()
#     page.wait_for_timeout(2000)
#     expect(page.locator("#singleFileStatus")).to_be_visible()
#     page.close()

# def test_select_options(page:Page):
#     page.goto("https://testautomationpractice.blogspot.com/")
#     page.locator("#singleFileInput").set_input_files("output_data.xlsx")
#     page.wait_for_timeout(4000)
#     page.get_by_role("button",name="Upload Single File").click()
#     page.wait_for_timeout(2000)
#     expect(page.locator("#singleFileStatus")).to_be_visible()
#     page.close()

# def test_select_options(page:Page):
#     page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")
#     with page.expect_download() as pd:
#         page.locator('button[onclick="generatePDFFile()"]').click()
#     file = pd.value
#     file.save_as("myfile.pdf")
#     page.close()

def test_select_options(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/#")
    with page.expect_popup() as p:
        page.locator("body > a").click()
        new_page=p.value
        expect(new_page.locator('ul[class="clearfix"] li')).to_have_text("contact@rahulshettyacademy.com")
    page.on("")
    page.close()

