from ..domain.interfaces.language_detector import ILanguageDetector

class MockLanguageDetector(ILanguageDetector):
    def detect_language(self, file_path: str) -> str:
        # Simple extension-based mapping
        if file_path.endswith(".py"):
            return "python"
        elif file_path.endswith(".java"):
            return "java"
        elif file_path.endswith(".js"):
            return "javascript"
        elif file_path.endswith(".ts") or file_path.endswith(".tsx"):
            return "typescript"
        return "unknown"
Class = MockLanguageDetector
