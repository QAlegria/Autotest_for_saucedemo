from pathlib import Path

HOME_PAGE_URL = 'https://www.saucedemo.com/'
INVENTORY_PAGE_URL = f'{HOME_PAGE_URL}inventory.html'
CART_PAGE_URL = f'{HOME_PAGE_URL}cart.html'
INVENTORY_ITEM_PAGE_URL = f'{HOME_PAGE_URL}inventory-item.html**'
CHECK_OUT_FIRST_PAGE_URL = f'{HOME_PAGE_URL}checkout-step-one.html'

STATIC_IMAGE_URL = f'{HOME_PAGE_URL}static/media/'
TWITTER_LINK = 'https://twitter.com/saucelabs'
X_TWITTER_LINK = 'https://x.com/saucelabs'
FACEBOOK_LINK = 'https://www.facebook.com/saucelabs'
LINKEDIN_LINK = 'https://www.linkedin.com/company/sauce-labs/'
TERMS_FOOTER_TEXT = '© 2025 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy'

JSON_DIR = current_dir = Path(__file__).parent.parent / 'data' / 'inventory_products.json'
