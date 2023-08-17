from django.test import TestCase
from .services import fetch_summary, interpret_summary

# Create your tests here.

class TestServices(TestCase):

        def test_fetch_summary(self):
            wiki =  "https://en.wikipedia.org/wiki/Python_(programming_language)"
            result = fetch_summary(wiki)
            self.assertEqual(type(result), str)
            self.assertIn('Python', result) # check if the string is in the result
            self.assertTrue('Python' in result) # check if the string is in the result


        def test_interpret_summary(self):
            summary = 'Python is an interpreted high-level general-purpose programming language.'
            result = interpret_summary(summary)
            self.assertIn('Python', result)
            self.assertEqual(type(result), list)

