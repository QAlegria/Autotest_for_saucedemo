from time import sleep

import pytest
from pages.home_page import HomePage

def test_main_page_objects(checking_main_page):
    checking_main_page.open()
    checking_main_page.checking_the_main_page_logo()
    checking_main_page.checking_login_text_field()
    checking_main_page.checking_password_text_field()
    checking_main_page.checking_header_of_list_of_users()
    checking_main_page.checking_list_of_users()
    checking_main_page.checking_header_of_list_of_password()
    checking_main_page.checking_list_of_password()
    checking_main_page.checking_empty_error()


def test_main_page_empty_field_errors(checking_main_page, wrong_username):
    checking_main_page.open()
    checking_main_page.click_login_button()
    checking_main_page.checking_error_of_empty_username()
    checking_main_page.open()
    checking_main_page.enter_username(wrong_username)
    checking_main_page.click_login_button()
    checking_main_page.checking_error_of_empty_password()


def test_main_page_invalid_username(checking_main_page,wrong_username, valid_password):
    checking_main_page.open()
    checking_main_page.enter_username(wrong_username)
    checking_main_page.checking_username_is_written(wrong_username)
    checking_main_page.enter_password(valid_password)
    checking_main_page.checking_password_is_written(valid_password)
    checking_main_page.click_login_button()
    checking_main_page.checking_error_of_invalid_credentials()


def test_main_page_invalid_password(checking_main_page,standard_user, invalid_password):
    checking_main_page.open()
    checking_main_page.enter_username(standard_user)
    checking_main_page.checking_username_is_written(standard_user)
    checking_main_page.enter_password(invalid_password)
    checking_main_page.checking_password_is_written(invalid_password)
    checking_main_page.click_login_button()
    checking_main_page.checking_error_of_invalid_credentials()


def test_main_page_standard_user_login(checking_main_page,standard_user,valid_password):
    checking_main_page.open()
    checking_main_page.enter_username(standard_user)
    checking_main_page.enter_password(valid_password)
    checking_main_page.click_login_button()
    checking_main_page.checking_new_page_after_login()


