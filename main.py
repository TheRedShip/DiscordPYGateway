from Gateway import Gateway

gateway = Gateway()

def on_message(message):
	print(f"{gateway.client.username} a ecrit {message.content}")

def on_voice_update(update):
	if (update.member.user.username != gateway.client.username):
		return
	print(gateway.guilds.get(update.guild_id))
		
if __name__ == "__main__":
	gateway.on("MESSAGE_CREATE", on_message)
	gateway.on("VOICE_STATE_UPDATE", on_voice_update)
	gateway.start()