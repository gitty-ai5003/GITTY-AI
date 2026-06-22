import pytest
from libs.shared_kernel import Result, Maybe, Identifier
from libs.cache import MemoryCache, cached
from libs.feature_flags import FeatureManager, ENABLE_NEO4J
from libs.ai.agents import RepositoryQAAgent
from services.parser_service.application.parser_factory import ParserFactory
from services.scanner_service.application.language_detection_service import LanguageDetectionService
from services.scanner_service.infrastructure.mock_detector import MockLanguageDetector

def test_result_monad():
    # Test success path
    success_res = Result.ok("data")
    assert success_res.is_success
    assert not success_res.is_failure
    assert success_res.value == "data"

    # Test mapping
    mapped_res = success_res.map(lambda x: x + "_mapped")
    assert mapped_res.value == "data_mapped"

    # Test failure path
    fail_res = Result.fail("error message")
    assert fail_res.is_failure
    assert not fail_res.is_success
    assert fail_res.error == "error message"

def test_maybe_monad():
    some_val = Maybe.some("val")
    assert some_val.has_value
    assert not some_val.is_empty
    assert some_val.value == "val"
    assert some_val.get_or_else("default") == "val"

    none_val = Maybe.none()
    assert none_val.is_empty
    assert not none_val.has_value
    assert none_val.get_or_else("default") == "default"

def test_memory_cache():
    cache = MemoryCache()
    cache.set("key", "value", ttl=10)
    assert cache.get("key") == "value"

    cache.delete("key")
    assert cache.get("key") is None

def test_feature_manager():
    manager = FeatureManager(defaults={ENABLE_NEO4J: True})
    assert manager.is_enabled(ENABLE_NEO4J)
    assert not manager.is_enabled("ENABLE_RAG")

def test_ai_agent():
    agent = RepositoryQAAgent()
    res = agent.run({"query": "What is authentication?"})
    assert res["status"] == "success"
    assert "Mock" in res["answer"]

def test_parser_factory():
    factory = ParserFactory()
    python_parser = factory.get_parser("python")
    assert python_parser.parse_file("content")["language"] == "python"

    with pytest.raises(ValueError):
        factory.get_parser("cobol")

def test_language_detection_service():
    detector = MockLanguageDetector()
    service = LanguageDetectionService(detector)
    assert service.detect("main.py") == "python"
    assert service.detect("UserService.java") == "java"
    assert service.detect("App.ts") == "typescript"
    assert service.detect("script.js") == "javascript"
    assert service.detect("document.txt") == "unknown"
