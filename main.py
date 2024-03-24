from Gateway import Gateway
import os

gateway = Gateway(os.getenv("token"))

def on_message(message):
	if message.content == "!redping":
		gateway.users.get(message.author.id).send("Pong!")

if __name__ == "__main__":
	gateway.on("MESSAGE_CREATE", on_message)
	gateway.start()
