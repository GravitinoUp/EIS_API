# delete any if you don't need it
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# import from your apps routers
# e.g. - from src.your_app.views import my_router

from src.users.views import router as users_router
from src.plans.views import router as plans_router
from src.purchases.views import router as purchases_router


# import base settings
from src.settings import (
    APP_VERSION,
    APP_TITLE,
    DEBUG,
    DESCRIPTION,
    DOCS_URL,
    REDOC_URL,
    ALLOW_METHODS,
    ALLOW_HEADERS,
    ALLOW_CREDENTIALS,
    ALLOW_ORIGINS,
)

# creating app with base settings
app = FastAPI(
    title=APP_TITLE,
    version=APP_VERSION,
    debug=DEBUG,
    description=DESCRIPTION,
    docs_url=DOCS_URL,
    redoc_url=REDOC_URL,
)

# add middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,
    allow_credentials=ALLOW_CREDENTIALS,
    allow_methods=ALLOW_METHODS,
    allow_headers=ALLOW_HEADERS,
)

# add routers to app
# list of routers to include in app
# e.g. routers = [my_app_router, users_router, auth_router]
routers = [
    plans_router,
    purchases_router,
    users_router,
]

for router in routers:
    app.include_router(router)
