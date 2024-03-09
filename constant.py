DISCORD_WS_URL		= 'wss://gateway.discord.gg/?v=9&encoding=json'

ALL_INTENTS			= (
	1 << 0 | 1 << 1 | 1 << 2 | 1 << 3 | 1 << 4 | 1 << 5 | 1 << 6 | 1 << 7 | 
	1 << 8 | 1 << 9 | 1 << 10 | 1 << 11 | 1 << 12 | 1 << 13 | 1 << 14 | 
	1 << 15 | 1 << 16 | 1 << 20 | 1 << 21
)

OP_EVENT_DISPATCH	= 0
OP_HEARTBEAT_SEND	= 1
OP_IDENTIFY			= 2
OP_HELLO			= 10