from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\\Users\\kh2jg\\Desktop\\Fuck" # Your Chrome Driver path
driver = webdriver.Chrome(chrome_driver, options=chrome_options)