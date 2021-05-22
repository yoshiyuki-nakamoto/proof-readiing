import unittest
import proofreading_function

class TestProofreading(unittest.TestCase):
    def test_load_change_rule(self):
        expect = {
        "一斉" : "いっせい" ,
        "走る" : "はしる"
        }
        result = proofreading_function.load_change_rule("change_test.csv")
        self.assertEqual(result, expect)

    def test_multiple_replace(self):
        s= "一斉"
        expect = "いっせい"
        result = proofreading_function.multiple_replace(s)
        self.assertEqual(result, expect)

    def test_multiple_replace(self):
        s= "に"
        expect = "に"
        result = proofreading_function.multiple_replace(s)
        self.assertEqual(result, expect)

    def test_multiple_replace(self):
        s= "走る"
        expect = "はしる"
        result = proofreading_function.multiple_replace(s)
        self.assertEqual(result, expect)

    def test_proof_with_word_base(self):
        s= "一斉に走る"
        expect = "いっせいにはしる"
        result = proofreading_function.proof_with_word_base(s)
        self.assertEqual(result, expect)

if __name__ == '__main__':
    unittest.main(verbosity=2)
