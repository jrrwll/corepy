from typing import Optional, Union

from pydantic import BaseModel, JsonValue


class ApiResult[T: BaseModel | JsonValue | None](BaseModel):
    err_code: str = 'ok'
    err_args: Optional[dict[str, Union[str, int, list[str], list[int]]]] = None
    data: T = None

    @classmethod
    def ok[R: BaseModel | JsonValue | None](cls, data: R = None) -> "ApiResult[R]":
        return cls(data=data)

    @classmethod
    def error[R: BaseModel | JsonValue | None](cls, e: str | Exception) -> "ApiResult[R]":
        return cls(err_code='err', err_args=dict(msg=f"{e}"))


class IdResult(BaseModel):
    id: int | str


class ListResult[T: BaseModel | JsonValue](BaseModel):
    items: list[T]

    @classmethod
    def create[R: BaseModel | JsonValue](cls, data: list[R]) -> "ListResult[R]":
        return ListResult(items=data)


# PEP 695 Generic Bounds
class PageResult[T: BaseModel | JsonValue](BaseModel):
    page_no: int
    page_size: int
    total: int
    items: list[T]
