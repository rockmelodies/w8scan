# E-mail搜索
def run(url='',body=''):
    pattern = re.compile(r'([\w-]+@[\w-]+\.[\w-]+)+')
    email_list = re.findall(pattern, body)
    if (email_list):
        for email in email_list:
            print email
            report.add_list("E-mail",email)
        return True
    return False