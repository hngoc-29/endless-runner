# 🦖 Dino Run – Game Python Platformer

Một trò chơi chạy vô tận đơn giản giống Chrome Dino, viết bằng **Python + Pygame**, có âm thanh, điểm số cao, tăng tốc theo thời gian và hiệu ứng hình ảnh động.

![screenshot](https://i.imgur.com/4RMVfQa.png) <!-- Bạn có thể thay bằng ảnh thật từ project -->

---

### 📦 Link tải bản chơi thử `.exe`

👉 [Tải bản chạy sẵn (.exe)](https://example.com/dino_run.exe)
*(Thay link bằng Google Drive, Dropbox hoặc nơi bạn up file `dino_run.exe`)*

---

## 🚀 Tính năng nổi bật

* Nhảy, ngồi và tránh chướng ngại vật
* Hệ thống tăng tốc theo thời gian
* Nhạc nền và hiệu ứng âm thanh tùy bật/tắt
* Điểm số và High Score được lưu lại
* Menu khởi đầu thân thiện

---

## 🛠️ Yêu cầu cài đặt

* Python 3.10+
* Pygame:

  ```bash
  pip install pygame
  ```

---

## 📁 Cấu trúc thư mục

```
.
├── main.py
├── player.py
├── obstacle.py
├── logic.py
├── define.py
├── assets/
│   ├── image/
│   ├── sound/
│   └── text/highscore.txt
```

---

## 🏃‍♂️ Chạy game

```bash
python main.py
```

---

## 🧱 Build file `.exe`

Dùng [PyInstaller](https://pyinstaller.org/) để đóng gói:

1. Cài:

   ```bash
   pip install pyinstaller
   ```

2. Build:

   ```bash
   pyinstaller main.py --onefile --add-data "assets;assets" --windowed
   ```

3. File `.exe` sẽ nằm ở `dist/main.exe`

---

## 📄 Ghi chú khi build

Nếu bạn dùng:

```python
ASSET_PATH = os.path.join(ROOT_PATH, 'assets')
```

Hãy thay bằng:

```python
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

ASSET_PATH = resource_path('assets')
```

---

## 📬 Liên hệ & đóng góp

Góp ý, cải tiến hoặc báo lỗi qua GitHub hoặc email.
