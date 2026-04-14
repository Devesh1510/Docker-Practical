from flask import Flask
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Devesh's CI/CD Pipeline!"

# Expose Prometheus metrics at /metrics
metrics_app = make_wsgi_app()
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': metrics_app
})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)