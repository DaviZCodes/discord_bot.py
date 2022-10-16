import random


def handle_response(message) -> str:
    input_message = message.lower()

    if input_message == "hello":
        return "hey bro"

    elif input_message == "dance for me":
        return "https://tenor.com/view/happy-dance-dance-moves-groove-cute-gif-17919727"
