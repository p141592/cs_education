#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.application import logging
from core.settings import BOT_TOKEN

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler


logger = logging.getLogger(__name__)

GENDER, PHOTO, LOCATION, BIO = range(4)


def start(update, context):
    reply_keyboard = [["Boy", "Girl", "Other"]]

    update.message.reply_text(
        "Hi! My name is Professor Bot. I will hold a conversation with you. " "Send /cancel to stop talking to me.\n\n" "Are you a boy or a girl?",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return GENDER


def gender(update, context):
    user = update.message.from_user
    logger.info("Gender of %s: %s", user.first_name, update.message.text)
    update.message.reply_text(
        "I see! Please send me a photo of yourself, " "so I know what you look like, or send /skip if you don't want to.", reply_markup=ReplyKeyboardRemove()
    )

    return PHOTO


def photo(update, context):
    user = update.message.from_user
    photo_file = update.message.photo[-1].get_file()
    photo_file.download("user_photo.jpg")
    logger.info("Photo of %s: %s", user.first_name, "user_photo.jpg")
    update.message.reply_text("Gorgeous! Now, send me your location please, " "or send /skip if you don't want to.")

    return LOCATION


def skip_photo(update, context):
    user = update.message.from_user
    logger.info("User %s did not send a photo.", user.first_name)
    update.message.reply_text("I bet you look great! Now, send me your location please, " "or send /skip.")

    return LOCATION


def location(update, context):
    user = update.message.from_user
    user_location = update.message.location
    logger.info("Location of %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude)
    update.message.reply_text("Maybe I can visit you sometime! " "At last, tell me something about yourself.")

    return BIO


def skip_location(update, context):
    user = update.message.from_user
    logger.info("User %s did not send a location.", user.first_name)
    update.message.reply_text("You seem a bit paranoid! " "At last, tell me something about yourself.")

    return BIO


def bio(update, context):
    user = update.message.from_user
    logger.info("Bio of %s: %s", user.first_name, update.message.text)
    update.message.reply_text("Thank you! I hope we can talk again some day.")

    return ConversationHandler.END


def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text("Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            GENDER: [MessageHandler(Filters.regex("^(Boy|Girl|Other)$"), gender)],
            PHOTO: [MessageHandler(Filters.photo, photo), CommandHandler("skip", skip_photo)],
            LOCATION: [MessageHandler(Filters.location, location), CommandHandler("skip", skip_location)],
            BIO: [MessageHandler(Filters.text, bio)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    dp.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
