# MainPage
MAIN_URL = "https://www.leyven.com.ua/"
BUY_PRODUCTS = "//div[@class = 'mt-3 sm:mb-10']"
SHOW_ALL = "//button[@class = 'group mt-3 flex items-center gap-3 rounded-xl px-5 py-3 text-lg font-medium transition-all  duration-300 hover:bg-primary hover:text-white hover:shadow-xl max-sm:hidden sm:text-xl']"
HELP_ME = "//div[@class = 'group fixed bottom-2 right-2 z-[1] rounded-full bg-primary transition duration-200 hover:scale-105 sm:bottom-5 sm:right-5']"

# Help Me Form
HELP_ME_FORM = "//form[@class = 'modal-box mx-auto flex max-w-[800px] flex-col gap-5 bg-base-100 font-medium']"
ENTER_USERNAME = "//input[@id = 'name']"
ENTER_PHONE = "//input[@id = 'phone']"
ENTER_YOUR_QUESTION = "//input[@id = 'question']"
CLICK_SEND = "//button[@class = 'btn btn-primary btn-lg mx-auto mb-10 w-full max-w-sm text-white']"

# Main Menu
MAIN_LOGO = "//a[@class = 'btn btn-outline flex border-none']"
CATALOG = "//div[@class='dropdown dropdown-hover']"
CATALOG_DROPDOWN = "//div[@class='card dropdown-content card-compact z-[1] w-[1000px] bg-white p-2 text-slate-900 shadow-xl']"

# For Dynamic list definition
DROPDOWN_LIST_ITEMS = "//ul[@class = 'flex flex-col gap-5']/child::li"

# For Static list definition
UNSELECTED_DD_ITEM_CLS = 'false link flex items-center justify-between font-medium no-underline transition-all duration-300'
SELECTED_DD_ITEM_CLS = 'rounded-xl bg-primary p-3 text-white link flex items-center justify-between font-medium no-underline transition-all duration-300'
CATALOG_DROPDOWN_ITEM_1 = f"(//li[@class ='{UNSELECTED_DD_ITEM_CLS}' or @class = '{SELECTED_DD_ITEM_CLS}'])[1]"
CATALOG_DROPDOWN_ITEM_2 = f"(//li[@class ='{UNSELECTED_DD_ITEM_CLS}' or @class = '{SELECTED_DD_ITEM_CLS}'])[2]"
CATALOG_DROPDOWN_ITEM_3 = f"(//li[@class ='{UNSELECTED_DD_ITEM_CLS}' or @class = '{SELECTED_DD_ITEM_CLS}'])[3]"
CATALOG_DROPDOWN_ITEM_4 = f"(//li[@class ='{UNSELECTED_DD_ITEM_CLS}' or @class = '{SELECTED_DD_ITEM_CLS}'])[4]"
CATALOG_DROPDOWN_ITEM_5 = f"(//li[@class ='{UNSELECTED_DD_ITEM_CLS}' or @class = '{SELECTED_DD_ITEM_CLS}'])[5]"
CATALOG_DROPDOWN_ITEM_6 = f"(//li[@class ='{UNSELECTED_DD_ITEM_CLS}' or @class = '{SELECTED_DD_ITEM_CLS}'])[6]"
CATALOG_DROPDOWN_ITEM_7 = f"(//li[@class ='{UNSELECTED_DD_ITEM_CLS}' or @class = '{SELECTED_DD_ITEM_CLS}'])[7]"
CATALOG_DROPDOWN_ITEM_8 = f"(//li[@class ='{UNSELECTED_DD_ITEM_CLS}' or @class = '{SELECTED_DD_ITEM_CLS}'])[8]"
CATALOG_DROPDOWN_ITEM_9 = f"(//li[@class ='{UNSELECTED_DD_ITEM_CLS}' or @class = '{SELECTED_DD_ITEM_CLS}'])[9]"

SEARCH_FIELD = "//input[@class='text-sm outline-none xl:cursor-pointer 2xl:text-lg']"
CROSS_BUTTON = "//*[contains(@class,'lucide lucide-x ')]"
PHONE = "//div[@class = 'tooltip tooltip-bottom tooltip-info text-xl']"

FACEBOOK = "(//*[contains(@href,'www.facebook.com')])[1]"
INSTAGRAM = "(//*[contains(@href,'www.instagram.com')])[1]"
TIKTOK = "(//*[contains(@href,'www.tiktok.com')])[1]"
LOG_IN = "(//div[@class= 'hidden sm:flex'])[1]"
CART = "//div[contains(@class,'flex cursor-pointer items-center')]"

# Footer
FACEBOOK_FL = "Facebook"
INSTAGRAM_FL = "Instagram"
TIKTOK_FL = "Tiktok"
ABOUT_US = "//a[contains(@href,'/about')]"
CONTACTS = "//a[contains(@href,'/contacts')]"
PAYMENT = "//a[contains(@href,'/paymentAndShipping')]"
PUBLIC_OFERTA = "//a[contains(@href,'/publicOfferta')]"
PRIVACY_POLICY = "//a[contains(@href,'/privacyPolicy')]"
FACEBOOK_FB = "(//*[contains(@href,'www.facebook.com')])[3]"
INSTAGRAM_FB = "(//*[contains(@href,'www.instagram.com')])[3]"
TIKTOK_FB = "(//*[contains(@href,'www.tiktok.com')])[3]"
MAIN_LOGO_FL = "//a[@class = 'flex items-center gap-3']"

# Cart
CHECKOUT = "//button[@class = 'btn btn-primary btn-lg text-white']"
CONTINUE_SHOPPING = "//button[@class = 'btn btn-ghost text-primary']"
CLOSE_CART = "//button[contains(@class,'h-fit cursor-pointer rounded-lg')]"
REMOVE_PDP_1 = "(//div[contains(@class,'h-fit cursor-pointer')])[1]"

# Product cards
PRODUCT_CARDS = "//div[contains(@class,'md:grid-cols-3 xl:grid-cols-5')]/child::div"
# PRODUCT_CARDS = "((//div[@class = 'block w-full']/child::div)[2])/child::div"
PR_CARD = "(//div[@class = 'col-span-1'])"
PR_CARD_1 = "(//div[@class = 'col-span-1'])[1]"
PR_CARD_18 = "(//div[@class = 'col-span-1'])[18]"
PR_CARD_36 = "(//div[@class = 'col-span-1'])[36]"
PR_CARD_266 = "(//div[@class = 'col-span-1'])[266]"
TO_BUY_1 = "(//button[@class = 'btn bg-green-600 text-white hover:bg-green-500'])[1]"
TO_BUY_2 = "(//button[@class = 'btn bg-green-600 text-white hover:bg-green-500'])[2]"
