"""The Config Module."""


class Config:
    """The API Configration class."""
    APP_NAME = "Masterblog API"
    POSTS_FOLDER_NAME = "data"
    POSTS_FILE_NAME = "posts.json"
    SWAGGER_URL = "/api/docs"  # (1) swagger endpoint e.g. HTTP://localhost:5002/api/docs
    API_URL = "/static/masterblog.json"  # (2) ensure you create this dir and file
    LIMITER_DEFAULT_LIMITS = ["1000 per hour", "100 per minute"]
