from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os


def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")


def crawling_img(name):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(
        executable_path='C:/Users/joohj/OneDrive/바탕 화면/학교/2022/4차/chromedriver.exe', options=options)

    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    elem = driver.find_element_by_name("q")
    elem.send_keys(name)
    elem.send_keys(Keys.RETURN)

    dir = "C:\\Users\\joohj\\OneDrive\\바탕 화면\\학교\\2022\\4차\\지폐\\크롤링\\구글\\" + name

    createDirectory(dir)  # 폴더 생성
    count = 1
    for i in range(1, 50):
        try:
            imgUrl = driver.find_element_by_xpath(
                f'//*[@id="islrg"]/div[1]/div[{i}]/a[1]/div[1]/img').get_attribute(
                "src")
            path = "C:\\Users\\joohj\\OneDrive\\바탕 화면\\학교\\2022\\4차\\지폐\\크롤링\\구글\\" + name + "\\"
            urllib.request.urlretrieve(
                imgUrl, path + name + str(count) + ".jpg")
            count += 1
        except:
            break
    driver.close()


search_words = ["1000원 지폐", "5000원 지폐", "10000원 지폐", "50000원 지폐"]

for search_word in search_words:
    crawling_img(search_word)

print("finished")
