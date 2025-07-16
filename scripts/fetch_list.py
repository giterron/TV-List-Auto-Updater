import requests
import os
from datetime import datetime

def fetch_tv_list():
    url = "http://rihou.cc:555/gggg.nzk/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        # 保存到文件
        os.makedirs("../public", exist_ok=True)
        with open("../public/tv-list.txt", "w", encoding="utf-8") as f:
            f.write(response.text)
            
        print("TV list updated successfully!")
        return True
    except Exception as e:
        print(f"Error updating TV list: {e}")
        return False

if __name__ == "__main__":
    if fetch_tv_list():
        # 写入成功标志
        with open("success.log", "w") as log:
            log.write(f"Success at {datetime.utcnow().isoformat()}")
        exit(0)
    else:
        exit(1)
