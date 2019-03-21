import re

before_num = ["010-7499-8045","01056532928","010-38473828","010-2233-3423","010-4038-3948", "017-277-8800"]
basic = "(\d{3})\D?\d{3,4}\D?(\d{4})"
purified_num = []
for pNum in before_num:
    flag = len(re.findall('\d', pNum))
    if flag == 10:
        purified_num.append(re.sub(basic, "\\1-***-\\2", pNum))
    else:
        purified_num.append(re.sub(basic, "\\1-****-\\2", pNum)) # \1 == g<1>   -> \\1       \g<1>
print(purified_num)
    