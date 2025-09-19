import json
from typing import Any, Dict, Literal, Tuple, Type

from pydantic import BaseModel, Field, ValidationError, create_model
from pydantic.fields import FieldInfo
from pydantic_core import ErrorDetails


def create_model_type(  # type: ignore[no-untyped-def]
        model_name: str,
        fields: Dict[str, Tuple[Type[Any], Dict[str, Any] | FieldInfo]],
        base: Type[BaseModel] = BaseModel,
        **kwargs
) -> Type[BaseModel]:
    field_definitions = {}
    for field_name, (field_type, field_config) in fields.items():
        if isinstance(field_config, dict):
            field_config = Field(**field_config)
        field_definitions[field_name] = (field_type, field_config)

    return create_model(  # type: ignore[no-any-return]
        model_name,
        __base__=base,
        **field_definitions,
        **kwargs
    )


def dump_json(a: Any):
    if isinstance(a, BaseModel):
        return json.dumps(a.model_dump(), ensure_ascii=False)
    else:
        return json.dumps(a, ensure_ascii=False)


# {"a": "{}", "b": "[]"} -> {"a": BaseModel, "b": []}
def load_and_update_dict(d: dict[str, Any],
        *keys: str, **model_classes: type[BaseModel]) -> None:
    new_dict = {}
    for key in keys:
        if key in d:
            new_dict[key] = json.loads(d[key])

    for key, model_cls in model_classes.items():
        if key in d:
            new_dict[key] = model_cls.model_validate_json(d[key])

    d.update(new_dict)


# {"a": [1]} -> {"a": "[1]"}
def dump_and_update_dict(d: dict[str, Any], *keys: str) -> None:
    new_dict = {}
    for key in keys:
        if key in d:
            new_dict[key] = dump_json(d[key])
    d.update(new_dict)


def model_validate_dict[T: BaseModel](
        raw_dict: dict[str, dict[str, dict]], model: type[T]
) -> dict[str, dict[str, T]]:
    new_dict = {}
    for k1, d in raw_dict.items():
        new_d = {}
        for k2, v in d.items():
            new_d[k2] = model.model_validate(v)
        new_dict[k1] = new_d

    return new_dict


def extract_validation_error(
        e: ValidationError
) -> dict[Literal["missing_fields", "invalid_fields"], list[str]]:
    missing_fields, invalid_fields = [], []
    for err in e.errors():
        loc = err.get("loc", [])
        if err.get("type") == "missing":
            missing_fields.extend(loc)
        else:
            invalid_fields.extend(loc)

    return {
        "missing_fields": missing_fields,
        "invalid_fields": invalid_fields,
    }


def new_validation_error(instance: BaseModel,
        missing_fields: list[str] | None = None,
        invalid_fields: list[str] | None = None) -> ValidationError:
    line_errors = []
    if missing_fields:
        line_errors.append(ErrorDetails(
            type="missing", loc=tuple(missing_fields),
            input=instance, msg="Field required"))

    if invalid_fields:
        line_errors.append(ErrorDetails(
            type="value_error", loc=tuple(invalid_fields),
            input=instance, msg="Value error"))

    return ValidationError.from_exception_data(
        title=type(instance).__name__,
        line_errors=line_errors
    )


def get_extra_schema(model_cls: type[BaseModel]) -> dict[str, dict[str, Any]]:
    fields = {}
    for field_name, field_info in model_cls.model_fields.items():
        json_schema_extra = field_info.json_schema_extra
        if json_schema_extra and isinstance(json_schema_extra, dict):
            fields[field_name] = json_schema_extra

    return fields
