import pytest
from services.scanner_service.infrastructure.language_detector import LanguageDetector

def test_language_detector_mappings():
    detector = LanguageDetector()
    
    assert detector.detect_language("main.py") == "python"
    assert detector.detect_language("src/main.py") == "python"
    assert detector.detect_language("UserService.java") == "java"
    assert detector.detect_language("script.js") == "javascript"
    assert detector.detect_language("App.tsx") == "typescript"
    assert detector.detect_language("App.ts") == "typescript"
    assert detector.detect_language("component.jsx") == "javascript"
    assert detector.detect_language("README.md") == "unknown"
    assert detector.detect_language("Makefile") == "unknown"
    assert detector.detect_language("MAIN.PY") == "python"  # Case-insensitivity check
