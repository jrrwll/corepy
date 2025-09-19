from corepy.expression import eval_code, eval_main_func

corrected_code = """
def main(arg1: str) -> list[str]:
    body_obj = json_loads(arg1)
    if isinstance(body_obj, dict):
        return [model['name'] for model in body_obj['models']]
    else:
        return body_obj
"""

arg1 = '{"models": [{"name": "Model1"}, {"name": "Model2"}]}'
arg1_not_dict = '["SingleModel"]'


def test_eval_main_func():
    print(f"\narg1: {eval_main_func(corrected_code, arg1)}")

    print(f"\narg1_not_dict: {eval_main_func(corrected_code, arg1_not_dict)}")


def test_eval_code():
    res = eval_code("a > 3 and b is not None", a=4, b=__name__)
    print(f"\nbool expr1: {res}")
    res = eval_code("a > 3 and b is not None", a=10, b=None)
    print(f"\nbool expr2: {res}")

    res = eval_code(f"{corrected_code}\nmain(arg1)", arg1=arg1)
    print(f"\narg1: {res}")

    res = eval_code(f"{corrected_code}\nmain(arg1)", arg1=arg1_not_dict)
    print(f"\narg1_not_dict: {res}")
