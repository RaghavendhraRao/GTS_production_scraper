from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
#from selenium.webdriver import FirefoxOptions
from random import choice
import time

desktop_agents = \
    ['Mozilla/5.0(Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML, like Gecko) '
     'Chrome/54.0.2840.99 Safari/537.36',
     'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) '
     'Chrome/54.0.2840.99 Safari/537.36',
     'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) '
     'Chrome/54.0.2840.99 Safari/537.36',
     'Mozilla/5.0(Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14(KHTML, like Gecko) '
     'Version/10.0.1 Safari/602.2.14',
     'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) '
     'Chrome/54.0.2840.71 Safari/537.36',
     'Mozilla/5.0(Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36(KHTML, like Gecko) '
     'Chrome/54.0.2840.98 Safari/537.36',
     'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36(KHTML, like Gecko) '
     'Chrome/54.0.2840.98 Safari/537.36',
     'Mozilla/5.0(Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML, like Gecko) '
     'Chrome/54.0.2840.71 Safari/537.36',
     'Mozilla/5.0(Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) '
     'Chrome/54.[;;[;0.2840.99 Safari/537.36',
     'Mozilla/5.0(Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']

#options = FirefoxOptions()
#options.headless = True

options = Options()
options.headless = True
#executable_path='/data/softwares/geckodriver'
# service=s
s = Service('/data/softwares/geckodriver')
print("checking driver")
#driver = webdriver.Firefox(options=options, executable_path='/data/softwares/geckodriver')
driver = webdriver.Firefox(options=options,executable_path='/data/softwares/geckodriver')
time.sleep(2)
driver.get("https://www.google.com")
time.sleep(5)
#logger.info("Driver started ----> Headless")
print("Driver started..")
driver.quit()
userAgent = choice(desktop_agents)
driver.addheaders = [('User-Agent', userAgent),
                     ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                     ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),
                     ('Accept-Encoding', 'none'),
                     ('Accept-Language', 'en-US,en;q=0.8'),
                     ('Connection', 'keep-alive')]
print("driver closed")
