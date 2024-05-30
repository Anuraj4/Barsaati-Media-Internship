from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from pymongo import MongoClient
from datetime import datetime
import uuid
import random

# ProxyMesh configuration
proxy_list = [
    "proxy1_ip:port",
    "proxy2_ip:port",
    "proxy3_ip:port",
    # Add more proxies as needed
]

# Function to set up the Chrome driver with proxy
def get_driver_with_proxy():
    proxy_ip_port = random.choice(proxy_list)
    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': proxy_ip_port,
        'sslProxy': proxy_ip_port,
    })

    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=%s' % proxy_ip_port)

    driver = webdriver.Chrome(options=options)
    return driver, proxy_ip_port

def scrape_trending_topics():
    driver, ip_address = get_driver_with_proxy()
    driver.get("https://twitter.com/login")

    # Login to Twitter
    username = driver.find_element(By.NAME, "session[username_or_email]")
    password = driver.find_element(By.NAME, "session[password]")
    username.send_keys("your_twitter_username")
    password.send
