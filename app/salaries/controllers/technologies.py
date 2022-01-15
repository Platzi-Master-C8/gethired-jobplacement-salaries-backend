from app.utils.controllers import BaseController
from app.salaries.schemas import Technology


class TechnologyController(BaseController):

    model_class = Technology
