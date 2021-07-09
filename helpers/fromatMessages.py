from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from utils.Logger import *
from utils.Config import Config

Config = Config()


def getMessage(message, action):
    try:
        ALLOWED_CHAT_TYPES = config.get("ALLOWED_CHAT_TYPES")

        if action == "private-chat":
            send_message = f"**Hey 👋 {message.chat.first_name if hasattr(message.chat, 'first_name') else 'User'}**"
            send_message = send_message + \
                f"\n\n**Zer0Byte Music 3.0 Beta]({config.get('BOT_URL')})** is a [Zer0Byte Project](t.me/Zer0ByteOfficial)."
            send_message = send_message + \
                f"\nZer0Byte 2.0 is a project designed for play music in your **group's voice Chat**, as simple as possible"

            send_message = send_message + \
                f"\n\n**This is not fully developed its still on testing!**\n\n**Source Code :** [Repository](https://telegra.ph/file/6d661cc458396796f4692.jpg)"
            return send_message, getReplyKeyBoard(message, action)

        elif action == "help-msg":
            helpMessage = f"**Zer0Byte Music beta**\n**Source Code :** [Repository](https://telegra.ph/file/6d661cc458396796f4692.jpg)"
            helpMessage = helpMessage + \
                f"\n\n• **/play song name/song url : ** __Start a song / add to queue.__"
            helpMessage = helpMessage + f"\n• **/skip : ** __Skip to the next song in queue.__"
            helpMessage = helpMessage + f"\n• **/stop : ** __Stop the playback.__"
            helpMessage = helpMessage + \
                f"\n• **/refreshadmins : ** __Refreshes the admin list.__"
            helpMessage = helpMessage + \
                f"\n• **/auth : ** __Adds the user in reply to the message as admin.__"
            helpMessage = helpMessage + \
                f"\n• **/unauth : ** __Removes the user in reply to the message as admin.__"
            helpMessage = helpMessage + \
                f"\n• **/listadmins : ** __Lists the users assigned as admins for the bot.__"
            helpMessage = helpMessage + \
                f"\n• **/adminmode on|off : ** __Turning this on makes the bot actions available only to bot admins.__"
            helpMessage = helpMessage + \
                f"\n• **/loop [2-5]|off : ** __Loop the playback [x] times(x is between 2-5) / Turn off the loop playback.__"
            helpMessage = helpMessage + f"\n\n**__For any issues contact @Zer0ByteSupport**"
            return helpMessage, getReplyKeyBoard(message, action)

        elif action == "chat-not-allowed":
            send_message = f"**Sorry but this chat is not yet allowed to access the service. You can always check the demo in [Support Group](https://t.me/Zer0ByteSupport).**"
            send_message = send_message + \
                f"\n\n**Why ❓**\n- __Due to high usage we have restrcited the usage of the bot in just our [Support Group](https://t.me/Zer0ByteSupport) __"
            send_message = send_message + \
                f"\n- __Join the [Support Group](https://t.me/Zer0ByteSupport) to access the bot or deploy your own bot __ **Source Code :** [Github](https://telegra.ph/file/6d661cc458396796f4692.jpg)"

            return send_message, getReplyKeyBoard(message, action)

        elif action == "start-voice-chat":
            send_message = f"**Please start a voice chat and then send the command again**"
            send_message = send_message + \
                f"\n**1.** __To start a group chat, you can head over to your group’s description page.__"
            send_message = send_message + \
                f"\n**2.** __Then tap the three-dot button next to Mute and Search start a Voice Chat.__"
            return send_message, getReplyKeyBoard(message, action)

    except Exception as ex:
        logException(f"**__Error : {ex}__**", True)


def getReplyKeyBoard(message, action):
    try:
        if action == "private-chat":
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "➕ Add Zer0Byte Music Beta ➕", url=f"{config.get('BOT_URL')}?startgroup=bot"),
                    ],
                    [
                        InlineKeyboardButton(
                            "👥 Support Group", url=f"https://t.me/Zer0ByteOfficial"),

                        InlineKeyboardButton(
                            "🔔 Updates", url=f"https://t.me/Zer0ByteSupport"),
                    ],

                ]
            )
            return keyboard
        elif action == "chat-not-allowed":
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🏁 Use In Demo Group", url=f"https://t.me/Friends_Chatting_Grp"),
                    ],
                    [
                        InlineKeyboardButton(
                            "🗃 Source Code", url=f"https://telegra.ph/file/6d661cc458396796f4692.jpg"),

                    ],

                ]
            )
            return keyboard
        return None
    except Exception as ex:
        logException(f"**__Error : {ex}__**", True)
