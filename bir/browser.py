from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

# 使用者輸入資料
stock = input("輸入要爬的股票代號 ex:台積電輸入2330\n")
start_year = input("輸入爬蟲起始時間西元年份,最早2011 ex:2024\n")
start_month = input("輸入爬蟲起始時間月份 ex:9\n")
end_year = input("輸入爬蟲結束時間西元年份 ex:2024\n")
end_month = input("輸入爬蟲結束時間月份(包含),不能超過現在時間,因為我不想寫try/except ex:9\n")

# 設置 ChromeDriver
chrome_options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 開啟指定網頁
driver.get("https://www.twse.com.tw/zh/trading/historical/stock-day.html")

try:
    # 等待網頁元素加載完成，使用 WebDriverWait
    wait = WebDriverWait(driver, 10)

    # 等待股票代號輸入框可用
    stock_input = wait.until(EC.presence_of_element_located((By.NAME, "stockNo")))
    stock_input.clear()
    stock_input.send_keys(stock)  # 輸入股票代號

    
    while True:
        # 等待年份下拉選單可用
        year_select = wait.until(EC.presence_of_element_located((By.NAME, "yy")))
        year_select_dropdown = Select(year_select)
        year_select_dropdown.select_by_value(start_year)  # 根據年份選擇

        # 等待月份下拉選單可用
        month_select = wait.until(EC.presence_of_element_located((By.NAME, "mm")))
        month_select_dropdown = Select(month_select)
        month_select_dropdown.select_by_value(start_month)  # 根據月份選擇

        query_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "submit")))
        query_button.click()

        csv_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "csv")))
        driver.execute_script("arguments[0].click();", csv_button)

        
        if start_month==end_month and start_year==end_year:
            break

        a=int(start_month)
        a+=1
        if a==13:
            a=1
            b=int(start_year)
            b+=1
            start_year=str(b)
        start_month=str(a)
        time.sleep(1)

        
        
except Exception as e:
    print("發生錯誤:", e)


input("輸入任意字元結束程式")

# 關閉瀏覽器
driver.quit()
