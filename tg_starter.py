import os

def create_folders(folder_name):
    try:
        os.mkdir(folder_name)
        print(f"Папка '{folder_name}' успешно создана.")
        
        os.mkdir(os.path.join(folder_name, 'handlers'))
        os.mkdir(os.path.join(folder_name, 'keyboards'))
        os.mkdir(os.path.join(folder_name, 'settings'))
        
        bot_tg_code = '''from aiogram import executor
from create_bot import dp
from handlers import start_connect

async def on_startup(_):
    print("Bot Online!")
    
start_connect.register_handlers_start_connect(dp)
    
def main():
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

if __name__ == '__main__':
    main()'''

        with open(os.path.join(folder_name, 'bot_tg.py'), 'w') as file:
            file.write(bot_tg_code)

        create_bot_code = '''from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from settings.file_settings import API_KEY_TG

bot = Bot(token=API_KEY_TG)
dp = Dispatcher(bot, storage=MemoryStorage())
        '''  # Ваш код для create_bot.py

        with open(os.path.join(folder_name, 'create_bot.py'), 'w') as file:
            file.write(create_bot_code)
        
        env_code = '''API_KEY_TG='''

        with open(os.path.join(folder_name,'settings', '.env'), 'w') as file:
            file.write(env_code)

        file_settings_code = f'''import dotenv
import os

dotenv.load_dotenv("{folder_name}\\settings\\.env")
API_KEY_TG = os.environ["API_KEY_TG"]'''

        with open(os.path.join(folder_name,'settings', 'file_settings.py'), 'w') as file:
            file.write(file_settings_code)

        start_connect_code = '''from aiogram import types,Dispatcher
from keyboards.main_kb import main_menu

#@dp.message_handler(commands='start',state=None)
async def start(message: types.Message, state=None):
    await message.answer("Добро пожаловать!",reply_markup=main_menu)
     
     
def register_handlers_start_connect(dp: Dispatcher):
    dp.register_message_handler(start,commands="start",state=None)
'''

        with open(os.path.join(folder_name,'handlers', 'start_connect.py'), 'w') as file:
            file.write(start_connect_code)

        init_for_handlers_code = '''from handlers import start_connect'''

        with open(os.path.join(folder_name,'handlers', '__init__.py'), 'w') as file:
            file.write(init_for_handlers_code)

        main_kb_code = '''from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

calculate_bt = KeyboardButton("")
make_excel_bt = KeyboardButton("")
bot_settings_bt = KeyboardButton("")

menu_bt = KeyboardButton("↩MENU")
start_bt = KeyboardButton("/start")

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu = ReplyKeyboardMarkup(resize_keyboard=True)
start_button = ReplyKeyboardMarkup(resize_keyboard=True)

main_menu.add(calculate_bt,bot_settings_bt)
menu.add(menu_bt)
start_button.add(start_bt)'''

        with open(os.path.join(folder_name,'keyboards', 'main_kb.py'), 'w', encoding='utf-8') as file:
            file.write(main_kb_code)

        init_for_keyboards_code = '''from keyboards.main_kb import main_menu,menu'''

        with open(os.path.join(folder_name,'keyboards', '__init__.py'), 'w') as file:
            file.write(init_for_keyboards_code)

        print("Внутренние папки и файлы успешно созданы.")
    except FileExistsError:
        print(f"Папка '{folder_name}' уже существует.")

if __name__ == '__main__':
    folder_name = input("Введите имя папки: ")
    create_folders(folder_name)