from Gateway import Gateway
import os

gateway = Gateway(os.getenv("token"))

def on_message(message):
	if (message.author.id != gateway.client.id and message.content == "Hey"):
		gateway.guilds.get(message.guild_id).channel(message.channel_id).send(f"Hey {message.author.username}")

if __name__ == "__main__":
	gateway.on("MESSAGE_CREATE", on_message)
	gateway.start()