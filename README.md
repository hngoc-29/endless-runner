# 🦖 Dino Run – Game Python Platformer

Một trò chơi chạy vô tận đơn giản giống Chrome Dino, viết bằng **Python + Pygame**, có âm thanh, điểm số cao, tăng tốc theo thời gian và hiệu ứng hình ảnh động.

---

![screenshot](https://github.com/hngoc-29/endless-runner/raw/main/assets/images/exam1.png)

![screenshot](https://github.com/hngoc-29/endless-runner/raw/main/assets/images/exam2.png)

![screenshot](https://github.com/hngoc-29/endless-runner/raw/main/assets/images/exam3.png)

---

### 📦 Link tải bản chơi thử `.exe`

👉 [Tải bản chạy sẵn (.exe)](https://github.com/hngoc-29/endless-runner/raw/main/dist/Dino.exe)

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
│   ├── ARIAL.TTF
│   └── highscore.txt
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
   Hoặc nếu muốn có icon
   ```bash
   pyinstaller main.py --onefile --add-data "assets;assets" --windowed --icon="<thư mục gốc>\assets\images\logoGame.ico"
   ```

3. File `.exe` sẽ nằm ở `dist/main.exe`

---

## 📬 Liên hệ & đóng góp

Góp ý, cải tiến hoặc báo lỗi qua GitHub hoặc email.
