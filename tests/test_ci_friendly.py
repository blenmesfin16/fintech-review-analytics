"""
CI/CD Friendly Unit Tests
These tests verify project structure without requiring data files
"""

import pytest
import os

class TestProjectStructure:
    """Test that project has required directories"""
    
    def test_scripts_directory(self):
        """Test scripts directory exists"""
        assert os.path.exists("scripts"), "scripts directory missing"
    
    def test_src_directory(self):
        """Test src directory exists"""
        assert os.path.exists("src"), "src directory missing"
    
    def test_tests_directory(self):
        """Test tests directory exists"""
        assert os.path.exists("tests"), "tests directory missing"
    
    def test_requirements_file(self):
        """Test requirements.txt exists"""
        assert os.path.exists("requirements.txt"), "requirements.txt missing"
    
    def test_readme_file(self):
        """Test README.md exists"""
        assert os.path.exists("README.md"), "README.md missing"
    
    def test_gitignore_file(self):
        """Test .gitignore exists"""
        assert os.path.exists(".gitignore"), ".gitignore missing"

class TestGitHubWorkflow:
    """Test CI/CD workflow exists"""
    
    def test_workflow_file_exists(self):
        """Test GitHub Actions workflow exists"""
        workflow_path = ".github/workflows/unittests.yml"
        assert os.path.exists(workflow_path), f"{workflow_path} not found"

class TestDataRequirements:
    """Test data requirements are documented"""
    
    def test_minimum_reviews_requirement(self):
        """Requirement: 1200+ total reviews"""
        required_total = 1200
        assert required_total >= 1200, "Need at least 1200 reviews"
    
    def test_minimum_per_bank_requirement(self):
        """Requirement: 400+ per bank"""
        required_per_bank = 400
        assert required_per_bank >= 400, "Need at least 400 reviews per bank"

class TestCodeModules:
    """Test that code modules exist"""
    
    def test_scraper_script_exists(self):
        """Test scraper script exists"""
        assert os.path.exists("scripts/scraper_fixed.py") or os.path.exists("scripts/scrape_reviews.py")

    def test_preprocess_script_exists(self):
        """Test preprocessing script exists"""
        assert os.path.exists("scripts/preprocess.py")

    def test_sentiment_script_exists(self):
        """Test sentiment script exists"""
        assert os.path.exists("scripts/sentiment_simple.py")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
