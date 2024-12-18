import os

# 指定資料夾路徑
folder_path = "original_csv"  # 替換成您的資料夾路徑
output_file = "merged_output.csv"  # 輸出結果的檔案路徑

# 遍歷資料夾中的所有 CSV 檔案
files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

all_content = ["\"日期\",\"成交股數\",\"成交金額\",\"開盤價\",\"最高價\",\"最低價\",\"收盤價\",\"漲跌價差\",\"成交筆數\"\n"]  # 用來儲存所有檔案的內容

# 讀取所有檔案並將內容加到 all_content
for filename in sorted(files):  # 按照字典順序排序
    file_path = os.path.join(folder_path, filename)
    
    try:
        # 讀取 CSV 文件當作純文本
        with open(file_path, 'r', encoding='big5') as infile:
            content = infile.readlines()  # 讀取每一行
            all_content.extend(content)  # 把內容加入 all_content
        print(f"處理完成：{filename}")
    
    except Exception as e:
        print(f"處理檔案 {filename} 時發生錯誤: {e}")

# 合併完成後刪除所有的空行
all_content = [line for line in all_content if line.strip() != ""]

# 儲存處理後的結果為新的檔案
with open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.writelines(all_content)  # 寫入所有非空的行

print(f"所有檔案已經合併並儲存為 {output_file}")
