def handle_response(message) -> str:
    input_message = message.lower()

    if input_message == "hello":
        return "hey bro"

    if input_message == "dance for me":
        return "https://tenor.com/view/happy-dance-dance-moves-groove-cute-gif-17919727"

    if input_message == "!help":
        return_string = "Here are a list of commands I currently hold." \
                        "hello, dance for me, !help"
        return return_string

    return ""
