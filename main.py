from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from getnew import getnew

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    titles = getnew()
    for title, link in titles:
        await update.message.reply_text(f'{title}\n{link}')

app = ApplicationBuilder().token("7323666787:AAHiV1OXoFY8BKUvqNmRE1A2KGbf5ZoP6GU").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("news", news))

app.run_polling()
