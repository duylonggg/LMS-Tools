import requests

SLIDE_IDs = [68, 69, 70, 71]
ID = 0
SESSION_ID = '5b623dc90e7963cacce132453de034c51c98d507'

def use_existing_session():
    url = "https://lms.ptit.edu.vn/slides/slide/set_completed"
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36",
    }

    cookies = {
        "session_id": SESSION_ID,
        "frontend_lang": "vi_VN",
    }
    
    for SLIDE_ID in SLIDE_IDs:
        payload = {
            "jsonrpc": "2.0",
            "method": "call",
            "params": {
                "slide_id": SLIDE_ID
            },
            "id": ID
        }

        response = requests.post(url, json=payload, headers=headers, cookies=cookies)

        if response.status_code == 200:
            print("Yêu cầu thành công!")
            print(response.json()) 
        else:
            print(f"Yêu cầu thất bại. Mã trạng thái: {response.status_code}")

if __name__ == "__main__":
    use_existing_session()
