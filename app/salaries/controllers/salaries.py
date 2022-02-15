
from typing import List

from sqlalchemy.orm import Query

from app.utils.controllers import BaseController
from app.salaries.models import Salary as Salary, Title
from app.salaries.schemas import Salary as SalarySchema, SalaryOut


class SalaryController(BaseController):

    model_class = Salary

    def _compare_querysets(self, old_queryset, new_queryset):
        if not len(new_queryset) and len(old_queryset):
            return old_queryset
        return new_queryset

    def filter_by_title(self, query, title_name):
        title = self.session.query(Title).filter_by(name=title_name).first()
        query = query.filter_by(title_id=title.id)
        return query

    def filter_by_seniority(self, query, seniority):
        query = query.filter_by(seniority=seniority)
        return query

    def filter_by_english_level(self, query, english_level):
        query = query.filter_by(english_level=english_level)
        return query

    def filter_by_remote(self, query, is_remote: bool):
        query = query.filter_by(is_remote=is_remote)
        return query

    def filter_by_location(self, query, location: str):
        query = query.filter_by(location=location)
        return query

    def _get_not_none_query(self, deprioritised_query, prioritised_query):
        if prioritised_query.count():
            return prioritised_query
        return deprioritised_query

    def _get_salary_by_layers(
            self, title_name: str, seniority: int, english_level: str,
            is_remote: bool, location: str,
    ):
        layers = list()
        salaries_by_title = self.filter_by_title(self.base_query, title_name)
        salaries_by_seniority = self.filter_by_seniority(salaries_by_title, seniority)
        first_layer = self._get_not_none_query(salaries_by_title, salaries_by_seniority)
        layers.append(first_layer)
        salaries_by_english_level = self.filter_by_english_level(first_layer, english_level)
        second_layer = self._get_not_none_query(first_layer, salaries_by_english_level)
        layers.append(second_layer)
        salaries_by_remote = self.filter_by_remote(second_layer, is_remote)
        third_layer = self._get_not_none_query(second_layer, salaries_by_remote)
        layers.append(third_layer)
        if not is_remote and location:
            salaries_by_location = self.filter_by_location(third_layer, location)
            layers.append(self._get_not_none_query(third_layer, salaries_by_location))
        return layers

    def _get_upper_layer(self, layers):
        layer = layers[0]
        for query in layers:
            if query.count():
                layer = query
        return layer

    def _filter_salaries_by_technologies(self, salaries: Query, technologies: List[str]) -> Salary:
        best_salary = (None, 0)
        for salary in salaries:
            salary_technologies = [technology for technology in salary.technologies_collection if technology.name in technologies]
            number_of_technologies = len(salary_technologies)
            if number_of_technologies >= best_salary[1]:
                best_salary = (salary, number_of_technologies)
        return best_salary[0] or salaries.first()

    def _get_most_alike_salary(
            self, title_name: str, seniority: int, english_level: str,
            is_remote: bool, location: str, technologies: List[str]
    ) -> Salary:
        layers = self._get_salary_by_layers(title_name, seniority, english_level, is_remote, location)
        salaries = self._get_upper_layer(layers)
        salary = self._filter_salaries_by_technologies(salaries, technologies)
        return salary

    def calculate_salary(self, salary_data: SalarySchema) -> SalaryOut:
        salary = self._get_most_alike_salary(
            salary_data.title_name, salary_data.seniority, salary_data.english_level,
            salary_data.is_remote, salary_data.location, salary_data.technologies
        )
        if salary:
            return SalaryOut(bottom=salary.bottom, average=salary.average, top=salary.top)
        return SalaryOut(bottom=0, top=0, average=0)
