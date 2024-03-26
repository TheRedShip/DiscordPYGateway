from Gateway import Gateway
import os

gateway = Gateway(os.getenv("token"))

def on_message(message):
	if (not message.has("guild_id") and message.content == "!getmessages"):
		user = gateway.users.get(message.channel_id)
		last_message_id = user.last_message_id
		for i in range(3):
			messages = user.get_dm_messages(50, last_message_id)
			[print(m.author.username, ":", m.content) for m in messages]
			last_message_id = messages[len(messages) - 1].id


if __name__ == "__main__":
	gateway.on("MESSAGE_CREATE", on_message)
	gateway.start()
