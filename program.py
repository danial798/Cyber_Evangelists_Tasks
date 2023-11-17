from employees import Manager, Secretary, SalesPerson, FactoryWorker, TemporarySecretary, EmployeeDatabase
from productivity import ProductivitySystem, track
import contacts
import disgruntled
import hr
import employees
import productivity
import json


def create_employees():
    manager = Manager(1, 'Mary Poppins', 3000)
    manager.address = contacts.Address(
        '121 Admin Rd', 'Concord', 'NH', '03301')

    secretary = Secretary(2, 'John Smith', 1500)
    secretary.address = contacts.Address(
        '67 Paperwork Ave.', 'Manchester', 'NH', '03101')

    sales_guy = SalesPerson(3, 'Kevin Bacon', 1000, 250)
    factory_worker = FactoryWorker(4, 'Jane Doe', 40, 15)
    temporary_secretary = TemporarySecretary(5, 'Robin Williams', 40, 9)

    return [manager, secretary, sales_guy, factory_worker, temporary_secretary]


def create_hr_payroll_system():
    return hr.PayrollSystem()


def create_productivity_system():
    return ProductivitySystem()


def create_employee_database():
    return EmployeeDatabase()


def print_dict(d):
    print(json.dumps(d, indent=2))


def main():
    employees = create_employees()
    productivity_system = create_productivity_system()
    payroll_system = create_hr_payroll_system()

    productivity_system.track(employees, 40)
    payroll_system.calculate_payroll(employees)
    
if __name__ == "__main__":
    main()
