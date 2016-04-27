from telegram.ext import Updater

token = '218769106:AAExu45VK1hxju5yKAt0YutT5exHD-WaEWk'

updater = Updater(token=token)
dispatcher = updater.dispatcher

budget = 0.0


def help(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm your bottle, you can talk to me.")


def add_incoming(bot, update, args):
    num = float(args[0])
    global budget
    budget += num
    bot.sendMessage(chat_id=update.message.chat_id, text=("Your incoming %d were added." % num))
    bot.sendMessage(chat_id=update.message.chat_id, text=("The budget is: %d." % budget))


def add_expenses(bot, update, args):
    num = float(args[0])
    global budget
    budget -= num
    bot.sendMessage(chat_id=update.message.chat_id, text=("Your expenses %d were added." % num))
    bot.sendMessage(chat_id=update.message.chat_id, text=("The budget is: %d." % budget))


def echo(bot, update):
    sender_name = update.message.from_user.first_name
    message = 'Good morning, %s' % sender_name
    # bot.sendMessage(chat_id=update.message.chat_id, text="%s says: %s" % (sender_name, update.message.text))
    bot.sendMessage(chat_id=update.message.chat_id, text=message)


def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")


def main():
    dispatcher.addUnknownTelegramCommandHandler(unknown)
    dispatcher.addTelegramCommandHandler('help', help)
    dispatcher.addTelegramCommandHandler('add_incoming', add_incoming)
    dispatcher.addTelegramCommandHandler('add_expenses', add_expenses)
    dispatcher.addTelegramMessageHandler(echo)

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
