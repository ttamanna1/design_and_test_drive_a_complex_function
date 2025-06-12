# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def age_checker(date):
    """
    Grants access based on age.

    Parameters: string => `YYYY-MM-DD`

    Returns: string => 'access has been granted' or 'access is denied'

    Side effects: test type of arguments => should be string. Should be in format `YYYY-MM-DD`.
        
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a age is over 16
It returns access granted
"""
age_checker("1960-10-21") => 'access granted'

"""
Given is under 16
It returns a access denied
"""
age_checker("2015-10-21") => "Access denied. your age is 10. You need to be 16."

"""
Given the type is not str
It returns an error
"""
age_checker(123445) => raise Exception('Enter DOB in string format.')


"""
Given the string is not in the correct date format
It returns 
"""
age_checker("") => raise Exception('Enter DOB in string format: YYYY-MM-DD.')


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

```

Ensure all test function names are unique, otherwise pytest will ignore them!
