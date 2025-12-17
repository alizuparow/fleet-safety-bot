import asyncio
from aiogram import Bot
from config import BOT_TOKEN, COMPANY_CHAT_ID

bot = Bot(token=BOT_TOKEN)

async def send_daily_digest():
    message = (
        "📊 <b>Daily Safety Digest</b>\n\n"
        "Company: Company X\n\n"
        "🚚 Total Units: 10\n"
        "📈 Incidents: 3\n\n"
        "📋 Action Items:\n"
        "• Daily report test (GitHub Actions)"
    )

    await bot.send_message(
        chat_id=COMPANY_CHAT_ID,
        text=message,
        parse_mode="HTML"
    )

async def main():
    try:
        await send_daily_digest()
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
