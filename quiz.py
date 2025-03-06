import requests

SESSION_ID = "5b623dc90e7963cacce132453de034c51c98d507"  
SLIDE_DATA = {
    166: 1640,
    167: 1680,
    168: 1760,
    169: 1800
}

def submit_quiz(num_submits, step=4):
    url = "https://lms.ptit.edu.vn/slides/slide/quiz/submit"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9,vi;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Cookie": "_ga=GA1.3.62599926.1696842192; _ga_WF3VN29N2R=GS1.3.1723679742.14.0.1723679742.0.0.0; pll_language=vi; frontend_lang=vi_VN; tz=Asia/Bangkok; session_id=" + SESSION_ID,
        "Host": "lms.ptit.edu.vn",
        "Origin": "https://lms.ptit.edu.vn",
        "Sec-Ch-Ua": "\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0"
    }
    
    for slide_id, start_ans_id in SLIDE_DATA.items():
        answer_ids = [start_ans_id + i * step for i in range(num_submits)] 
        payload = {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "call",
            "params": {
                "slide_id": slide_id,
                "answer_ids": answer_ids
            }
        }
        
        response = requests.post(url, json=payload, headers=headers)
        print(f"Submit (Slide {slide_id}): {answer_ids} -> Status: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    submit_quiz(num_submits=10)