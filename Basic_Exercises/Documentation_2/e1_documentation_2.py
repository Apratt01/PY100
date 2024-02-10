name = "Victor"
profession = "programmer"

print("Hello, " + name + ". You are a " + profession + ".")

print(f"Hello, {name}. You are a {profession}.")


message_format = "Hello, {}. You are a {}."
formatted_message = message_format.format(name, profession)
print(formatted_message)
# Hello, Victor. You are a programmer.