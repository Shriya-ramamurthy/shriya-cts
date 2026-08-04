from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Docker is Working Successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


    docker build -t myapp .
docker run -p 5000:5000 myapp