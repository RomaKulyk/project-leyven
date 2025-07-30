# MainPage
MAIN_URL = "https://www.leyven.com.ua/"
SHOW_ALL = "//button[@class = 'group mt-3 flex items-center gap-3 rounded-xl px-5 py-3 text-lg font-medium transition-all  duration-300 hover:bg-primary hover:text-white hover:shadow-xl max-sm:hidden sm:text-xl']"
GO_TO_CATEGORY = "(//div[@class ='font-[500] flex items-center gap-[6px] xl:text-[16px]'])"
HELP_ME = "//div[@class = 'fixed bottom-2 right-2 z-[1] transition duration-200 sm:bottom-5 sm:right-5']"

CATS = "(//a[contains(@class,'w-40 overflow-hidden rounded-3xl')])[1]"
DOGS ="(//a[contains(@class,'w-40 overflow-hidden rounded-3xl')])[2]"
CATTLE ="//a[contains(@class,'h-28 w-full overflow-hidden rounded-3xl')]"
OTHERS = "//div[contains(@class,'relative h-28 overflow-hidden rounded-3xl')]"

CATEGORIES = "//div[@class = 'flex flex-1 flex-col justify-between space-y-5']"
FEEDING = "(//a[contains(@class,'flex w-full gap-3 rounded-full bg-white')])[1]"
HEALTH = "(//a[contains(@class,'flex w-full gap-3 rounded-full bg-white')])[2]"
TOYS = "(//a[contains(@class,'flex w-full gap-3 rounded-full bg-white')])[3]"
AMMUNITION = "(//a[contains(@class,'flex w-full gap-3 rounded-full bg-white')])[4]"
CAROUSEL_ITEM = "//div[contains(@class,'relative h-[250px] w-full')]"
CAROUSEL_ITEMS = "//div[contains(@class,'relative h-[250px] w-full')]/child::a/img"

PRODUCT_CATEGORIES = "//ul[contains(@class,'mx-auto mt-2 hidden items-center')]/child::li"
PRODUCT_CATEGORY = "//ul[contains(@class,'mx-auto mt-2 hidden items-center')]/child::li"

MAIN_PRODUCTS_CATEGORIES = "//div[@class='flex flex-1 flex-col justify-between space-y-5']/child::a"

# Help Me Form
HELP_ME_FORM = "//form[@class = 'modal-box mx-auto flex max-w-[800px] flex-col gap-5 overflow-hidden rounded-[50px] bg-white font-medium xl:p-10']"
ENTER_USERNAME = "//input[@id = 'name']"
ENTER_PHONE = "//input[@id = 'phone']"
ENTER_YOUR_QUESTION = "//input[@id = 'question']"
CLICK_SEND = "//button[@class = 'btn btn-primary btn-lg mx-auto mb-10 w-full max-w-sm text-white']"

# Main Menu
MAIN_LOGO = "(//img[@alt='Лейвен логотип'])[2]"
CATALOG = "//div[@class='dropdown dropdown-hover']"
CATALOG_DROPDOWN = "//div[@class='dropdown-content z-20 w-[1000px] rounded-xl border bg-base-100 shadow-2xl']"
LANGUAGE_BUTTON = "(//button[contains(@class,'flex h-9 items-center justify-between')])[1]"
SOCIAL_MEDIA_BUTTONS_LIST_ITEMS = "//div[@class='flex items-center gap-5 xl:scale-90 2xl:scale-100']/child::a"
SIGN_IN_BUTTON = "//button[contains(@class,'w-full rounded-md bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-500')]"

# For Dynamic list definition
DROPDOWN_LIST_ITEMS = "//ul[@class = 'flex flex-col gap-2']/child::li"

