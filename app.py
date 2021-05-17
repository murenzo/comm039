from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    title = "Afeez Aheeb Comm039"
    return render_template("index.html", title=title)


@app.route('/configuration')
def configuration():
    title = "Application Configuration"
    return render_template("configuration.html", title=title)


@app.route('/configure', methods=["POST"])
def configure():
    resource_count = request.form.get("resource_count")
    total_shots = request.form.get("total_shots")
    reporting_rate = request.form.get("reporting_rate")
    matching_digits = request.form.get("matching_digits")
    title = "Thank You"
    return render_template("configure.html", title=title, resource_count=resource_count, total_shots=total_shots, reporting_rate=reporting_rate, matching_digits=matching_digits)
