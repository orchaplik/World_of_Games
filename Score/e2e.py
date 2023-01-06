from selenium import webdriver
from selenium.webdriver.common.by import By


def test_scores_service():
    my_driver = webdriver.Chrome(executable_path="D:\\Users\\WIN10\\Downloads\\chromedriver_win32\\chromedriver.exe")
    my_driver.get("http://127.0.0.1:30000/")
    score = my_driver.find_element(By.ID, VALUE="score")
    if 0 <= int(score) <= 1000:
        return True
    else:
        return False


def main_function():
    test = test_scores_service()
    if test:
        return 0
    else:
        return -1






# my_driver.find_element(By.ID, "arialabel.er8xn").send_keys("אור")
# my_driver.find_element(By.XPATH, "textarea").send_keys("אור")
# my_driver.find_element(By.ID, "gt-submit").click()
