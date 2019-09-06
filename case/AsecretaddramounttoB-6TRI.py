from framework.basepage import BasePage
from case.login import Login
import configparser,os
import time

'''
A明文转B 2TRI
'''
driver=Login().login()
bs=BasePage(driver)
config = configparser.ConfigParser()
dir = os.path.abspath('.').split('case')[0]
config.read(dir + "/config/config.ini", encoding='UTF-8')
w2 = config.get("theWallets", "wallet2")
try:
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[4]/div[1]/input").send_keys(w2)
    time.sleep(1)
    driver.find_element_by_id('utxoNormalAmountId').send_keys(600)
    time.sleep(1)
    bs.find_element('id<=>hidePrivacyAmount').click()
    time.sleep(1)
    bs.find_element('id<=>hideNormalAmount').click()
    time.sleep(1)
    driver.find_element_by_id('normalTransferButtonId').click()
    time.sleep(2)
    driver.switch_to_alert().accept()
    driver.find_element_by_xpath('//*[@id="refreshCurrentBalanceButton"]').click()
    time.sleep(5)
except Exception as e:
    print(e)

driver.quit()