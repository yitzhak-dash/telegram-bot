from telegram.ext import Updater, JobQueue

token = '218769106:AAExu45VK1hxju5yKAt0YutT5exHD-WaEWk'

updater = Updater(token=token)
dispatcher = updater.dispatcher

budget = 0.0
timers = dict()


def help(bot, update):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id=chat_id, text="I'm your bottle, you can talk to me.")


def say_cool(bot, update, args, job_queue):
    chat_id = update.message.chat_id

    def alarm(bot, job):
        """Inner function to send the alarm message"""
        bot.sendMessage(chat_id, text='Cool!')

    due = 1

    # Add job to queue
    job = JobQueue(alarm, due, repeat=True)
    timers[chat_id] = job
    job_queue.put(job)

    bot.sendMessage(chat_id=chat_id, text=("You are coo, man."))


def echo(bot, update):
    sender_name = update.message.from_user.first_name
    message = 'Hello, %s. You are very cool.' % sender_name
    # bot.sendMessage(chat_id=update.message.chat_id, text="%s says: %s" % (sender_name, update.message.text))
    bot.sendMessage(chat_id=update.message.chat_id, text=message)


def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")


def main():
    dispatcher.addUnknownTelegramCommandHandler(unknown)
    dispatcher.addTelegramCommandHandler('help', help)
    dispatcher.addTelegramCommandHandler('say_cool', say_cool)
    dispatcher.addTelegramMessageHandler(echo)

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
