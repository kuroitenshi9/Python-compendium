'''
Napisz kod funkcji, która sprawdzi czy email znajduje się na liście
i zwróci True/False
'''
# myemailbook = ["ewa@wp.pl", "tega@wp.pl", "mima@p.pl"]

# def email_search():
#     email = input("Check if e-mail is in your address book: ")
#     print(x)
#     if email in myemailbook:
#         return "True"
#     else:
#         return "False"

# print(email_search())

def find_email(searched, emails):
    for e in emails:
        if e == searched: # porownanie czy istnieje
            return "Znaleziono"
        else:
            continue
        return "Email nie występuje"

with open('emails.txt as file')


