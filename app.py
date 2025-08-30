from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route("/proxy")
def proxy():
    url = request.args.get("url")
    if not url:
        return "Passe uma URL ?url=https://site.com", 400

    # Faz a requisição externa
    resp = requests.get(url, stream=True)

    # Monta a resposta com headers originais (importante p/ vídeos, etc)
    excluded_headers = ["content-encoding", "transfer-encoding", "connection"]
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    return Response(resp.content, resp.status_code, headers)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
