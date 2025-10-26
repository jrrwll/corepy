from datetime import datetime, timedelta, timezone
from typing import Literal

import jwt
from jwt.exceptions import InvalidTokenError
from pydantic import BaseModel, ValidationError


class JwtPayload(BaseModel):
    exp: datetime # expired at
    sub: str # subject


class JwtProvider:

    def __init__(self, private_key: str, public_key: str,
            algorithm: Literal["RS256", "HS256"] = "RS256"):
        self.private_key = private_key
        self.public_key = public_key
        self.algorithm = algorithm

    def create_access_token(
            self, subject: str,
            expire_delta: timedelta) -> str:
        expire = datetime.now(timezone.utc) + expire_delta
        payload = JwtPayload(exp=expire, sub=subject)
        return self.encode_access_token(payload)

    def encode_access_token(self, payload: JwtPayload) -> str:
        return jwt.encode(
            payload.model_dump(exclude_none=True),
            self.private_key,
            algorithm=self.algorithm)

    def decode_access_token(self, token: str) -> JwtPayload | None:
        try:
            payload = jwt.decode(
                token, self.public_key,
                algorithms=[self.algorithm]
            )
            return JwtPayload(**payload)
        except (InvalidTokenError, ValidationError) as e:
            return None
