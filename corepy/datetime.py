from datetime import datetime


def format_date(d: datetime = datetime.now()) -> str:
    return d.strftime('%Y-%m-%d')


def format_date_compact(d: datetime = datetime.now()) -> str:
    return d.strftime('%Y%m%d')


def isoformat_dict(d: dict) -> None: # type: ignore[type-arg]
    for k, v in d.items():
        if isinstance(v, datetime):
            d[k] = v.isoformat()
        elif isinstance(v, dict):
            isoformat_dict(v)
        elif isinstance(v, list):
            new_list = []
            for i in v:
                if isinstance(i, datetime):
                    i = i.isoformat()
                elif isinstance(i, dict):
                    isoformat_dict(i)
                new_list.append(i)
