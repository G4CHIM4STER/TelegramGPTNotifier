import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

bot = Bot(token='6596637011:AAGimhzJEToQKuffxdsfV8n9ZCrajEHFkNg')

dp = Dispatcher()
#asdasd
# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message : types.Message):
    await message.answer("Hello")
    
@dp.message(Command("test1"))
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")
    
# Хэндлер на команду /test2
async def cmd_test2(message: types.Message):
    await message.reply("Test 2")

@dp.message(Command("answer"))
async def cmd_answer(message: types.Message):
    await message.answer("Это простой ответ")


@dp.message(Command("reply"))
async def cmd_reply(message: types.Message):
    await message.reply('Это ответ с "ответом"')
    
@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")    

#! Не работает !

# mylist = [1,2,3]

# @dp.message(Command("add_to_list"))
# async def cmd_add_to_list(message: types.Message, mylist: list[int]):
#     mylist.append(7)
#     await message.answer("Добавлено значение 7")
    
# @dp.message(Command("show_list"))
# async def cmd_show_list(message: types.Message, mylist: list[int]):
#     await message.answer(f"Ваш список: {mylist}")

async def main():
    await dp.start_polling(bot)
    
# Хэндлер на команду /test1
    
if __name__ == "__main__":
    # Где-то в другом месте, например, в функции main():
    dp.message.register(cmd_test2, Command("test2"))
    asyncio.run(main())