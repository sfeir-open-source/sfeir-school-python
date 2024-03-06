
from datetime import datetime
import unittest

from pydantic import ValidationError
from main import MessageGet

class testCase(unittest.TestCase):

    def test_MessageGetSuccess(self):
        get_message = MessageGet(
            id=1,
            author="author",
            message="message",
            creation_date=datetime.now()
        )
        self.assertIsNotNone(get_message)

    def test_MessageGetFailed(self):
        with self.assertRaises(ValidationError):
            MessageGet()

if __name__ == '__main__':
    unittest.main()
