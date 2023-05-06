import traceback

import helpers
from config import AppConfigValues
from helpers import logger

import json
import hashlib
import requests

from common import ResponseMessagesValues
from fastapi.responses import JSONResponse
from starlette.requests import Message
from fastapi import FastAPI, Request
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken


def decryptor_middleware(app: FastAPI):
    @app.middleware("http")
    async def decrypt_body(request: Request, call_next):
        method_logger = logger.global_logger.getChild("decrypt_body")
        scope = request.scope
        send = request._send
        # Receive the entire request body using request.stream()
        body = b""
        new_bytes_body = b''
        async for chunk in request.stream():
            body += chunk
        if body:
            raw_json_body = json.loads(body)
            clean_json_body = dict(filter(lambda kv: kv[0] not in ["hash"], json.loads(body).items()))
            try:
                fernet = Fernet(AppConfigValues.ENCRYPTION_KEY_SECRET.encode())
                if fernet.decrypt(raw_json_body.get('hash')).decode() != helpers.get_hash(clean_json_body):
                    return JSONResponse(status_code=403,
                                        content={"error": ResponseMessagesValues.NO_MATCHING_HATCH})
            except (InvalidToken, ValueError):
                method_logger.error(traceback.format_exc())
                return JSONResponse(status_code=401,
                                    content={"error": ResponseMessagesValues.INVALID_ENCRYPTION_KEY})
            except:
                method_logger.error(traceback.format_exc())
                return JSONResponse(status_code=400,
                                    content={"error": ResponseMessagesValues.GENERAL_ENCRYPTION_ERROR_MSG})
            new_bytes_body = json.dumps(clean_json_body).encode()

        async def new_receive() -> Message:
            return {"type": "http.request", "body": new_bytes_body}

        request = Request(scope, new_receive, send)

        if scope.get("path") not in ["/", "/docs", "/openapi.json", "/health/", "/health"]:
            method = request.method
            headers = request.headers
            body = await request.body()
            body = json.loads(body or "{}") or None
            query_params = request.query_params
            micro_url = f"{AppConfigValues.MICRO_SERVICE_URL}{scope.get('path')}"
            try:
                response: requests.Response = requests.request(method,
                                                               micro_url,
                                                               headers=dict(headers.items()),
                                                               params=tuple(query_params.items()),
                                                               json=body)
                return JSONResponse(status_code=response.status_code,
                                    content=response.json() if response.content else None)
            except:
                method_logger.error(traceback.format_exc())
                return JSONResponse(status_code=503,
                                    content={"error": ResponseMessagesValues.GENERAL_REQUESTS_FAILURE_MESSAGE})
        else:
            response = await call_next(request)
            return response
