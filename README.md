
# Tools-LMS-PTIT
**Author:** Ha Duy Long - Tôi Yêu PTIT
---
### Bước 1: Tạo môi trường ảo và cài đặt các gói cần thiết
1. Mở terminal và điều hướng đến thư mục dự án.

3. Tạo môi trường ảo `.venv`:
   ```bash
   python -m venv .venv
   ```
   
4. Kích hoạt môi trường ảo:
	- Trên Windows:
	```bash
	.venv\Scripts\activate
	```
	- Trên Linux/MacOS:
	```bash
	source .venv/bin/activate
	```
	
5. Cài đặt các gói cần thiết từ `requirements.txt`:
	```bash
	pip install -r requirements.txt
	```
---
### Bước 2: Tải BurpSuite
- Tải và cài đặt **BurpSuite** từ trang chủ [BurpSuite](https://portswigger.net/burp).
---
### Bước 3: Khởi động BurpSuite

1. Mở BurpSuite.
2. Chọn **Next** và bấm **Start Burp**.
3. Trên thanh công cụ, chọn **Proxy**.
4. Nhấn **Open browser** để mở trình duyệt tích hợp của BurpSuite.
---
### Bước 4: Đăng nhập vào LMS bằng trình duyệt của BurpSuite

1.  Trên trình duyệt BurpSuite, truy cập trang LMS PTIT và tiến hành đăng nhập.
2.  Vào một học phần và chọn bất kỳ một video bài giảng.
3.  Nhấn **F12** để mở Developer Tools và chọn tab **Network** để theo dõi các API của trang web.
4.  Trong tab **Network**, lọc tìm **Fetch/XHR**.
5.  Tìm API có tên **get_session_info**.
---
### Bước 5: Lấy session_id và thông tin payload

1.  Trong **get_session_info**:
    -   Chọn tab **Headers**.
    -   Tìm **Request Headers** > **Cookies** và sao chép **session_id** từ mục **Cookies** rồi dán vào code Python.
2.  Tiếp tục:
    -   Chuyển sang tab **Payload** (bên cạnh **Headers**).
    -   Sao chép **id** và **slide_id** từ payload và dán vào code.
---
### Bước 6: Chạy mã Python

-   Sử dụng thông tin vừa lấy (session_id, id, và slide_id) trong code Python của bạn để tiến hành xử lý tiếp.