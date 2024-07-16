# delete any if you don't need it
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# import from your apps routers
# e.g. - from src.your_app.views import my_router

from src.users.views import router as users_router
from src.currency.views import router as currency_router
from src.document_types.views import router as document_types_router
from src.documents.views import router as documents_router
from src.okei.views import router as okei_router
from src.okpd.views import router as okpd_router
from src.organization_types.views import router as organization_types_router
from src.organizations.views import router as organizations_router
from src.plan_statuses.views import router as plan_statuses_router
from src.plan_values.views  import router as plan_values_router
from src.products.views import  router as products_router
from src.purchase_events.views import router as purchase_events_router
from src.purchase_products.views import router as purchase_products_router
from src.purchase_steps.views import router as purchase_steps_router
from src.purchase_type.views import router as purchase_type_router
from src.purchases.views import router as purchases_router
from src.tech_tasks.views import router as tech_tasks_router
from src.way.views import router as way_router
from src.plans.views import router as plans_router
from src.plan_statuses.views import router as plan_statuses_router
from src.branches.views import router as branches_router

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
    branches_router,
    currency_router,
    document_types_router,
    documents_router,
    okei_router,
    okpd_router,
    organization_types_router,
    organizations_router,
    plan_statuses_router,
    plan_values_router,
    plans_router,
    products_router,
    purchase_events_router,
    purchase_products_router,
    purchase_steps_router,
    purchase_type_router,
    purchases_router,
    tech_tasks_router,
    users_router,
    way_router
]

for router in routers:
    app.include_router(router)
