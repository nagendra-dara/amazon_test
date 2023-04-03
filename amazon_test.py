from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

class Amazon_Shopping:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        path_to_chrome_driver = 'c:/my_programs/chromedriver'
        self.driver = webdriver.Chrome(executable_path=path_to_chrome_driver)
        self.wait = WebDriverWait(self.driver, 40)

    def login(self):
        self.driver.get("https://www.amazon.in/")
        self.driver.maximize_window()

        # Validation1 for correct url validation
        # Get the url of the current page
        actual_url = self.driver.current_url

        # Define the expected title
        expected_url = "https://www.amazon.in/"

        # Validate that the actual title matches the expected title
        if actual_url == expected_url:
            print("Correct url is opened.")
        else:
            print("Incorrect url is opened")
        time.sleep(5)

        # Validation2 for title validation
        # Get the title of the current page
        actual_title = self.driver.title

        # Define the expected title
        expected_title = "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"

        # Validate that the actual title matches the expected title
        if actual_title == expected_title:
            print("Title is correct.")
        else:
            print("Title is incorrect.")
        time.sleep(5)

        drop_down_button = self.wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='nav-link-accountList']/span/span")))
        drop_down_button.click()

        email_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='ap_email']")))
        email_input.send_keys(self.email)

        continue_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='continue']")))
        continue_btn.click()

        password_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ap_password")))
        password_input.send_keys(self.password)

        signin_btn = self.wait.until(EC.presence_of_element_located((By.ID, "signInSubmit")))
        signin_btn.click()

        '''time.sleep(15)

        # handling captcha manually using web driver waits
        password_re_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='ap_password']")))
        password_re_input.send_keys(self.password)

        time.sleep(5)

        signin_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='signInSubmit']")))
        signin_btn.click()
        time.sleep(5)'''


    def add_to_cart(self):
        search_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='twotabsearchtextbox']")))
        actual_text = "(Renewed)Redmi Note 12 5G Frosted Green 4GB RAM 128GB ROM |"
        search_input.send_keys(actual_text)
        search_input.send_keys(Keys.RETURN)

        # get the Window Handle of the parent window
        parent_window = self.driver.current_window_handle

        time.sleep(15)
        # self.driver.implicitly_wait(30)
        product_link = self.wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='search']/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span")))
        #product_text = product_link.text
        product_link.click()
        time.sleep(15)




        # retrieve the Window Handles of all open windows
        all_windows = self.driver.window_handles

        # loop through the set of Window Handles and find the new window
        for window in all_windows:
            if window != parent_window:
                new_window = window

        # switch to the new window
        self.driver.switch_to.window(new_window)

        #Taking product price of searched product before adding to the cart for validating
        product_price = self.wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='corePriceDisplay_desktop_feature_div']/div[1]/span[2]/span[2]/span[2]")))
        original_prodict_price = product_price.text

        # Click on the Add to Cart button
        add_to_cart_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='submit.add-to-cart']")))
        add_to_cart_button.click()
        time.sleep(25)


        place_order_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='sc-buy-box-ptc-button']/span/input")))
        place_order_link.click()
        time.sleep(20)

        use_this_address_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='shipToThisAddressButton']/span/input")))
        use_this_address_button.click()
        time.sleep(15)

        # Find the cash on delivery button by its XPath
        last_radio_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='radio'])[5]")))
        last_radio_button.click()

        time.sleep(15)
        use_this_payment_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='orderSummaryPrimaryActionBtn']/span/input")))
        use_this_payment_button.click()
        time.sleep(10)

        product_in_the_cart = self.wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='spc-orders']/div/div/div/div/div/div[3]/div[1]/div/div/div/div/div/div[2]/div[1]/span")))
        cart_product_name = product_in_the_cart.text

        # Validate that the actual search text matches the result in the cart
        if actual_text in cart_product_name:
            print("correct product is added to the cart.\n Searched Product Name: {} \n Product in Cart: {}".format(actual_text, cart_product_name[:58]))
        else:
            print("Incorrect product is added to the cart.\n Searched Product Name: {} \n Product in Cart: {}".format(actual_text, cart_product_name[:58]))
        time.sleep(10)

        # validating the product price and Order Total Price
        cart_product_price = self.wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='subtotals-marketplace-table']/tbody/tr[6]/td[2]")))
        order_total_price = cart_product_price.text

        if original_prodict_price in order_total_price:
            print('Correct price Product is added to the cart.\n Original Product price:{}, Order Total Price {}'.format(original_prodict_price , order_total_price))
        else:
            print('Incorrect price product is added to the cart.\n Original Product price:{},  Order Total Price {}'.format(original_prodict_price , order_total_price))

        # Click on a link or button that opens the pop-up window
        pop_up_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='spc-orders']/div/div/div/div/div/div[3]/div[1]/div/div/div/div/div/div[2]/div[3]/div[1]/div/span/span/span/span/span/span")))
        pop_up_button.click()
        time.sleep(15)



        # Delete the selected option using the "delete" key
        pop_up_button.send_keys(Keys.DELETE)


if __name__ == "__main__":
    email = "nagendra.dara0464@gmail.com"
    password = "Resume@123"
    shopping = Amazon_Shopping(email, password)
    shopping.login()
    shopping.add_to_cart()




