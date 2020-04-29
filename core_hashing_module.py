import bcrypt 
import hmac

class Password:

    # creates a hashed password out of a cleartext password
    def hash_password(self, password_string):
        hashed_password = bcrypt.hashpw(password_string, bcrypt.gensalt())
        return hashed_password

    # evaluates whether a hashed password matches a cleartext password
    # we need to encode/decode a string to a byte object
    def hash_check(self, cleartext_password, hashed_password):
        if (hmac.compare_digest(bcrypt.hashpw(cleartext_password.encode(), hashed_password), hashed_password)):
            return True
        else:
            return False

    def atest():
        return True    