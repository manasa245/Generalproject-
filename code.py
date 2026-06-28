def fun(s):
    if s.count('@') != 1:
        return False
    
    email_index = s.index('@')
    dot_index = s.rindex('.')
    
    if dot_index < email_index:
        return False
    
    username = s[:email_index]
    website_name = s[email_index+1:dot_index]
    extension = s[dot_index+1:]
    
    if not username or not website_name or not extension:
        return False
    
    if len(extension) > 3:
        return False
    
    for c in username:
        if not (c.isalpha() or c.isdigit() or c == '_' or c == '-'):
            return False
    
    for c in website_name:
        if not (c.isalpha() or c.isdigit()):
            return False
    
    for c in extension:
        if not c.isalpha():
            return False
    
    return True

def filter_mail(emails):
    return list(filter(fun, emails))

n = int(input())
emails = [input() for _ in range(n)]
print(sorted(filter_mail(emails)))