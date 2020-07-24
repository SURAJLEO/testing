# Dependencies
from flask import Flask, request

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def print_square():
    print("inside the predict func")
    recieved_value = int(request.get_json(force=True))
    ### load the poickle ,h5 file 
    print(recieved_value)
    return str(recieved_value**2)

if __name__ == "__main__":
    app.run()