from constant import OP_HEARTBEAT_SEND
import json
import time

def ws_heartbeat(ws, interval):
	payload = {
		"op": OP_HEARTBEAT_SEND,
		"d": "None"
	}
	while True:
		time.sleep(interval / 1000)
		ws.send(json.dumps(payload))
		print("Heartbeat sent")