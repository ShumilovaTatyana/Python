# Выберите необходимое действие
# 1. Найти сотрудника
# 2. Сделать выборку сотрудников по должности
# 3. Сделать выборку сотрудников по зарплате
# 4. Добавить сотрудника
# 5. Удалить сотрудника
# 6. Обновить данные сотрудника
# 7. Экспортировать данные в формате json
# 8. Экспортировать данные в формате cmv
# 9. Закончить работу

# def find_employees_by_salary_range(employees: list) -> list:
#     result = []
#     lo, hi = get_salary_range()
#     for employee in employees:
#         if lo <= employee["salary"] <= hi:
#             result.append(employee)
#     return result

# def find_employees_by_salary_range(list_of_salary):
#     result = []
#     lo, hi = 1000, 3000
#     for i in range(len(list_of_salary)):
#         if lo <= list_of_salary[i] <= hi:
#             result.append(list_of_salary[i])
#     return result


from controller import work_with_data_base

if __name__ == "__main__":
    work_with_data_base()