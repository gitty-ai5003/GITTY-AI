from ..domain.interfaces.language_detector import ILanguageDetector

class LanguageDetectionService:
    def __init__(self, detector: ILanguageDetector):
        self.detector = detector

    def detect(self, file_path: str) -> str:
        return self.detector.detect_language(file_path)
