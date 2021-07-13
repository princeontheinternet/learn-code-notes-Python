def get_domain_name(email):
    return email.split('@')[1]


domain = get_domain_name('xyz@gmail.com')
print(domain)