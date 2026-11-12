import unittest

from app import build_metadata


class TestApplicationBuild(unittest.TestCase):

    def test_service_name(self):
        result = build_metadata()
        self.assertEqual(result["service"], "inventory-api")

    def test_application_version(self):
        result = build_metadata()
        self.assertEqual(result["version"], "2.0")

    def test_application_status(self):
        result = build_metadata()
        self.assertEqual(result["status"], "ready")


if __name__ == "__main__":
    unittest.main()