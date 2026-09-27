import unittest
from models.user import User
from models.place import Place
from models.review import Review


class TestReview(unittest.TestCase):

    @class_method
    def setUpClass(cls):
        cls.user = User()
        cls.place = Place()
        cls.review = Review()
      

    @class_method
    def tearDownClass(cls):
        del cls.user
        del cls.place
        del cls.review

    def test_reviewText(self):
        self.review.text = "It's serene in the mornings."
        self.assertEqual(self.review.text, "It's serene in the mornings.")

    def test_reviewPlace(self):
        self.review.place_id =  self.place.id
        self.assertEqual( self.review.place_id, self.place.id)

    def test_reviewUser(self):
        self.review.user_id =  self.user.id
        self.assertEqual( self.review.user_id, self.user.id)


if __name__ == '__main__':
    unittest.main()
