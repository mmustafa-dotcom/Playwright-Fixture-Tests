import pytest

from playwright.sync_api import Page, expect


BASE_URL = "https://www.saucedemo.com/"
INVENTORY_URL = "https://www.saucedemo.com/inventory.html"


@pytest.fixture
def login(page: Page):

    def _login(username):
        page.goto(BASE_URL)
        page.get_by_role("textbox", name="Username").fill(username)
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("button", name="Login").click()

        return page

    yield _login


class TestLogin:

    def test_login1(self, login, page: Page):

        login("standard_user")

        expect(page).to_have_url(INVENTORY_URL)


    def test_login2(self, login, page: Page):

        login("problem_user")

        expect(page).to_have_url(INVENTORY_URL)


    def test_login3(self, login, page: Page):

        login("locked_out_user")

        expect(page).to_have_url(BASE_URL)

        expect(page.locator('[data-test="error"]')).to_be_visible()


    def test_login4(self, login, page: Page):

        login("performance_glitch_user")

        expect(page).to_have_url(INVENTORY_URL)


    def test_login5(self, login, page: Page):

        login("error_user")

        expect(page).to_have_url(INVENTORY_URL)


    def test_login6(self, login, page: Page):

        login("visual_user")

        expect(page).to_have_url(INVENTORY_URL)