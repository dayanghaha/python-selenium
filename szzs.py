from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait  #等待
from selenium.webdriver.support import expected_conditions #预期条件类
from selenium.webdriver.common.by import By   #为了等待定位元素

driver=webdriver.Ie()
#登陆系统
driver.get('http://192.168.0.200:8080/xtxraweb/')
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="txtPass"]').click()
driver.find_element_by_xpath('//*[@id="txtPass"]').send_keys('111111')    #为什么输入密码时候这个慢？？？？？？
#current_window=driver.current_window_handle
driver.find_element_by_xpath('//*[@id="Image1"]').click()
#driver.switch_to.window(current_window)
time.sleep(1) #确保跳转至页面

fn=open("D:\\feng.txt","r")
ff=fn.readlines()
#while True:
for i in ff:
    j=i.split('"')
    num=j[1]
    driver.refresh()
    try:
        WebDriverWait(driver, 10, 0.5).until(expected_conditions.presence_of_element_located((By.ID, 'frmMenu')))
    except:
        driver.refresh()
    driver.switch_to.frame('frmMenu')  #进入frame框架

    #WebDriverWait(driver, 10, 0.5).until(expected_conditions.presence_of_element_located((By.ID, '700004')))
    driver.find_element_by_xpath('//*[(@class="closed last" or @class="last closed") and @id="700004"]').click()
    time.sleep(1)
    #WebDriverWait(driver, 6, 0.5).until(expected_conditions.presence_of_element_located((By.ID, '111005')))
    driver.find_element_by_xpath('//*[@class="last leaf" and @id="111005"]').click()

    driver.switch_to.parent_frame()      #退入当前frame框架
    driver.switch_to.frame('frmShow')  #进入frame框架

    WebDriverWait(driver, 6, 0.5).until(expected_conditions.presence_of_element_located((By.ID, 'txtEnvsn')))
    driver.find_element_by_xpath('//*[@id="txtEnvsn"]').click()
    driver.find_element_by_xpath('//*[@id="txtEnvsn"]').send_keys(str(num))#这里改了
    driver.find_element_by_xpath('//*[@id="btnOK"]').click()

    #WebDriverWait(driver, 6, 0.5).until(expected_conditions.presence_of_element_located(By.ID,''))
    time.sleep(2)
    driver.find_element_by_xpath('//a[contains(@href,"downddetailAction.action?tradeSn")]').click()
    #driver.find_element_by_xpath('//*[@id="Button2"]').click()    #这个应该就能直接运行了

    driver.switch_to.parent_frame()  # 退入当前frame框架
    shuru=input("继续输入1，不继续输入0！！！")
    if shuru is'0':
        break
    else:
        driver.refresh()
        continue
driver.quit()
#IE浏览器必须把该网站弄成兼容性视图设置!!!!!!!!!!!!!!
