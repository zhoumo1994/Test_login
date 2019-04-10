from selenium import webdriver
import time
#开始定位
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://admin.91duobaoyu.com/admin_new/#/login')
sw = driver.find_element_by_class_name('el-input__inner')
sw.clear()
sw.send_keys('zhoumo')
sd = driver.find_element_by_name('password')
sd.clear()
sd.send_keys('402496')
driver.find_element_by_xpath('//*[@id="app"]/div/form/button[1]').click()

def ssr(self):
    md = driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/ul/div[3]/button/span/a')
    data = md.get_text()
    self.assertEqual('问题反馈', data)

driver.close()
