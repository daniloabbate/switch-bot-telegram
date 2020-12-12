#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import argparse
from switchbotpy import Bot

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
globalConfig = None

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    user = update.message.chat.first_name
    update.message.reply_text("Ciao " + user)
    print("Connection from user: " + user)


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    response_message = "Ciao " + update.message.chat.first_name + " : " + update.message.text
    update.message.reply_text(response_message) # 'Ciao %s. %s' , update.message.chat.first_name, update.message.text)


def apri_portone(update, context):
    """setup switchbot""" 
    username = update.message.chat.first_name
        
    reply_message = "Apro il portone per te, " + username + "..."
    update.message.reply_text(reply_message) # 'Apro il portone per te...')
    """Configure SwitchBot """
    configureAndPressSwitchBot()
    """Call switchbot to push the botton... and hence open the entrance"""
    update.message.reply_text('Portone aperto!') 
    

def configureAndPressSwitchBot(): 
    global globalConfig
    # initialize bot
    logger.debug('Setting up Switchbot')
    bot = Bot(bot_id=0, mac=globalConfig.mac, name="bot0")
    if globalConfig.password:
        bot.encrypted(password=globalConfig.password)

    # execute press command
    bot.press()

     
def main():
    global globalConfig
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary

    parser = argparse.ArgumentParser()
    parser.add_argument("--token", help="Telegram bot token")
    parser.add_argument("--mac", help="mac address of switchbot")
    parser.add_argument("--password", help="password of switchbot")
    args = parser.parse_args()
    token = mac = password = ""
    if not args.mac or args.mac == "" or not args.password or args.password == "" or not args.token or args.token == "":
        logger.error("Please provide all args: Telegram Token AND Switch-bot MAC Address AND Switch-bot Password")
        sys.exit(1)
    else:
        globalConfig = args
        token = args.token
        mac = args.mac
        password = args.password
        logger.info('Token: %s, MAC: %s, Paasword: %s', globalConfig.token, globalConfig.mac, globalConfig.password)
       
    updater = Updater(token=globalConfig.token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("apriportone", apri_portone))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    logger.info('starting up')
    main()
