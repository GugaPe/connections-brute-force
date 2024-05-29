from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import itertools

date_of_wordle = input('Enter the date of the wordle: ')

url = "https://www.connectionsunlimited.org/?archive=" + date_of_wordle


def select_bruteforce(number_of_combinations):
    found_array = []
    select_known(found_array)
    for i in range(number_of_combinations):
        found = True
        time.sleep(1)
        game_elements = driver.find_elements(By.CLASS_NAME, "game-item")
        game_elements_texts = [i.text for i in game_elements]
        comb = itertools.combinations(game_elements_texts, 4)
        while found is True:
            for i in comb:
                for j in i:
                    driver.find_element(By.XPATH, f"//*[text()='{j.upper()}']").click()
                    submit = driver.find_element(By.XPATH, "//*[text()='Submit']")
                    submit.click()
                if len(driver.find_elements(By.CLASS_NAME, "game-item")) != len(game_elements):
                    found_array.append(driver.find_elements(By.CLASS_NAME, "group-members")[-1].text.split(', '))
                    found = False
                    break
                for j in i:
                    driver.find_element(By.XPATH, f"//*[text()='{j.upper()}']").click()
                if driver.find_element(By.CLASS_NAME, "game-attempts").text[-1] == '0':
                    driver.find_element(By.XPATH, "//*[contains(text(), 'Restart')]").click()
                    select_known(found_array)


def select_known(list_of_known_words):
    time.sleep(1)
    if len(list_of_known_words) == 0:
        return
    for i in list_of_known_words:
        for j in i:
            element = driver.find_element(By.XPATH, f"//*[text()='{j.upper()}']")
            element.click()
        submit = driver.find_element(By.XPATH, "//*[text()='Submit']")
        submit.click()
        time.sleep(1)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('executable_path=C:/Users/gptaszynski/Downloads/chromedriver.exe')
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
time.sleep(1)

accept_cookies = driver.find_element(By.ID, "ez-accept-all")
accept_cookies.click()

select_bruteforce(4)

time.sleep(10000)

driver.quit()
