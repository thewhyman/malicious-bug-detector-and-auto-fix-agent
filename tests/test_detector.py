import os
import json
import unittest
from unittest.mock import patch, MagicMock
from scripts.detector import MaliciousBugDetector

class TestMaliciousBugDetector(unittest.TestCase):
    def setUp(self):
        # Set up environment variables required by detector
        self.env_patcher = patch.dict(os.environ, {
            "GITHUB_TOKEN": "mock-token",
            "GITHUB_REPOSITORY": "test-owner/test-repo",
            "GITHUB_EVENT_PATH": "mock_event.json",
            "GEMINI_API_KEY": "mock-gemini-key",
            "ANTHROPIC_API_KEY": "mock-anthropic-key"
        })
        self.env_patcher.start()

    def tearDown(self):
        self.env_patcher.stop()

    @patch("requests.get")
    def test_check_user_risk_low_risk(self, mock_get):
        # Setup mock responses
        mock_profile = MagicMock()
        mock_profile.status_code = 200
        mock_profile.json.return_value = {
            "created_at": "2020-01-01T00:00:00Z"
        }
        
        mock_issues = MagicMock()
        mock_issues.status_code = 200
        mock_issues.json.return_value = {
            "total_count": 10
        }
        
        mock_get.side_effect = [mock_profile, mock_issues]
        
        # Instantiate and run check
        with patch("google.genai.Client"), patch("anthropic.Anthropic"):
            detector = MaliciousBugDetector()
            is_high_risk, reason = detector.check_user_risk("trusted_user")
            
            self.assertFalse(is_high_risk)
            self.assertEqual(reason, "Established account with history")

    @patch("requests.get")
    def test_check_user_risk_high_risk_new_account(self, mock_get):
        mock_profile = MagicMock()
        mock_profile.status_code = 200
        mock_profile.json.return_value = {
            # Less than 30 days from 2026-05-30
            "created_at": "2026-05-25T00:00:00Z"
        }
        
        mock_issues = MagicMock()
        mock_issues.status_code = 200
        mock_issues.json.return_value = {
            "total_count": 2
        }
        
        mock_get.side_effect = [mock_profile, mock_issues]
        
        with patch("google.genai.Client"), patch("anthropic.Anthropic"):
            detector = MaliciousBugDetector()
            is_high_risk, reason = detector.check_user_risk("new_user")
            
            self.assertTrue(is_high_risk)
            self.assertIn("Account age:", reason)

if __name__ == "__main__":
    unittest.main()
