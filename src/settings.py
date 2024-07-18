"""
App info, which includes in FastAPI object
e.g - app = FastAPI(title='my_app', version='0.1') e.t.c
"""

APP_VERSION = '0.2 Beta'
APP_TITLE = 'EIS clone'
DESCRIPTION = 'Simple mock-service for EIS'

# WARNING: change this to False on release
DEBUG = True

# url for openapi interactive docs
DOCS_URL = "/docs"
REDOC_URL = "/redoc"

# CORS settings
ALLOW_ORIGINS = ["*"]
ALLOW_METHODS = ["*"]
ALLOW_HEADERS = ["*"]
ALLOW_CREDENTIALS = True


# Database settings
ASYNC_DATABASE_URL ='sqlite+aiosqlite:///db.sqlite3'
SYNC_DATABASE_URL = 'sqlite:///db.sqlite3' # for alembic migrations
