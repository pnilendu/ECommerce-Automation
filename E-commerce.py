import random
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By



#initialize webdriver
driver = webdriver.Chrome("C:\\Users\\Win7\\Downloads\\chromedriver_win32\\chromedriver.exe")

#Open URL and maximize window
driver.get('http://tutorialsninja.com/demo/')
driver.maximize_window()

#phones button
laptops=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[1]/nav[1]/div[2]/ul[1]/li[2]/a[1]')
action=ActionChains(driver)
action.move_to_element(laptops).perform()
time.sleep(2)
laptops_2=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[1]/nav[1]/div[2]/ul[1]/li[2]/div[1]/a[1]')
laptops_2.click()
time.sleep(1)


#macbook
macbook=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[2]/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div[1]/h4[1]/a[1]')
macbook.click()
time.sleep(1)

#first picture
first_pic=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/img[1]')
first_pic.click()
time.sleep(2)

#next picture
next_click=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[2]/div[1]/button[2]')

for i in range(0,5):
    next_click.click()
    time.sleep(2)

#save screenshot
driver.save_screenshot('screenshot#' + str(random.randint(0,101)) + '.png')

#close
x_button=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/button[1]')
x_button.click()
time.sleep(1)

#quantity
quantity=driver.find_element(by=By.ID, value='input-quantity')
quantity.click()
time.sleep(1)

quantity.clear()
time.sleep(1)
quantity.send_keys('2')
time.sleep(1)

#add to cart
add_to_button=driver.find_element(by=By.ID, value='button-cart')
add_to_button.click()
time.sleep(2)

#adding hp laptop
laptops=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[1]/nav[1]/div[2]/ul[1]/li[2]/a[1]')

#to move cursor

action=ActionChains(driver)
action.move_to_element(laptops).perform()
time.sleep(2)
laptops_2=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[1]/nav[1]/div[2]/ul[1]/li[2]/div[1]/a[1]')
laptops_2.click()
time.sleep(1)

#click on HP laptop
HP=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/h4[1]/a[1]')
HP.click()
time.sleep(1)

#clicking on pictures and seeing all of them

first_pic=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/img[1]')
first_pic.click()

#next picture
next_click=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[2]/div[1]/button[2]')

for i in range(0,2):
    next_click.click()
    time.sleep(1)

#save screenshot
driver.save_screenshot('screenshot#' + str(random.randint(0,101)) + '.png')

#close pics
x_button=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/button[1]')
x_button.click()
time.sleep(1)

#scroll
add_to_button_2=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/button[1]')
add_to_button_2.location_once_scrolled_into_view
time.sleep(1)

#calendar
calendar=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/button[1]/i[1]')
calendar.click()
time.sleep(1)

next_click_calendar=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[4]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[3]')
month_year=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[4]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[2]')

#year:2022 month:december
while month_year.text != 'December 2022':
    next_click_calendar.click()
time.sleep(2)

#day 31
calendar_date=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[4]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[6]')
calendar_date.click()
time.sleep(2)

#add to button
add_to_button_2.click()
time.sleep(1)

#Checkout
go_to_cart=driver.find_element(by=By.ID, value='cart-total')
go_to_cart.click()
time.sleep(1)

checkout=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/header[1]/div[1]/div[1]/div[3]/div[1]/ul[1]/li[2]/div[1]/p[1]/a[2]/strong[1]')
checkout.click()
time.sleep(1)

#click on guest account
guest=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/label[1]')
guest.click()

#click continue 1
continue_1=driver.find_element(by=By.ID, value='button-account')
continue_1.click()
time.sleep(1)

#scrolling
step_2=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/h4[1]/a[1]')
step_2.location_once_scrolled_into_view
time.sleep(2)

#first name
first_name=driver.find_element(by=By.ID, value='input-payment-firstname')
first_name.click()
time.sleep(1)
first_name.send_keys('test_first_name')
time.sleep(1)

#last_name
last_name=driver.find_element(by=By.ID, value='input-payment-lastname')
last_name.click()
time.sleep(1)
last_name.send_keys('test_last_name')
time.sleep(1)

#email
email=driver.find_element(by=By.ID, value='input-payment-email')
email.click()
time.sleep(1)
email.send_keys('test@test.com')
time.sleep(1)

#telephone
telephone=driver.find_element(by=By.ID, value='input-payment-telephone')
telephone.click()
time.sleep(1)
telephone.send_keys('012345678')
time.sleep(1)

#address
address=driver.find_element(by=By.ID, value='input-payment-address-1')
address.click()
time.sleep(1)
address.send_keys('teststreet 187')
time.sleep(1)

#city
city=driver.find_element(by=By.ID, value='input-payment-city')
city.click()
time.sleep(1)
city.send_keys('Frankfurt')
time.sleep(1)

#postcode
postcode=driver.find_element(by=By.ID, value='input-payment-postcode')
postcode.click()
time.sleep(1)
postcode.send_keys('112233')
time.sleep(1)


#country
country=driver.find_element(by=By.ID, value='input-payment-country')
dropdown_1=Select(country)
time.sleep(1)
dropdown_1.select_by_index(87)
time.sleep(1)

#region
region=driver.find_element(by=By.ID, value='input-payment-zone')
dropdown_2=Select(region)
time.sleep(1)
dropdown_2.select_by_visible_text('Hessen')
time.sleep(1)

#click continue 2
continue_2=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/input[1]')
continue_2.click()
time.sleep(1)

#click continue 3
continue_3=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div[1]/input[1]')
continue_3.click()
time.sleep(1)

#accept terms & conditions
t_e=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[5]/div[2]/div[1]/div[2]/div[1]/input[1]')
t_e.click()
time.sleep(1)

#click continue 4
continue_4=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[5]/div[2]/div[1]/div[2]/div[1]/input[2]')
continue_4.click()
time.sleep(1)

#final price
final_price=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[6]/div[2]/div[1]/div[1]/table[1]/tfoot[1]/tr[3]/td[2]')

print("The final price of both products is " + final_price.text)
time.sleep(1)

#click on the confirmation button
confirmation_button=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[6]/div[2]/div[1]/div[2]/div[1]/input[1]')
confirmation_button.click()
time.sleep(2)


#success text
success_text=driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[2]/div[1]/div[1]')
print(success_text.text)
time.sleep(1)

driver.close()