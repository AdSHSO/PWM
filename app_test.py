import unittest
import pw_list
import check_pw_validity

from app import app
from flask import jsonify, json 
from core_hashing_module import Password

class BasicTests(unittest.TestCase):

    #always executed to prepare tests
    #could for example also include populating a database  
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True 
        pass

    #clean up everything, e.g. delete data created for testing
    def tearDown(self):
        pass 

    #test whether the PMS responds with http "ok"
    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200) 

    #test whether PMS responds with a "201" to a POST request
    def test_post_add_pw(self):
        rv = self.app.post(
            '/add_pw', data=json.dumps(dict(user_id="abcd", clear_pw="1234")), content_type='application/json')
            #the json. dumps() method will just return an encoded string, which would require manually adding the MIME type header.
        self.assertEqual(rv.status_code, 201)

    #example of a unit test for a class methode
    def test_pwm(self):
        p = Password()
        self.assertTrue(p.atest)
        #self.assertFalse(p.atest) -> liefert Fehler wie erwartet


    def test_check_pw_validity(self):
        password = "abcd"
        #Password is < 10
        self.assertFalse(check_pw_validity.check(password))

    def test_password_in_pwned_list(self):
        #self.assertTrue(True)
        self.assertTrue(pw_list.password_in_pwned_list("abcd1234"))

if __name__ == '__main__':
    unittest.main()