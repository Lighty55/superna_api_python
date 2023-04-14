import logging
from flask import Response, Flask, render_template
import jobv2_readiness_get

app = Flask(__name__)

# refresh and display new entries
@app.after_request
def adding_header_content(head):
    head.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    head.headers["Pragma"] = "no-cache"
    head.headers["Expires"] = "0"
    head.headers['Cache-Control'] = 'public, max-age=0'
    return head

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/metrics")
def response_metrics_data():
    jobv2_readiness_get.parse_metrics()
    metrics = jobv2_readiness_get.get_metrics()
    return Response(
        metrics,
        headers={"Content-Type": "text/plain"}
    )

if __name__ == '__main__':
    logging.basicConfig(filename='error.log',level=logging.DEBUG)
    app.run(host='0.0.0.0', port=9988, use_reloader=True)
