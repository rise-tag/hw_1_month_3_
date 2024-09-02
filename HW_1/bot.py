import asyncio
import logging
import random

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from config import TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_bot(message: Message):
    await message.reply("Привет! Я загадал число от 1 до 3, попробуйте его угадать.")


@dp.message(Command("help"))
async def help(message: Message):
    await message.reply("Я могу помочь вам угадать число от 1 до 3. Напишите число, и я скажу, угадали ли вы.")


@dp.message(F.text == "Как дела?")
async def how_are_you(message: Message):
    await message.reply("Хорошо, спасибо!")


@dp.message(F.text.in_({'Привет', 'привет', 'салам'}))
async def greeting(message: Message):
    await message.answer("Привет!")


@dp.message(F.text.in_({'1', '2', '3'}))
async def guess_number(message: Message):
    user_guess = int(message.text)
    random_number = random.randint(1, 3)

    if user_guess == random_number:
        await message.answer_photo(
            photo="https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg",
            caption="Правильно, вы угадали!"
        )
    else:
        await message.answer_photo(
            photo="https://media.makeameme.org/created/sorry-you-lose.jpg",
            caption=f"Неправильно, я загадал {random_number}. Попробуйте снова!"
        )


@dp.message(Command("photo"))
async def send_photo(message: Message):
    await message.answer_photo(
        photo="https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg",
        caption="Вы выиграли!"
    )


@dp.message()
async def echo(message: Message):
    await message.answer("Я вас не понял, попробуй число от 1 до 3.")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
