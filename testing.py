
def a_function():

    int = 42

def process_user(user):

    if user.is_active():             # +1 (if)

        process_active_user(user)

    else:                            # +1 (else)

        process_inactive_user(user)

def process_active_user(user):

    if user.has_profile():           # +1 (if) +1 (nested)

        ... # process active user with profile

    else:                            # +1 (else)

        ... # process active user without profile



USERNAME = "admin"
PASSWORD = "password123"


def calculate_sum(a, b):
    result = a + b
    unused_variable = 42  # SonarQube will flag this as unused
    return result


def print_hello():
    print("Hello, World!")  # Repeated code that could be consolidated

def greet_user():
    print("Hello, World!") 


import sqlite3

def get_user_data(username):
    # Vulnerable to SQL injection if username is not sanitized
    query = f"SELECT * FROM users WHERE username = '{username}'"
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    cursor.execute(query)  # SonarQube should flag this as a vulnerability
    return cursor.fetchall()

def execute_code(user_input):
    # This can allow arbitrary code execution if user_input is not sanitized
    eval(user_input)  # SonarQube should detect this as a potential vulnerability

def divide_numbers(a, b):
    return a / b  # SonarQube will flag if there's a possibility of b being zero

def get_list_item(my_list, index):
    return my_list[index]  # SonarQube will detect a potential out-of-bounds access

def calculate_area(radius):
    pi = 3.14
    area = pi * radius ** 2
    pi = 3.14159  # Changing pi after using it can cause unexpected results in other parts
    return area        
