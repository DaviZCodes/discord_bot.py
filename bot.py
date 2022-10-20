# main file for the discord bot
# import discord and bot_returns.py
import discord
import bot_returns


# bot send message using bot_returns function
async def send_message(message, user_message, is_private):
    try:
        bot_response = bot_returns.handle_response(user_message)
        if is_private:
            await message.author.send(bot_response)
        else:
            await message.channel.send(bot_response)

    except Exception as e:
        print(e)


def run_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    token = "MTAzMTA2ODU1NjUxMjcyNzEyMw.GEOtkL.gd_xJfr84g00V2Byuohea_FTwz1sENbnEOYZTY"  # this token doesn't work due to privacy reasons
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready(): # I have to use on_ready as function name because it is on discord.py library
        print(f"{client.user} is running!")

    @client.event
    async def on_message(message):  # I have to use function name on_message because it is part of discord.py library
        if message.author == client.user:
            return

        # dividing each message to three parts:
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} " said " {user_message} in the channel: {channel}')  # printing what user says to console

        if user_message[0] == "!":
            # exclude the first two characters
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(token)
