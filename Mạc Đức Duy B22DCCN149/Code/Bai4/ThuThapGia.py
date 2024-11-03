from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time

# Thiết lập Selenium để chạy Chrome ở chế độ ẩn (headless)
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# URL trang web chứa dữ liệu chuyển nhượng
url = 'https://www.footballtransfers.com/en/transfer-values'

# Truy cập trang web
driver.get(url)
time.sleep(3)  # Đợi trang tải xong (tăng thời gian này nếu trang tải chậm)

# Lấy nội dung trang
page_content = driver.page_source
soup = BeautifulSoup(page_content, 'html.parser')

# Tìm bảng chứa thông tin chuyển nhượng cầu thủ
players = []
for row in soup.select('table tbody tr'):  # Duyệt qua từng hàng trong bảng
    try:
        # Lấy tên cầu thủ
        name = row.select_one('.player-name').text.strip()

        # Lấy đội bóng
        team = row.select_one('.club-name').text.strip()

        # Lấy giá trị chuyển nhượng
        transfer_value = row.select_one('.value').text.strip()

        # Lưu thông tin vào danh sách players
        players.append({
            "Tên cầu thủ": name,
            "Đội bóng": team,
            "Giá trị chuyển nhượng": transfer_value
        })
    except AttributeError:
        continue  # Bỏ qua hàng nào không có đủ dữ liệu

# Đóng trình duyệt
driver.quit()

# Chuyển dữ liệu thành DataFrame và lưu vào CSV
df = pd.DataFrame(players)
df.to_csv('results3.csv', index=False, encoding='utf-8')
print("Dữ liệu đã được lưu vào results3.csv")
