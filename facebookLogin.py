#from selenium module import webdriver
from selenium import webdriver

#from selenium module import Keys
from selenium.webdriver.common.keys import Keys

user = "" #enter your facebook username
pwd = ""  #enter your password

#we are initialising Chrome by making an object of it
driver = webdriver.Chrome(executable_path= r'.\\driver\\chromedriver.exe')

#The "driver.get method" will explore to a page given by the URL.WebDriver will hold up until the page has completely been loaded (that is, the "onload" occasion has let go), before returning control to your test or script.
driver.get("http://www.facebook.com")

# "assert" keyword is used to verify the conditions. In this line, we are confirming whether the title is correct or not. For that, we will compare the title with the string which is given.
assert "Facebook" in driver.title

#In this line, we are finding the element of the textbox where the "email" has to be written.
elem = driver.find_element_by_id("email")

#Now we are sending the values to the email section
elem.send_keys(user)

#same for password
elem = driver.find_element_by_id("pass")

elem.send_keys(pwd)

#elem.send_keys(Keys.RETURN) is used to press enter after the values are inserted
elem.send_keys(Keys.RETURN)

#closes
#driver.close()