from contacts import get_employee_address
from hr import get_policy
from productivity import get_role
from productivity import ProductivitySystem
from contacts import AddressBook
from hr import PayrollSystem
from hr import SalaryPolicy, CommissionPolicy, HourlyPolicy
from productivity import ManagerRole, SecretaryRole, SalesRole, FactoryRole


class Employee():
    def __init__(self, id, name, role, payroll, address=None):
        self.id = id
        self.name = name
        self.address = address
        self.role = role
        self.payroll = payroll

    def work(self, hours):
        duties = self.role.perform_duties(hours)
        print(f'Employee {self.id} - {self.name}:')
        print(f'- {duties}\n')
        self.payroll.track_work(hours)

    def calculate_payroll(self):
        return self.payroll.calculate_payroll()


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name, None, SalaryPolicy(weekly_salary))


class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name, None, HourlyPolicy(hours_worked, hour_rate))


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.payroll = CommissionPolicy(weekly_salary, commission)


class Manager(SalaryEmployee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name, weekly_salary)
        self.role = ManagerRole()


class Secretary(SalaryEmployee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name, weekly_salary)
        self.role = SecretaryRole()


class SalesPerson(CommissionEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary, commission)
        self.role = SalesRole()


class FactoryWorker(HourlyEmployee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name, hours_worked, hour_rate)
        self.role = FactoryRole()


class TemporarySecretary(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name, SecretaryRole(), HourlyPolicy(hours_worked, hour_rate))
