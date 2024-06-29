from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader

from config import API_KEY, security

api_key_query = APIKeyHeader(name="api-key", auto_error=False)


def get_api_key(api_key: str = Security(api_key_query)) -> str:
    if security:
        if api_key == API_KEY:
            return api_key
        raise HTTPException(status_code=401, detail="Error 401: Unauthorized")
