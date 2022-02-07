
from app.utils.controllers import BaseController
from app.salaries.schemas import Salary as SalarySchema, Title
from app.salaries.models import Salary as SalaryModel, SalaryOut


class SalaryController(BaseController):

    model_class = SalarySchema

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
        query = query.filter_by(english_levely=english_level)
        return query

    def _get_not_none_query(self, deprioritised_query, prioritised_query):
        pass

    def _get_most_alike_salary(self, title_name: str, seniority: int, english_level: int):
        layer = list()
        salaries_by_title = self.filter_by_title(self.base_query, title_name)
        salaries_by_seniority = self.filter_by_seniority(salaries_by_title, seniority)
        first_layer_query = self._get_not_none_query(salaries_by_title, salaries_by_seniority)
        return temporal_query

    def calculate_salary(self, salary_data: SalaryModel) -> SalaryOut:
        last_salaries = self.filter_by_title(self.base_query, salary_data.title_name)
        new_salaries = self.filter_by_seniority(last_salaries, salary_data.seniority)
        salaries = self._compare_querysets(last_salaries, new_salaries)
        last_salaries = self.filter_by_english_level(salaries, salary_data.english_level)
        self._compare_querysets(salaries, last_salaries)
        salary = salaries.first()
        if salary:
            return SalaryOut(bottom=salary.bottom, average=salary.average, top=salary.top)
        return SalaryOut(bottom=0, top=0, average=0)
