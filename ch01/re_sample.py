import re
from typing import Pattern

data = """
홍길동의 주민번호는 800905-1049118 입니다. 
그리고 고길동의 주민번호는 700905-0059119 입니다.
그렇다면 누가 나이가 많을까요?
"""

pat = re.compile("(\d{6})[-](\d{1})\d{6}")
print(pat.sub("\g<1>-\g<2>******", data))

