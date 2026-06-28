import re

def fun(s):
    return bool(re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', s))

def filter_mail(emails):
    return list(filter(fun, emails))

n = int(input())
emails = [input() for _ in range(n)]
print(sorted(filter_mail(emails)))