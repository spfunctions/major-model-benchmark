import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src" / "sf_benchmark"))

from scoring import score_output


class ScoringTests(unittest.TestCase):
    def test_exact_match(self):
        self.assertEqual(score_output({"value": "0.715"}, {"method": "exact_match"}, " 0.715 "), 1.0)

    def test_contains(self):
        self.assertEqual(score_output({"value": "range(len(xs) - window + 1)"}, {"method": "contains"}, "use range(len(xs) - window + 1)"), 1.0)

    def test_json_subset(self):
        expected = {"value": {"probability": 0.62}}
        self.assertEqual(score_output(expected, {"method": "json_subset"}, '{"probability":0.62,"event":"x"}'), 1.0)

    def test_label_match(self):
        self.assertEqual(score_output({"value": "YES"}, {"method": "label_match"}, "YES, because edge is positive"), 1.0)

    def test_range(self):
        self.assertEqual(score_output({"min": 45, "max": 65}, {"method": "range"}, "55%"), 1.0)


if __name__ == "__main__":
    unittest.main()
