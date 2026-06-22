import os
from typing import Dict, Optional

class FeatureManager:
    def __init__(self, defaults: Optional[Dict[str, bool]] = None):
        self._defaults = defaults or {}

    def is_enabled(self, flag: str) -> bool:
        # Check environment variables first (prefix GITTY_FF_)
        env_val = os.environ.get(f"GITTY_FF_{flag}")
        if env_val is not None:
            return env_val.lower() in ("true", "1", "yes")

        # Fallback to defaults list
        return self._defaults.get(flag, False)
