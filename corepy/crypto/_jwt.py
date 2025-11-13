from datetime import datetime, timedelta, timezone
from typing import Literal

import jwt
from jwt.exceptions import InvalidTokenError
from pydantic import BaseModel, Field, ValidationError


# https://datatracker.ietf.org/doc/html/rfc7519
class JwtPayload(BaseModel):
    subject: str = Field(alias="sub")
    expired_at: datetime = Field(alias="exp")


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
        payload = JwtPayload(subject=subject, expired_at=expire)
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