# For Static list definition
UNSELECTED_DD_ITEM_CLS = 'hover:bg-primary/5 block rounded-lg p-3 text-sm transition-all duration-200 text-base-content'
SELECTED_DD_ITEM_CLS = 'hover:bg-primary/5 block rounded-lg p-3 text-sm transition-all duration-200 bg-primary/5 font-medium text-secondary'
CATALOG_DROPDOWN_ITEM_1 = f"(//li/a[@class ='{UNSELECTED_DD_ITEM_CLS}' or @class = '{SELECTED_DD_ITEM_CLS}'])[1]"
CATALOG_DROPDOWN_ITEM_2 = f"(//li/a[@class ='{UNSELECTED_DD_ITEM_CLS}' or @class = '{SELECTED_DD_ITEM_CLS}'])[2]"
CATALOG_DROPDOWN_ITEM_3 = f"(//li/a[@class ='{UNSELECTED_DD_ITEM_CLS}' or @class = '{SELECTED_DD_ITEM_CLS}'])[3]"
CATALOG_DROPDOWN_ITEM_4 = f"(//li/a[@class ='{UNSELECTED_DD_ITEM_CLS}' or @class = '{SELECTED_DD_ITEM_CLS}'])[4]"
CATALOG_DROPDOWN_ITEM_5 = f"(//li/a[@class ='{UNSELECTED_DD_ITEM_CLS}' or @class = '{SELECTED_DD_ITEM_CLS}'])[5]"
CATALOG_DROPDOWN_ITEM_6 = f"(//li/a[@class ='{UNSELECTED_DD_ITEM_CLS}' or @class = '{SELECTED_DD_ITEM_CLS}'])[6]"
CATALOG_DROPDOWN_ITEM_7 = f"(//li/a[@class ='{UNSELECTED_DD_ITEM_CLS}' or @class = '{SELECTED_DD_ITEM_CLS}'])[7]"
CATALOG_DROPDOWN_ITEM_8 = f"(//li/a[@class ='{UNSELECTED_DD_ITEM_CLS}' or @class = '{SELECTED_DD_ITEM_CLS}'])[8]"
CATALOG_DROPDOWN_ITEM_9 = f"(//li/a[@class ='{UNSELECTED_DD_ITEM_CLS}' or @class = '{SELECTED_DD_ITEM_CLS}'])[9]"

SEARCH_FIELD_OUT = "(//input[@class='w-full bg-transparent text-[14px] font-[500] outline-none xl:cursor-pointer'])[3]"  
SEARCH_FIELD_INN = "(//input[@class='w-full bg-transparent text-[14px] font-[500] outline-none xl:cursor-pointer'])[4]"
SEARCH_FOUND_ITEMS = "//div[@class='flex-1 overflow-y-auto px-6 py-4']/child::div"
SEARCH_FOUND_ITEM = "//div[@class='flex-1 overflow-y-auto px-6 py-4']/child::div/child::div/child::a"

CROSS_BUTTON = "(//button[@class='ml-auto text-base-content/80'])[2]"
PHONE = "//div[@class = 'relative flex items-center gap-[8px] xl:cursor-pointer']"
FACEBOOK = "(//*[contains(@href,'www.facebook.com')])[1]"
INSTAGRAM = "(//*[contains(@href,'www.instagram.com')])[1]"
TIKTOK = "(//*[contains(@href,'www.tiktok.com')])[1]"
LOG_IN = "(//a[@class= 'pl-[14px]'])[2]"
CART = "(//div[@class = 'indicator'])[2]"

# Footer
FOOTER = "//div[@class='bg-secondary']"
FACEBOOK_FL = "Facebook"
INSTAGRAM_FL = "Instagram"
TIKTOK_FL = "Tiktok"
ABOUT_US = "Про компанію"
CONTACTS = "Контакти"
PAYMENT = "Оплата і доставка"
PUBLIC_OFERTA = "//a[contains(@href,'/publicOfferta')]"
PRIVACY_POLICY = "//a[contains(@href,'/privacyPolicy')]"
FACEBOOK_FB = "(//*[contains(@href,'www.facebook.com')])[3]"
INSTAGRAM_FB = "(//*[contains(@href,'www.instagram.com')])[3]"
TIKTOK_FB = "(//*[contains(@href,'www.tiktok.com')])[3]"
MAIN_LOGO_FL = "//a[@class = 'flex items-center gap-3']"
FOOTER_SOCIAL_MEDIA_BUTTONS_LIST_ITEMS = "//div[@class='flex items-center gap-5 xl:scale-90 2xl:scale-100']/child::a"
FOOTER_SOCIAL_MEDIA_LINKS_LIST_ITEMS = "//footer/nav[1]/child::a"
FOOTER_ABOUT_US_LINKS_LIST_ITEMS = "//footer/nav[2]/child::a"
FOOTER_LEGAL_LINKS_LIST_ITEMS = "//footer/nav[3]/child::a"

