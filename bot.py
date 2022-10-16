import discord
import bot_returns


async def send_message(message, user_message, is_private):
    try:
        bot_response = bot_returns.handle_response(user_message)
        if is_private:
            await message.author.send(bot_response)
        else:
            await message.channel.send(bot_response)
    except Exception as wrong:
        print(wrong)


def run_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    token = "MTAzMTA2ODU1NjUxMjcyNzEyMw.GfKJEw.z2_xag-fOXLyjbvXce_xIF6xwxE3h6lP2NOOMA"
    client = discord.Client(intents = intents)

    @client.event
    async def bot_on():
        print(f"{client.user} is running!")

    @client.event
    async def message_response(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(username + " said " + user_message + " in " + channel)

        if message[0:2] == "dm":
            # exclude the first two characters

            message = message[2:]
            await send_message(message, user_message, is_private= True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(token)