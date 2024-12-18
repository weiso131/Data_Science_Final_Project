import os

# 指定資料夾路徑

folder_path = "original_csv"  # 替換為你的資料夾路徑



# 遍歷資料夾中的所有 CSV 檔案
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):  # 檢查是否是 CSV 檔案
        file_path = os.path.join(folder_path, filename)
        
        try:
            # 開啟 CSV 檔案作為純文字
            with open(file_path, 'r', encoding='big5') as file:
                lines = file.readlines()  # 讀取所有行
            
            # 刪除前兩行和最後五行
            lines_to_keep = [line for i, line in enumerate(lines) if i not in list(range(2)) and i not in list(range(len(lines)-6, len(lines)))]
            
            # 移除空行，向前補行
            lines_to_keep = [line for line in lines_to_keep if line.strip() != ""]  # 移除空行
            
            # 儲存處理後的結果為新的檔案
            with open(file_path, 'w', encoding='big5') as file:
                file.writelines(lines_to_keep)  # 將處理過的文字寫回檔案

            print(f"處理完成：{filename}")
        
        except Exception as e:
            print(f"處理檔案 {filename} 時發生錯誤: {e}")

print("所有檔案處理完成")
