from flask import Flask
import time, random
from prometheus_client import Counter, Histogram, generate_latest

app = Flask(__name__)

REQUESTS = Counter("http_requests_total", "Total HTTP requests")
LATENCY = Histogram("http_request_latency_seconds", "Latency")

@app.route("/")
def home():
    REQUESTS.inc()
    with LATENCY.time():
        time.sleep(random.uniform(0.1, 1.5))
    return "FleetOps service running\n"

@app.route("/metrics")
def metrics():
    return generate_latest()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
