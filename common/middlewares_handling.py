import traceback

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
        receive = await request._receive()
        send = request._send
        if bytes_body := receive.get("body"):
            raw_json_body = json.loads(bytes_body)
            clean_json_body = dict(filter(lambda kv: kv[0] not in ["hash"], json.loads(bytes_body).items()))
            try:
                fernet = Fernet(AppConfigValues.ENCRYPTION_KEY_SECRET.encode())
                if not fernet.decrypt(raw_json_body.get('hash')).decode() == hashlib.md5(
                        json.dumps(clean_json_body, separators=(",", ":"), sort_keys=True,
                                   ensure_ascii=False).encode()).hexdigest():
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
            receive["body"] = new_bytes_body

        async def new_receive() -> Message:
            return receive

        request = Request(scope, new_receive, send)
        if scope.get("path") not in ["/", "/docs", "/openapi.json", "/health/", "/health"]:
            method = request.method
            headers = request.headers
            body = await request.json()
            query_params = request.query_params
            micro_url = f"{AppConfigValues.MICRO_SERVICE_URL}{scope.get('path')}"
            try:
                response: requests.Response = requests.request(method,
                                                               micro_url,
                                                               headers=dict(headers.items()),
                                                               params=tuple(query_params.items()),
                                                               data=body)
                return JSONResponse(status_code=response.status_code, content=response.json())
            except:
                method_logger.error(traceback.format_exc())
                return JSONResponse(status_code=503,
                                    content={"error": ResponseMessagesValues.GENERAL_REQUESTS_FAILURE_MESSAGE})
        else:
            response = await call_next(request)
            return response
