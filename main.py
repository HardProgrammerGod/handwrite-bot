import asyncio
import logging
import re
import io
import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import BufferedInputFile
from PIL import Image, ImageDraw, ImageFont

# --- НАЛАШТУВАННЯ ---
API_TOKEN = # add here ur telegram bot api
FONT_PATH = 'myfont.ttf' # name of ur .ttf
IMG_SIZE = (1000, 1400)  
BG_COLOR = (255, 255, 255)
TEXT_COLOR = (20, 30, 100)
FONT_SIZE = 42
MARGIN_LEFT = 70
MARGIN_RIGHT = 60
TOP_MARGIN = 80

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

def wrap_text_by_pixels(text, font, max_width, draw):
    """Розбиває текст на рядки, орієнтуючись на піксельну ширину шрифту."""
    lines = []
    paragraphs = text.split('\n')
    
    for p in paragraphs:
        if not p.strip():
            lines.append("")
            continue
            
        words = p.split(' ')
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            if draw.textlength(test_line, font=font) <= max_width:
                current_line.append(word)
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
        lines.append(' '.join(current_line))
    
    return lines

def create_handwritten_image(text: str):
    image = Image.new("RGB", IMG_SIZE, BG_COLOR)
    draw = ImageDraw.Draw(image)
    
    try:
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    except Exception as e:
        logging.warning(f"Помилка шрифту: {e}")
        font = ImageFont.load_default()

    # очищ текст (оставил укр, англ, цифры та символы физик)
    clean_text = re.sub(r'[^а-яА-ЯіїєґІЇЄҐa-zA-Z0-9\s.,?!=\-/*+()\[\]%^:;°#№"\'&]', '', text) 

    max_w = IMG_SIZE[0] - MARGIN_LEFT - MARGIN_RIGHT
    lines = wrap_text_by_pixels(clean_text, font, max_w, draw)

    current_y = TOP_MARGIN
    line_step = FONT_SIZE + 15 

    for line in lines:
        if not line.strip():
            current_y += line_step
            continue
            
        if current_y + line_step > IMG_SIZE[1] - TOP_MARGIN:
            break 
        
        x_rand = MARGIN_LEFT + random.randint(-2, 3)
        y_rand = current_y + random.randint(-1, 2)
        
        draw.text((x_rand, y_rand), line, font=font, fill=TEXT_COLOR)
        current_y += line_step + random.randint(-2, 2)

    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='JPEG', quality=95)
    img_byte_arr.seek(0)
    return img_byte_arr

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("📝 Надсилайте текст, і я зроблю з нього конспект!\nЯ вирівняв поля та додав ефект реалістичного письма.")

@dp.message(F.text)
async def handle_text(message: types.Message):
    await bot.send_chat_action(message.chat.id, "upload_photo")
    try:
        image_data = create_handwritten_image(message.text)
        photo = BufferedInputFile(image_data.read(), filename="notes.jpg")
        await message.answer_photo(photo)
    except Exception as e:
        logging.error(f"Error: {e}")
        await message.answer("Сталася помилка при генерації.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Бот вимкнений")
