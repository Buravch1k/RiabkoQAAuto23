import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database
from modules.ui.page_objects.sign_in_page import SignInPage


class User:
    def __init__(self):
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Oleksandr"
        self.second_name = "Riabko"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    api = GitHub()
    yield api


@pytest.fixture
def database():
    database = Database("/Users/apple/RiabkoQAAuto23/become_qa_auto.db")
    yield database


@pytest.fixture
def sign_in_page():
    page = SignInPage()
    yield page
