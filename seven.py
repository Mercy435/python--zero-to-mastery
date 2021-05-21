class ContactBook:
    name = 'local'

    def __init__(self, id, name, address, phone, email):
        self.id = id
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email


person1 = ContactBook()
print(person1.email)

# contactbook={}
import pandas as pd
df = pd.DataFrame(columns=['id''name', 'address', 'phone', 'email'])
df.to_csv('contact_book.csv', index=False)

