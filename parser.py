import re

def is_alert(line: str) -> bool:
    return bool(re.search(r'ERROR|WARNING', line))
