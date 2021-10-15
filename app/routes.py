from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)

# Flask Hello lesson - Endpoint 1 
@hello_world_bp.route("/hello-world", methods=["GET"])
def hello_world():
    response = "hello world!"
    return response

@hello_world_bp.route("/hello/JSON", methods=["GET"])
def say_hello_json():
    return {
        "name": "Duke Cabebe",
        "message": "Hello!",
        "interests": ["barking", "chasing squirrels", "interrupting zoom calls", "being adorable"]
    }

@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)
    return response_body