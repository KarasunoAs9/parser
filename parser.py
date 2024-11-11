import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import openpyxl


chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-blink-feature=AutomationControlled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
action = ActionChains(driver)

INPUT_TEXT = ("xpath", "(//input)[1]")
SEARCH_BUTTON = ("xpath", "//span[text()='Знайти роботу']")
FILTER_CHECKBOX = ("xpath", "//span[text()=' Без досвіду ']")
WORKS_BLOCKS = ("xpath", "//div[contains(@class, 'santa--mb-20 ng-star-inserted')]")
PAGE_BLOCKS = ("xpath", "//div[@class='paginator santa-text-16 ng-star-inserted']//a")

driver.get("https://robota.ua/")
wait = WebDriverWait(driver, 15)


i_text = driver.find_element(*INPUT_TEXT)
s_button = driver.find_element(*SEARCH_BUTTON)

i_text.send_keys("python")
s_button.click()

lst = []


wait.until(EC.element_to_be_clickable(FILTER_CHECKBOX)).click()
time.sleep(1)

def find(blocks):
    w_block = wait.until(EC.presence_of_all_elements_located(blocks))
    for i in range(len(w_block)):
        blk = driver.find_elements(*WORKS_BLOCKS)
        block = blk[i]

        action.scroll_to_element(block).perform()
        title_block = block.find_element("xpath", ".//h2").text
        url_block = block.find_element("xpath", ".//a").get_attribute("href")
        lst.append((title_block, url_block))


def next_page(pages_selector, works_blocks):
    pages = driver.find_elements(*pages_selector)
    
    if len(pages) > 1:
        for page_number in range(len(pages)):
            pages = driver.find_elements(*pages_selector)
            page = pages[page_number]
            
            try:
                action.scroll_to_element(page)
                page.click()
                time.sleep(3)
                find(works_blocks)
            except Exception as e:
                find(works_blocks)
                continue
    else:
        find(works_blocks)
        
next_page(PAGE_BLOCKS, WORKS_BLOCKS)

def to_xml(list: list, filename: str):
    df = pd.DataFrame(lst, columns=["Title", "Url"])
    df.to_excel(f"{filename}.xlsx", index=False, engine="openpyxl")
    
def to_file(list: list, filename: str):
    with open(f"{filename}.txt", "w+", encoding="UTF-8") as file:
        for i in list:
            file.write(f"{i}\n")

