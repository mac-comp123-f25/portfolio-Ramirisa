<<<<<<< HEAD
import random
# import math  # <- unused; safe to remove

class Employee:
    """
    Employee with a gender, a flag for whether they will make sexist comments,
    and a counter of comments received.
    """
    def __init__(self, gender: str, will_comment: bool):
        self.gender = gender                  # "Man" or "Woman"
        self.will_comment = will_comment      # True or False
        self.comments_received = 0            # starts at 0

    def __str__(self):
=======
"""
Contains a simulation of the Petrie Multiplier that is based on classes.
"""

import random
import math


class Employee:
    """
    For this simulation, we only focus on the gender of an employee, and on
    whether this employee is likely to make negative statements
    towards the other gender.
    """

    def __init__(self, gender: str, will_comment):
        """
        Takes in the employee's gender and whether they comment, and it
        saves those values to instance variables. It also initializes the
        variable that holds the comments received by this employee to zero.
        """
        # TODO: Implement this method then remove this line
        pass

    def __str__(self):
        """
        Produces a printable string format for this employee.
        """
>>>>>>> 6b6f4bfcc4be35394f77a6148c0327dfb4ed7a25
        return (self.gender.rjust(5)
                + ": "
                + str(self.comments_received)
                + " sexist comments received")

<<<<<<< HEAD
    # --- Methods required by the spec ---
    def set_commenter_status(self, status: bool):
        self.will_comment = status

    def receive_sexist_comment(self):
        self.comments_received += 1

    def get_gender(self):
        return self.gender

    def get_commenter_status(self):
        return self.will_comment

    def get_comments_received(self):
        return self.comments_received


def print_employee_list(lst):
    """
    Print each employee using its __str__.
    """
    for emp in lst:
        print(emp)


def create_employees(total_num: int):
    """
    Create ~80% men and the remainder women, all starting with will_comment=False.
    Return a single combined list.
    """
    num_men = int(total_num * 0.8)         # 80% men (rounded down)
    num_women = total_num - num_men        # remainder women

    employees = []
    for _ in range(num_men):
        employees.append(Employee("Man", False))
    for _ in range(num_women):
        employees.append(Employee("Woman", False))
    return employees
=======

def print_employee_list(lst):
    """
    Given a list of employees, this method will print the details of each employee
    by using the print() method
    """
    # TODO: Implement this function then remove this line
    pass


def create_employees(total_num):
    """
    Takes in the number of employees to make, builds and returns a list that contains
    that many employees. It ensures that ~80% are men and the rest women.
    """
    # TODO: Implement this function then remove this line
    pass
>>>>>>> 6b6f4bfcc4be35394f77a6148c0327dfb4ed7a25


def create_commenters(lst):
    """
<<<<<<< HEAD
    Each employee has a 20% chance to be marked as a commenter.
    Modifies employees in place; returns nothing.
    """
    for emp in lst:
        if random.random() < 0.2:          # 20% chance
            emp.set_commenter_status(True)
=======
    Given a list of employees, make 20% of each gender be sexist employees. This
    method should not return anything.
    """
    # TODO: Implement this function then remove this line
    pass
>>>>>>> 6b6f4bfcc4be35394f77a6148c0327dfb4ed7a25


def generate_comments(lst):
    """
<<<<<<< HEAD
    Each employee who will comment gives ONE sexist comment to a random
    opposite-gender employee. Modifies counts in place; returns nothing.
    """
    males   = [e for e in lst if e.get_gender() == "Man"]
    females = [e for e in lst if e.get_gender() == "Woman"]

    # Men who comment -> target random woman
    for m in males:
        if m.get_commenter_status() and females:
            target = random.choice(females)
            target.receive_sexist_comment()

    # Women who comment -> target random man
    for w in females:
        if w.get_commenter_status() and males:
            target = random.choice(males)
            target.receive_sexist_comment()
=======
    Given a list of employees, have each sexist employee give one sexist comment to
    another employee of the opposite gender, chosen randomly. This method should
    not return anything
    """
    # TODO: Implement this function then remove this line
    pass
>>>>>>> 6b6f4bfcc4be35394f77a6148c0327dfb4ed7a25


def average_comments(lst):
    """
<<<<<<< HEAD
    Return (<avg_for_men>, <avg_for_women>) based on comments_received.
    """
    male_counts = []
    female_counts = []

    for emp in lst:
        if emp.get_gender() == "Man":
            male_counts.append(emp.get_comments_received())
        else:
            female_counts.append(emp.get_comments_received())

    avg_male   = (sum(male_counts) / len(male_counts)) if male_counts else 0
    avg_female = (sum(female_counts) / len(female_counts)) if female_counts else 0
    return (avg_male, avg_female)
=======
    Returns a tuple that represents the average amount of comments received for men and women
    respectively. Return statement will be in the form (<avg_for_men>, <avg_for_women>)
    """
    # TODO: Implement this function then remove this line
    pass
>>>>>>> 6b6f4bfcc4be35394f77a6148c0327dfb4ed7a25


def main():
    """
    Print out information about the average comments
    received by men and women after a simulation has been run
    """
    num_employees_to_generate = 100
    num_comment_rounds = 50

    employee_list = create_employees(num_employees_to_generate)
    create_commenters(employee_list)
    for rounds in range(num_comment_rounds):
        generate_comments(employee_list)

    (men_avg, women_avg) = average_comments(employee_list)
    print("  Men received on average ",   men_avg, "sexist comments")
    print("Women received on average ", women_avg, "sexist comments")


if __name__ == "__main__":
    "<----- Test code for print_employee_list ----->"
    lst = [Employee('Man', True),
           Employee('Man', False),
           Employee('Woman', True),
           Employee('Woman', False)]
    print_employee_list(lst)

    "<----- Test code for create_employees ----->"
    employees = create_employees(10)
    print_employee_list(employees)

    "<----- Test code for create_commenters ----->"
    create_commenters(employees)
    print_employee_list(employees)

    "<----- Test code for generate_comments ----->"
    generate_comments(employees)
    print_employee_list(employees)

    "<----- Test code for average_comments ----->"
    print(average_comments(employees))

    "<----- Run the simulation ----->"
<<<<<<< HEAD
    # main()  # <-- KEEP THIS, Uncomment it after implementing all the functions
=======
    # main()  # <-- KEEP THIS, Uncomment it after implementing all the functions
>>>>>>> 6b6f4bfcc4be35394f77a6148c0327dfb4ed7a25
