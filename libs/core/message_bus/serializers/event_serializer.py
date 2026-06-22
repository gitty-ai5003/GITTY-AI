import json
from typing import Any
from datetime import datetime

class EventSerializer:
    @staticmethod
    def serialize(event: Any) -> str:
        """Serializes domain events (like Pydantic models or standard dicts) to JSON string."""
        if hasattr(event, "model_dump_json"): # Pydantic v2
            return event.model_dump_json()
        elif hasattr(event, "json"): # Pydantic v1
            return event.json()
        
        # Default fallback serializer for datetime/uuid
        def default_serializer(obj):
            if isinstance(obj, datetime):
                return obj.isoformat() + "Z"
            return str(obj)

        return json.dumps(event, default=default_serializer)

    @staticmethod
    def deserialize(payload: str) -> dict:
        """Deserializes a JSON string payload back into a dictionary."""
        return json.loads(payload)
