import unittest

from src.summit_tool_scan_flow.domain_review import DomainReview, review_lane, review_score


class DomainReviewTests(unittest.TestCase):
    def test_review_lane(self) -> None:
        item = DomainReview(65, 22, 32, 71)
        self.assertEqual(review_score(item), 127)
        self.assertEqual(review_lane(item), "watch")


if __name__ == "__main__":
    unittest.main()
