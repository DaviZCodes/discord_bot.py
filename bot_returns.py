import random

# joke command which returns a random joke
joke1 = "9 + 10 = 21"
joke2 = "Whatever"
joke3 = "I am a smart bot"
jokes_list = [joke1, joke2, joke3]


def handle_response(message) -> str:
    input_message = message.lower()

    if input_message == "hello":
        return "hey bro"

    if input_message == "dance for me":
        return "https://tenor.com/view/happy-dance-dance-moves-groove-cute-gif-17919727"

    if input_message == "help":
        return_string = "Here are a list of commands I currently hold. " \
                        "!help, !fart, !joke"
        return return_string

    if input_message == "fart":
        return "https://tenor.com/view/love-fart-lovefart-you-gif-22670000"

    if input_message == "joke":
        random_number = random.randint(0, 2)
        return jokes_list[random_number]

    return ""
