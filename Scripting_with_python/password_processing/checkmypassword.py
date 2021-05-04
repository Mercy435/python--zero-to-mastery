# requests allows to make a request from a browser
import requests
# to convert password to hash, import the hash module
import hashlib
# give arguments in the terminal
import sys

'''
# password API URL and password to check
url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
# k anonymity gives only the first five char of the hash version of the password
res = requests.get(url)
print(res)  # gives 400 when we used the real password on line 4
print(res)  # gives 200 as we used k anonymity
# response of 400 means sth is wrong with the API, 200 is ok
'''


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}, check the api and try again")
    return res


# to check the kind of data we got
# def read_res(response):
#     print(response.text) # returns response as text

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        # print(h, count)
        if h == hash_to_check:
            return count
    return 0


# check password if it exists in API response
def pwned_api_check(password):
    # print(password.encode('utf-8')) # b'123' b shows its encoded print(
    # hashlib.sha1(password.encode('utf-8'))) # <sha1 HASH object @ 0x0000011AC60D8BD0> shows its a hash obj print(
    # hashlib.sha1(password.encode('utf-8')).hexdigest()) # gives the hash(hexadec) form ofthe password in lowercase
    # print(hashlib.sha1(password.encode('utf-8')).hexdigest().upper()) # convert to upper case running without utf-8
    # gives an error that the arg must be encoded before hashing
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # return response
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    # print(first5_char, tail)
    # print(response)  # gives 200
    # return read_res(response) # gives hashed passwords that match the beginning of our hashed password and the no of
    # times they are hacked
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"{password} was found {count} times...... you should probably change your password")
        else:
            print(f"{password} was NOT found. Carry on!")
    return 'done!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))  # accept any arguments which are the passwords and exit out of the process using
    # terminal
