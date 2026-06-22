from libs.config import get_settings, SystemSettings

# Re-expose config setup for API Gateway
settings: SystemSettings = get_settings()
