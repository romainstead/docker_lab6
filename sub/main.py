import json
import redis
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

r = redis.Redis(host='redis', port=6379, decode_responses=True)
p = r.pubsub()


class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")


def run_health_server():
    server = HTTPServer(('0.0.0.0', 8080), HealthCheckHandler)
    server.serve_forever()


threading.Thread(target=run_health_server, daemon=True).start()


def message_handler(message):
    if message['type'] == 'message':
        print(f"Новый заказ: {json.loads(message['data'])}", flush=True)


p.subscribe(**{'order_notifications': message_handler})

print("Подписан на топик order_notifications. Ожидание сообщений...")

try:
    for message in p.listen():
        pass
except KeyboardInterrupt:
    p.unsubscribe()
    r.close()
