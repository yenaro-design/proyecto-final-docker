
import os
import time

from flask import Flask, jsonify, request, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Identificador de cada instancia del backend
INSTANCE = os.getenv("INSTANCE_ID", "Backend sin identificar")

# Contador de solicitudes recibidas
REQUEST_COUNT = Counter(
    "backend_requests_total",
    "Total de solicitudes recibidas por el backend",
    ["instance", "method", "endpoint", "status"]
)

# Medidor del tiempo de respuesta
REQUEST_LATENCY = Histogram(
    "backend_request_duration_seconds",
    "Tiempo de respuesta de las solicitudes del backend",
    ["instance", "method", "endpoint"]
)


# Registrar el momento en que comienza cada solicitud
@app.before_request
def start_timer():
    request.start_time = time.time()


# Registrar las métricas al finalizar cada solicitud
@app.after_request
def record_metrics(response):
    if request.path != "/metrics":
        duration = time.time() - request.start_time

        REQUEST_COUNT.labels(
            INSTANCE,
            request.method,
            request.path,
            str(response.status_code)
        ).inc()

        REQUEST_LATENCY.labels(
            INSTANCE,
            request.method,
            request.path
        ).observe(duration)

    return response


# Página principal
@app.route("/")
def home():
    return jsonify({
        "mensaje": "Backend funcionando correctamente",
        "instancia": INSTANCE,
        "estado": "OK"
    })


# Endpoint para comprobar el estado del backend
@app.route("/health")
def health():
    return jsonify({
        "estado": "saludable",
        "instancia": INSTANCE
    })


# Endpoint para entregar métricas a Prometheus
@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
