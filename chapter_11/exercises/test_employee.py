import pytest
from employee import Employee

@pytest.fixture
def emp():
    first = "test"
    last = "employee1"
    salary = 100_000
    emp = Employee(first, last, salary)
    return emp

def test_give_default_raise(emp):
    initial_salary = emp.salary
    emp.give_raise()
    assert emp.salary == initial_salary + 5000

def test_give_custom_raise(emp):
    initial_salary = emp.salary
    salary_raise = 6500
    emp.give_raise(salary_raise)
    assert emp.salary == initial_salary + salary_raise