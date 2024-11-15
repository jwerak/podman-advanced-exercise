from flask import Flask, jsonify
import redis
import signal
import sys

app = Flask(__name__)
cache = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

@app.route('/')
def hello():
    count = cache.incr('hits')
    return jsonify({"message": "Hello from Flask!", "hits": count})

# Function to handle SIGTERM
def handle_sigterm(signal_number, frame):
    print("Received SIGTERM. Shutting down gracefully...")
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGTERM, handle_sigterm)

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(host='0.0.0.0', port=5000)
