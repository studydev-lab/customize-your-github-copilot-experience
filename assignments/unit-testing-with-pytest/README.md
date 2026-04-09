# 📘 Assignment: Unit Testing with pytest

## 🎯 Objective

Learn to write effective unit tests using the pytest framework to ensure code quality and catch bugs early.
Students will write test cases for existing functions, practice test organization, and use pytest fixtures and assertions.

## 📝 Tasks

### 🛠️ Write Basic Unit Tests

#### Description
Create test cases for simple utility functions using pytest assertions and test organization.

#### Requirements
Completed program should:

- Write test functions for at least 3 utility functions (e.g., `add()`, `is_prime()`, `reverse_string()`).
- Use descriptive test names following the pattern `test_<function>_<scenario>`.
- Include positive and negative test cases for each function.
- Run tests with `pytest` and ensure all pass.


### 🛠️ Organize Tests with Fixtures and Parametrization

#### Description
Use pytest fixtures to set up shared test data and parametrize tests to cover multiple input scenarios efficiently.

#### Requirements
Completed program should:

- Create a pytest fixture that provides test data (e.g., sample lists, dictionaries, or objects).
- Use `@pytest.mark.parametrize` to test a function with multiple parameter sets in a single test.
- Demonstrate how parametrized tests reduce code duplication and improve readability.


### 🛠️ Test Error Handling and Edge Cases

#### Description
Write tests to verify that functions handle errors, exceptions, and edge cases correctly.

#### Requirements
Completed program should:

- Write tests to verify that invalid inputs raise appropriate exceptions (e.g., `ValueError`, `TypeError`).
- Test edge cases such as empty inputs, `None` values, and boundary conditions.
- Use `pytest.raises()` to assert that exceptions are raised as expected.
