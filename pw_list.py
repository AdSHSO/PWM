import hashlib
import requests

def pw_sha1_hash(password):

    #encode string as unicode utf-8
    #we hash bytes - not strings
    hashed_pw = hashlib.sha1(password.encode())

    #hashed_pw is hash obj  ect -> hexdigest for string
    return hashed_pw.hexdigest().upper()

def check_remote(hashed_pw):

    trunc_pw = hashed_pw[:5]
    r = requests.get("https://api.pwnedpasswords.com/range/"+trunc_pw)
    return r.text

def password_in_pwned_list(pw):

    candidate_list = check_remote(pw_sha1_hash(pw))

    for line in candidate_list.splitlines():       
        content = line.split(":")
        if content[0] == pw_sha1_hash(pw)[5:]:
            return True
        else:
            pass
    return False

#print(password_in_pwned_list("abcd1234"))