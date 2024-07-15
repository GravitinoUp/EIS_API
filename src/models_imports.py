"""
This file was made for import models to update their metadata for migrations

import e.g.
from src.your_app.models import your_model
"""

from src.auth.models import User, Role # noqa
from src.plans.models import Plan, PlanEvent, PlanPosition, Way, PlanStatus # noqa