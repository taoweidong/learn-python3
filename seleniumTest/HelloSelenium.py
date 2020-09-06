# -*- coding: utf-8 -*-
from selenium.webdriver import ActionChains
from time import sleep

from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Chrome()
    # time.sleep(5.5)

    all_hand = driver.window_handles

    driver.maximize_window()
    driver.get('https://www.imooc.com/')
    driver.find_element_by_xpath('//*[@id="nav"]/div[3]/div[1]/input[1]').send_keys('java')
    driver.find_element_by_xpath('//*[@id="nav"]/div[3]/div[2]/i').click()
    driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div[1]/div[2]/div[4]/div/a').click()

    driver.switch_to_window(all_hand[-1])
    sleep(3)
    driver.find_element_by_xpath('//*[@id="nav"]//a[@href="/read"]').click()
    result = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/ul/li/div/a[1]/p[@class="title"]')
    print(result.text)
    # 鼠标悬停事件
    # ActionChains(driver).move_to_element(driver.find_element_by_xpath(
    #     '//*[@id="main"]//div[@class="item" and @data-id="e"]')).perform()
    # driver.refresh()
    # driver.quit()
