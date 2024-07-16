"""
This file was made for import models to update their metadata for migrations

import e.g.
from src.your_app.models import your_model
"""

from src.auth.models import User, Role # noqa
from src.plans.models import Plan # noqa
from src.plan_statuses.models import PlanStatus # noqa
from src.branches.models import Branch # noqa
from src.plan_values.models import PlanValue # noqa