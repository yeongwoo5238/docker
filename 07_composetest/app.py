import os
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", "6379")),
)

@app.route("/")                   # http://localhost/
def hello():
    count = cache.incr("hits")
    return f"Code changed - Hello from Docker! I have been seen {count} time(s).\n"