# Cart
CHECKOUT = "//a[@class='false w-full']"
CONTINUE_SHOPPING = "//button/span[@class = 'group relative inline-block h-fit']"
CLOSE_CART = "//button[contains(@class,'h-fit rounded-lg p-1 outline-none')]"
REMOVE_PDP_1 = "(//button[@class='h-fit'])[1]"
CART_POPUP = "//div[@class='modal-box w-full rounded-[50px] bg-white px-0 sm:max-w-[800px] xl:max-w-[1180px]']"

# Product cards
PRODUCT_CARDS = "//div[@class='grid w-full grid-cols-2 gap-3 sm:grid-cols-4 xl:gap-5']/child::a"
PR_CARD = "//a[@class='group relative flex h-full flex-1 flex-col rounded-[20px] bg-white']"

PR_CARD_PRICE = "(//div[(@class = 'text-2xl lg:text-4xl')])[1]"
TO_BUY_1 = "(//button[contains(@class, 'h-[47px] transition-all duration-300')])[1]"
TO_BUY_2 = "(//button[contains(@class, 'h-[47px] transition-all duration-300')])[2]"
TO_BUY_5 = "(//button[contains(@class, 'h-[47px] transition-all duration-300')])[5]"
TO_BUY_6 = "(//button[contains(@class, 'h-[47px] transition-all duration-300')])[6]"

SORT = "//select[contains(@class,'select bg-transparent text-[14px]')]"
SORT1 = "//option[@value='price_asc']"
SORT2 = "//option[@value='price_desc']"
SORT3 = "//option[@value='popular']"

# Category Page
FILTER_MENU_BAR = "//div[contains(@class,'flex h-fit flex-col gap-[30px] rounded-[20px] bg-white p-5')]"
FILTERS_LIST = "(//div[@class = 'flex flex-col gap-[22px]'])[2]/child::div"
FILTER_ITEM = "//div[@class= 'font-[500] text-[14px] xl:text-[14px]']"
FILTERS_ELEMENTS = "(//div[@class='flex flex-col gap-[12px]'])[3]"
SHOW_MORE_BUTTON = "//button[contains(@class,'text-[16px] h-[47px] xl:h-[69px] transition-all duration-300 active:scale-95 font-[600]')]"

# Page Titles
MAIN_PAGE_TITLE = "Інтернет-зоомагазин Лейвен ✅"
DOGS_PAGE_TITLE = "Собаки | Лейвен"
BEDS_PAGE_TITLE = "Будиночки, лежанки, м'які місця | Лейвен"
BLOG_PAGE_TITLE = "Лейвен Блог"
BRANDS_PAGE_TITLE = "Бренди | Лейвен - Інтернет-зоомагазин"
CATS_PAGE_TITLE = "Коти | Лейвен"
DISCOUNTS_PAGE_TITLE = "Акції | Інтернет-зоомагазин Лейвен"
FOODS_PAGE_TITLE = "Сухий корм | Лейвен"
NEW_ARRIVALS_PAGE_TITLE = "Новинки | Інтернет-зоомагазин Лейвен"
SIMPARICA_PAGE_TITLE = "Сімпаріка | Інтернет-зоомагазин Лейвен"

AQUA_PAGE_TITLE = "Акваріумістика | Лейвен"
VET_PAGE_TITILE = "Ветеринарні засоби та препарати | Лейвен"
FEED_PAGE_TITLE = "Годування домашніх тварин і птахів | Лейвен"
RODEN_PAGE_TITLE = "Родентициди | Лейвен"
OUTLET_PAGE_TITLE = "Розпродаж | Лейвен"
DIFF_PAGE_TITLE = "Різне | Лейвен"
CARE_PAGE_TITLE = "Товари для догляду за домашніми тваринами | Лейвен"
COMFORT_PAGE_TITLE = "Товари для комфорту домашніх тварин | Лейвен"
TRAVEL_PAGE_TITLE = "Товари для прогулянок і подорожей з тваринами | Лейвен"

DRY_FOOD_PAGE_TITLE = "Сухий корм | Лейвен"