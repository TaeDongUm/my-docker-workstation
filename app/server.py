from pathlib import Path

from flask import Flask, render_template

from counter import increment_count, read_count

BASE_DIR = Path(__file__).resolve().parent.parent

app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static"),
)


@app.route("/")
def index():
    count = increment_count()
    return render_template("index.html", count=count)


@app.route("/health")
def health():
    count = read_count()
    return render_template("health.html", count=count)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)