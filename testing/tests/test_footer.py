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
            f"Social media link {i} is not enabled."
        assert footer.footer_social_media_link_n.is_displayed(), \
            f"Social media link {i} is not displayed."
        
        # 2.2.Click the social media link
        link_text = footer.footer_social_media_links_list[i - 1].text
        footer.click_footer_social_media_link(i)
        print(f"Social media link '{link_text}' is  clicked.")
        time.sleep(1)
        driver.back()
        
    footer.find_footer_about_us_links()
    for i in range(1,len(footer.footer_about_us_links_list) + 1):
        # 3.1.Find the About Us link    
        footer.find_footer_about_us_link(i)  

        assert footer.footer_about_us_link_n.is_enabled(), \
            f"About us link {i} is not enabled."
        assert footer.footer_about_us_link_n.is_displayed(), \
            f"About us link {i} is not displayed."
        
        # 3.2.Click the About us link
        link_text = footer.footer_about_us_links_list[i - 1].text
        footer.click_footer_about_us_link(i)
        print(f"About Us link '{link_text}' is  clicked.")
        footer.main_logo_fb()
        main_page.scroll_to_the_footer()

    footer.find_footer_legal_links()
    for i in range(1,len(footer.footer_legal_links_list) + 1):
        # 4.1.Find the Legal link
        footer.find_footer_legal_link(i)  

        assert footer.footer_legal_link_n.is_enabled(), \
            f"Legal link {i} is not enabled."
        assert footer.footer_about_us_link_n.is_displayed(), \
            f"Legal link {i} is not displayed."
        
        # 4.2.Click the Legal link
        link_text = footer.footer_legal_links_list[i - 1].text
        footer.click_footer_legal_link(i)
        print(f"Legal link '{link_text}' is  clicked.")
        footer.main_logo_fb()
        main_page.scroll_to_the_footer()

    
    footer.find_footer_social_media_buttons()
    for i in range((len(footer.footer_social_media_buttons_list) + 1) // 2):
        # 5.1.Find Social Media buttons
        footer.find_footer_social_media_button(i + 1)
        assert footer.footer_social_media_button_n.is_enabled(), \
            f"Social media button {i + 1} is not enabled."
        assert footer.footer_social_media_button_n.is_displayed(), \
            f"Social media button {i + 1} is not displayed."
        time.sleep(1)
        # 5.2.Click Social Media buttons
        footer.click_footer_social_media_button(i + 1)
        print(f"Social media button '{i + 1}' is  clicked.")
        
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

    assert 1 == 0  # This line is to ensure that the test fails if it reaches 
    # this point, which is useful for debugging purposes. Remove or comment out
    # this line in production code.


