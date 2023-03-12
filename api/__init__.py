from fastapi import FastAPI
from common import add_custom_errors, handle_cors, decryptor_middleware


def create_app():
    app = FastAPI()
    add_custom_errors(app)
    handle_cors(app)
    decryptor_middleware(app)
    return app
