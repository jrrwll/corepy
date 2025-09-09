import json
from typing import Any
import ast

_safe_globals = {
    "__builtins__": {
        # types
        "str": str,
        "int": int,
        "float": float,
        "list": list,
        "dict": dict,
        "set": set,
        "bool": bool,
        # functions
        "isinstance": isinstance,
        "len": len,
        "sum": sum,
        "max": max,
        "min": min,
    },
    "json_loads": json.loads,
    "json_dumps": json.dumps,
}


# eval main function and return the result
def eval_main_func(code: str, *args, **kwargs) -> Any:  # type: ignore[no-untyped-def]
    safe_locals = {}  # type: ignore[var-annotated]
    exec(code, _safe_globals, safe_locals)

    main_func = safe_locals.get("main")
    if not main_func:
        raise Exception("main func undefined")

    return main_func(*args, **kwargs)


def eval_code(code: str, **kwargs) -> Any:
    """
    :raise NameError if some var is not defined
    """
    mod = ast.parse(code, mode='exec')

    # no statements
    if not mod.body:
        return None

    last_stmt = mod.body.pop()
    if not isinstance(last_stmt, ast.Expr):
        return None

    last = ast.Expression(body=last_stmt.value)

    exec_code = compile(mod, '<string>', 'exec')
    last_code = compile(last,    '<string>', 'eval')

    # local scope
    loc = dict(kwargs)
    exec(exec_code, _safe_globals, loc)

    return eval(last_code, _safe_globals, loc)
