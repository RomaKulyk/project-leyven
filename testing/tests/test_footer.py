import pytest
from testing.pages.main_page import *
from testing.pages.footer import *
from testing.lib.constants import *
import time


def test_footer(chrome_browser: object):
    driver = chrome_browser
    main_page = MainPage(driver)

    # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    time.sleep(1)

    footer = Footer(driver)
    # 2.Find and click Facebook link
    footer.facebook_fl()
    assert footer.facebook_link.is_enabled()
    assert footer.facebook_link.is_displayed()
    footer.facebook_link.click()
    time.sleep(1)
    driver.back()

    # 3.Find and click Instagram link
    footer.instagram_fl()
    assert footer.instagram_link.is_enabled()
    assert footer.instagram_link.is_displayed()
    footer.instagram_link.click()
    time.sleep(1)
    driver.back()

    # 4.Find and click Tiktok link
    footer.tiktok_fl()
    assert footer.tiktok_link.is_enabled()
    assert footer.tiktok_link.is_displayed()
    footer.tiktok_link.click()
    time.sleep(1)
    driver.back()

    # 5.Find and click About Us link
    footer.about_us()
    assert footer.about_us_link.is_enabled()
    assert footer.about_us_link.is_displayed()
    footer.about_us_link.click()
    time.sleep(1)
    driver.back()

    # 6.Find and click Contacts link
    footer.contacts()
    assert footer.contacts_link.is_enabled()
    assert footer.contacts_link.is_displayed()
    footer.contacts_link.click()
    time.sleep(1)
    driver.back()

    # 7.Find and click Payment link
    footer.payment()
    assert footer.payment_link.is_enabled()
    assert footer.payment_link.is_displayed()
    footer.payment_link.click()
    time.sleep(1)
    driver.back()

    # 8.Find and click Public Oferta link
    footer.public_oferta()
    assert footer.public_oferta_link.is_enabled()
    assert footer.public_oferta_link.is_displayed()
    footer.public_oferta_link.click()
    time.sleep(1)
    driver.back()
    
    # 9.Find and click Privacy Policy link
    footer.privacy_policy()
    assert footer.privacy_policy_link.is_enabled()
    assert footer.privacy_policy_link.is_displayed()
    footer.privacy_policy_link.click()
    time.sleep(1)
    driver.back()

    # 10.Find and click Facebook button
    footer.facebook_fb()
    assert footer.facebook_fb_button.is_enabled()
    assert footer.facebook_fb_button.is_displayed()
    time.sleep(1)
    
    # 11.Find and click Instagram button
    footer.instagram_fb()
    assert footer.instagram_fb_button.is_enabled()
    assert footer.instagram_fb_button.is_displayed()
    time.sleep(1)
    
    # 12.Find and click Tiktok button
    footer.tiktok_fb()
    assert footer.tiktok_fb_button.is_enabled()
    assert footer.tiktok_fb_button.is_displayed()
    time.sleep(1)
    
    # 13.Find and click MAIN_LOGO button
    footer.main_logo_fb()
    assert footer.main_logo_button.is_enabled()
    assert footer.main_logo_button.is_displayed()
    time.sleep(1)
