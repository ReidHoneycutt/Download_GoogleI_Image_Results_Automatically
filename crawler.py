import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import requests


FIREFOX_DRIVER_PATH = "C:\\Users\\reidh\\Downloads\\geckodriver-v0.32.0-win32\\geckodriver.exe"
NULL_PATH = "C:\\Users\\reidh\\OneDrive\\Documents\\shit"


class Crawler:
    def __init__(self, query=None, num_imgs=None, images_path=None) -> None:
        self.url = "https://google.com/search?q="+query
        self.query = query
        self.num_imgs = num_imgs
        self.images_path = images_path

        self.driver = None
        self.set_driver()

    def set_driver(self) -> None:
        print("SETTING DRIVER ...", end='\r', flush=True)
        options = Options()
        options.binary_location = r"C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        options.headless = True
        self.driver = webdriver.Firefox(options=options,
                                        executable_path=FIREFOX_DRIVER_PATH)

    def go_to_imgs_url(self) -> None:
        print("NAVIGATING TO IMAGES PAGE ...", end='\r', flush=True)
        self.driver.get(self.url)
        time.sleep(3)
        mufpac_div = self.driver.find_elements(By.CLASS_NAME, 'MUFPAc')

        for element in mufpac_div:
            try:
                divs = element.find_elements(By.CLASS_NAME, 'hdtb-mitem')
                for div in divs:
                    containers = div.find_elements(By.TAG_NAME, 'a')
                    for container in containers:
                        if container.text == 'Images':
                            self.driver.get(container.get_attribute('href'))
                            return

            except NoSuchElementException:
                print('No Data Available!')

    def get_imgs(self):
        print("GETTING IMAGES ...", end='\r', flush=True)
        print('\r', flush=True)
        self.go_to_imgs_url()

        img_num = 0
        session_clicks = 1
        for i in range(self.num_imgs):
            element = self.driver.find_elements(By.XPATH, '//*[@id="islrg"]/div[1]/div[' + str(i) + ']')
            if len(element) > 0:
                element[0].find_elements(By.TAG_NAME, 'a')[0].click()
                mini_window = self.driver.find_elements(By.XPATH, '/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[' +
                                                 str(session_clicks)
                                                 + ']/div/div/div[3]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img')

                if len(mini_window) > 0:
                    img_src = mini_window[0].get_attribute('src')
                    if img_src[:5] == 'https':
                        response = requests.get(img_src)
                        if response.status_code == 200:
                            print("DOWNLOADING "+self.query+str(img_num)+".jpg", end='\r', flush=True)
                            with open(self.images_path+'\\'+self.query+str(img_num)+".jpg", 'wb') as f:
                                f.write(response.content)
                            img_num += 1
                session_clicks += 1

            time.sleep(0.5)
        print('\r', flush=True)
        print("DONE.")
        self.driver.quit()
