from selenium import webdriver
from urllib.parse import quote_plus
from urllib.request import urlopen
import os
import time


def save_images(images, save_path):
    for index, image in enumerate(images[:10]):  # images[:크롤링하고 싶은 사진 개수]
        src = image.get_attribute('src')
        t = urlopen(src).read()
        file = open(os.path.join(save_path, str(index + 1) + ".jpg"), "wb")
        file.write(t)
        print("img save " + save_path + str(index + 1) + ".jpg")


def create_folder_if_not_exists(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def make_url(search_term):
    # 네이버 이미지 검색
    base_url = 'https://search.naver.com/search.naver?where=image&section=image&query='

    if search_term == "1000원 지폐":
        color = "blue"
    elif search_term == "5000원 지폐":
        color = "red"
    elif search_term == "10000원 지폐":
        color = "green"
    elif search_term == "50000원 지폐":
        color = "yellow"
    end_url = f'&color={color}'
    return base_url + quote_plus(search_term) + end_url


def crawl_images(search_term):
    # URL 생성
    url = make_url(search_term)

    # chrome 브라우저 열기
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(
        executable_path='C:/Users/joohj/OneDrive/바탕 화면/학교/2022/4차/chromedriver.exe', options=options)
    browser.get(url)

    time.sleep(3)

    # 이미지 긁어오기
    images = browser.find_elements_by_class_name("_image")

    # 저장 경로 설정
    save_path = "C:\\Users\\joohj\\OneDrive\\바탕 화면\\학교\\2022\\4차\\지폐\\크롤링\\네이버\\" + search_term
    create_folder_if_not_exists(save_path)

    # 이미지 저장
    save_images(images, save_path)

    # 마무리
    print(search_term + " 저장 성공")
    browser.close()


if __name__ == '__main__':
    search_words = ["1000원 지폐", "5000원 지폐", "10000원 지폐", "50000원 지폐"]

    for search_word in search_words:
        crawl_images(search_word)
