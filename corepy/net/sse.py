import json

from pydantic import BaseModel, JsonValue


async def sse_format(data: BaseModel | JsonValue) -> str:
    if isinstance(data, BaseModel):
        data = data.model_dump()
    return f"data: {json.dumps(data, ensure_ascii=False)}\n\n"
