import pytest
from testing.pages.main_page import MainPage
from testing.pages.main_menu import MainMenu
from testing.pages.footer import Footer
from testing.lib.constants import MAIN_URL
import time


def test_footer(browser: object):
    driver = browser
    main_page = MainPage(driver)

    # 1.Open MAIN_URL page
    main_page.open_page(MAIN_URL)
    footer = Footer(driver)

    footer.find_footer_social_media_links()   
    for i in range(1,len(footer.footer_social_media_links_list) + 1):
        # 2.1.Find the social media link
        footer.find_footer_social_media_link(i)  

        assert footer.footer_social_media_link_n.is_enabled(), \
            f"Social media button {i} is not enabled."
        assert footer.footer_social_media_link_n.is_displayed(), \
            f"Social media button {i} is not displayed."
        
        # 2.2.Click the social media link
        footer.click_footer_social_media_link(i)
        print(f"Social media link {i} is clicked.")
        time.sleep(1)
        driver.back()
        
    footer.find_footer_about_us_links()
    for i in range(1,len(footer.footer_about_us_links_list) + 1):
        # 3.1.Find the About Us link
        footer.find_footer_about_us_link(i)  

        assert footer.footer_about_us_link_n.is_enabled(), \
            f"About us button {i} is not enabled."
        assert footer.footer_about_us_link_n.is_displayed(), \
            f"About us button {i} is not displayed."
        
        # 3.2.Click the About us link
        footer.click_footer_about_us_link(i)
        print(f"About Us link {i} is clicked.")
        footer.main_logo_fb()
        main_page.scroll_to_the_footer()
    
    # 4.Find and click Public Oferta link
    footer.public_oferta()
    assert footer.public_oferta_link.is_enabled()
    assert footer.public_oferta_link.is_displayed()
    footer.public_oferta_link.click()
    footer.main_logo_fb()
    main_page.scroll_to_the_footer()
    
    # 5.Find and click Privacy Policy link
    footer.privacy_policy()
    assert footer.privacy_policy_link.is_enabled()
    assert footer.privacy_policy_link.is_displayed()
    footer.privacy_policy_link.click()
    footer.main_logo_fb()
    main_page.scroll_to_the_footer()

    # 6.Find and click social media buttons
    footer.find_footer_social_media_buttons()
    # print(len(footer.footer_social_media_buttons_list))
    # print(footer.footer_social_media_buttons_list)

    for i in range((len(footer.footer_social_media_buttons_list) + 1) // 2):
        footer.click_footer_social_media_button(i + 1)
        assert footer.footer_social_media_button_n.is_enabled(), \
            f"Social media button {i} is not enabled."
        assert footer.footer_social_media_button_n.is_displayed(), \
            f"Social media button {i} is not displayed."
        time.sleep(1)

        # It goes to the social media page close it and returns back 
        # to the Main Page 
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[-1])
        time.sleep(1)
        driver.close()
        driver.switch_to.window(window_handles[0])
    
    # 9.Find and click MAIN_LOGO button
    footer.main_logo_fb()
    assert footer.main_logo_button.is_enabled()
    assert footer.main_logo_button.is_displayed()
    # assert 1 == 0

