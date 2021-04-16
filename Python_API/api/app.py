from flask import Flask, request

app = Flask(__name__)

@app.route("/showittome", methods = ["POST"])
def data_processor():
    request_data = request.get_json()

    key = request_data['key']
    address = request_data['address']
    fileName = request_data["fileName"]

    print((fileName, address, key))

    return "", 200

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run()
