

#Q1==============================================================================================================

class Employee:

    def __init__(self, gender, will_comment):

        self.gender = gender                 # man or woman
        self.will_comment = will_comment     # true or false
        self.comments_received = 0           # starts at 0 comments

    def __str__(self):

        return (self.gender
                + ": "
                + str(self.comments_received) #turns numbers into string
                + " sexist comments received")

    def set_commenter_status(self, status): #if employees amd comment or not

        self.will_comment = status

    def receive_sexist_comment(self):

        self.comments_received += 1 #add 1 if another comment was made

    def get_gender(self):

        return self.gender

    def get_commenter_status(self):

        return self.will_comment

    def get_comments_received(self):

        return self.comments_received

#Q2================================================================================================================

#part1-------------------------------------------------------------------------------------------------------------

def print_employee_list(lst):
    """
    Takes in a list of Employee objects and prints each one.
    """
    for emp in lst:         # Loop through every Employee in the list
        print(emp)          # Print each Employee using its __str__ method


#part2----------------------------------------------------------------------------------------------------------------

def create_employees(num_employees):


    num_men = int(num_employees * 0.8)   # 80% men (rounded down)
    num_women = num_employees - num_men  # remaining are women

    men_list = []
    for i in range(num_men):
        man = Employee("Man", False)     # Create a male employee
        men_list.append(man)             # Add him to the list

    women_list = []
    for i in range(num_women):
        woman = Employee("Woman", False) # Create a female employee
        women_list.append(woman)         # Add her to the list

    return men_list + women_list


#part3----------------------------------------------------------------------------------------------------------------

import random

def create_commenters(employee_list):

    for emp in employee_list:
        chance = random.random()

        if chance < 0.2:
            emp.set_commenter_status(True)


#part4--------------------------------------------------------------------------------------------------------------

import random

def generate_comments(employee_list):

    males = [e for e in employee_list if e.get_gender() == "Man"]
    females = [e for e in employee_list if e.get_gender() == "Woman"]

    for m in males:
        if m.get_commenter_status():          # only commenters act
            if females:                        # guard: skip if no women
                target = random.choice(females)
                target.receive_sexist_comment()

    for w in females:
        if w.get_commenter_status():
            if males:                          # guard: skip if no men
                target = random.choice(males)
                target.receive_sexist_comment()

#part5---------------------------------------------------------------------------------------------------------

def average_comments(employee_list):

    male_comments = []
    female_comments = []

    for emp in employee_list:
        if emp.get_gender() == "Man":
            male_comments.append(emp.get_comments_received())
        else:  # otherwise, the employee is a Woman
            female_comments.append(emp.get_comments_received())

    if len(male_comments) > 0:
        avg_male = sum(male_comments) / len(male_comments)
    else:
        avg_male = 0

    if len(female_comments) > 0:
        avg_female = sum(female_comments) / len(female_comments)
    else:
        avg_female = 0

    return (avg_male, avg_female)

employees = create_employees(10)
print_employee_list(employees)








