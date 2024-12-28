import lesson_01

def test_todo_1():
    assert lesson_01.x == 10  # Check if x is assigned the value 10.

def test_todo_2():
    assert hasattr(lesson_01, "first_name"), "first_name variable not found."
    assert hasattr(lesson_01, "last_name"), "last_name variable not found."
    full_name = f"{lesson_01.first_name} {lesson_01.last_name}"
    assert full_name.strip() == lesson_01.full_name  # Assuming full_name is stored.

def test_todo_3():
    assert lesson_01.a == 5, "Variable 'a' should be 5."
    assert lesson_01.b == 3, "Variable 'b' should be 3."
    assert lesson_01.sum_result == 8, "Sum is incorrect."
    assert lesson_01.diff_result == 2, "Difference is incorrect."
    assert lesson_01.prod_result == 15, "Product is incorrect."
    assert lesson_01.quot_result == 5 / 3, "Quotient is incorrect."

def test_todo_4():
    assert lesson_01.a == 20, "Variable 'a' value is not swapped."
    assert lesson_01.b == 10, "Variable 'b' value is not swapped."

def test_todo_5():
    assert lesson_01.number == 7, "Variable 'number' should be 7."
    assert lesson_01.even_or_odd == "odd", "Number parity check is incorrect."

def test_todo_6():
    assert lesson_01.age == 25, "Age should be 25 for testing purposes."  # Adjust expected value.
    assert lesson_01.age_message == "You are 25 years old.", "Age message is incorrect."

def test_todo_7():
    assert lesson_01.string_length == 18, "String length should be 18."

def test_todo_8():
    assert lesson_01.a is True, "Variable 'a' should be True."
    assert lesson_01.b is False, "Variable 'b' should be False."
    assert lesson_01.and_result is False, "'a and b' result is incorrect."
    assert lesson_01.or_result is True, "'a or b' result is incorrect."
    assert lesson_01.not_a_result is False, "'not a' result is incorrect."

def test_todo_9():
    assert lesson_01.number_to_square == 4, "Variable 'number_to_square' should be 4."
    assert lesson_01.square_result == 16, "Square calculation is incorrect."

def test_todo_10():
    expected_message = "Hello, Alice, you are 30 years old."
    assert lesson_01.formatted_message == expected_message, "Formatted message is incorrect."
