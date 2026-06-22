import pytest
from typing import Dict, Any, List
from services.scanner_service.application.repository_scan_service import RepositoryScanService
from services.scanner_service.application.file_discovery_service import FileDiscoveryService
from services.scanner_service.application.language_detection_service import LanguageDetectionService
from services.scanner_service.domain.interfaces.repository_scanner import IRepositoryScanner
from services.scanner_service.domain.interfaces.file_walker import IFileWalker
from services.scanner_service.domain.interfaces.language_detector import ILanguageDetector

class MockRepositoryScanner(IRepositoryScanner):
    def clone_or_fetch(self, repo_url: str, dest_path: str) -> str:
        return dest_path

class MockFileWalker(IFileWalker):
    def walk(self, root_path: str) -> List[Dict[str, Any]]:
        return [
            {"path": "main.py", "extension": ".py", "size": 100, "checksum": "abc"},
            {"path": "README.md", "extension": ".md", "size": 200, "checksum": "def"}
        ]

class MockDetector(ILanguageDetector):
    def detect_language(self, file_path: str) -> str:
        if file_path.endswith(".py"):
            return "python"
        return "unknown"

class MockEventBus:
    def __init__(self):
        self.published = []

    def publish(self, topic: str, event: Any) -> None:
        self.published.append((topic, event))

    def subscribe(self, queue_name: str, topic: str, handler: Any) -> None:
        pass

    def start_consuming(self) -> None:
        pass

def test_repository_scan_service():
    scanner = MockRepositoryScanner()
    walker = MockFileWalker()
    detector = MockDetector()
    discovery_service = FileDiscoveryService(walker)
    language_service = LanguageDetectionService(detector)
    event_bus = MockEventBus()

    service = RepositoryScanService(
        scanner=scanner,
        discovery_service=discovery_service,
        language_service=language_service,
        publisher=event_bus
    )

    res = service.scan_remote_repository("https://github.com/user/repo.git", "/tmp/repo", repo_id="repo-123")

    assert res["repository_id"] == "repo-123"
    assert res["root_path"] == "/tmp/repo"
    assert len(res["files"]) == 2
    
    # Assert language enrichment
    assert res["files"][0]["language"] == "python"
    assert res["files"][1]["language"] == "unknown"

    # Assert published events
    assert len(event_bus.published) == 2
    assert event_bus.published[0][0] == "repository.discovered"
    assert event_bus.published[0][1].repository_id == "repo-123"
    assert event_bus.published[0][1].name == "repo"
    assert event_bus.published[0][1].url == "https://github.com/user/repo.git"

    assert event_bus.published[1][0] == "repository.indexed"
    assert event_bus.published[1][1].repository_id == "repo-123"
    assert event_bus.published[1][1].indexed_files_count == 2
