"""
This file was made for import models to update their metadata for migrations

import e.g.
from src.your_app.models import your_model
"""

from src.users.models import * # noqa
from src.plans.models import * # noqa
from src.plan_statuses.models import * # noqa
from src.branches.models import * # noqa
from src.plan_values.models import * # noqa
from src.organizations.models import *   # noqa: F403
from src.currency.models import *  # noqa: F403
from src.document_types.models import *  # noqa: F403
from src.documents.models import *   # noqa: F403
from src.okei.models import *  # noqa: F403
from src.okpd.models import *  # noqa: F403
from src.organization_types.models import *  # noqa: F403
from src.products.models import *  # noqa: F403
from src.purchase_events.models import *  # noqa: F403
from src.purchase_products.models import *  # noqa: F403
from src.purchases.models import *  # noqa: F403
from src.tech_tasks.models import *  # noqa: F403
from src.way.models import *  # noqa: F403
from src.purchase_steps.models import *  # noqa: F403
from src.purchase_type.models import *  # noqa: F403
