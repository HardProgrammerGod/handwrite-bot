# 📝 Handwritten Notes Generator Bot

An automated Telegram bot that transforms digital text into aesthetically pleasing "handwritten" documents. Perfect for students, teachers, or anyone who wants to give their notes a personal touch without picking up a pen.

## ✨ Key Features
* **Realistic Simulation:** Subtle random character offsets ($X$ and $Y$ jitter) to mimic human handwriting.
* **Smart Typography:** Automatic word wrapping and line spacing based on pixel-perfect measurements.
* **Multi-language Support:** Process texts in **English**, **Ukrainian**, and **Russian** including special physics/math symbols.
* **High Quality:** Generates sharp JPEG images ready for printing or sharing.

---

## 🛠 Tech Stack
* **[aiogram 3.x](https://docs.aiogram.dev/)** – Modern asynchronous framework for Telegram Bots.
* **[Pillow (PIL)](https://python-pillow.org/)** – Powerful imaging library for generating the "paper" and "writing".
* **[Python 3.10+](https://www.python.org/)** – Core logic.

---

## 🌍 Language Support
The bot is pre-configured to filter and render:
1.  **Latin Alphabet:** (English, etc.)
2.  **Cyrillic Alphabet:** (Ukrainian, Russian, Belarusian)
3.  **Math & Symbols:** Basic arithmetic, degrees, and common brackets:
    > `+ - * / = % ^ [ ] ( ) ° # № " ' &`

---

## 🚀 Installation & Setup

### 1. Prerequisites
Ensure you have a `.ttf` font file that looks like handwriting (e.g., `myfont.ttf`).

### 2. Clone the Repository
```bash
git clone https://github.com/yourusername/handwritten-bot.git
cd handwritten-bot
```

### 3. Install Dependencies
```bash
pip install -U aiogram Pillow
```

### 4. Configuration
Open `main.py` and update the following:
```python
API_TOKEN = "YOUR_BOT_TOKEN_HERE"
FONT_PATH = "your_handwriting_font.ttf"
```

---

## 🎨 Customization
You can easily adjust the "paper" style in the `--- НАЛАШТУВАННЯ ---` section:

| Variable | Effect |
| :--- | :--- |
| `BG_COLOR` | Change background (e.g., beige or grey) |
| `TEXT_COLOR` | Change "ink" color (Deep Blue, Black, etc.) |
| `FONT_SIZE` | Adjust how large the writing appears |
| `MARGINS` | Control the "padding" on the sides of the paper |

---

## 📸 How it Works
1.  **Send Text:** User sends a long text or essay to the bot.
2.  **Processing:** The bot cleans the text, wraps it to fit the page, and draws it onto a virtual canvas.
3.  **Output:** The bot replies with a high-quality photo of the "written" note.

---

## 📜 License
Distributed under the MIT License. Use it for your homework, projects, or just for fun!

---

### 👨‍💻 Author
Created by Hard  
*Turning code into ink, one line at a time.*
