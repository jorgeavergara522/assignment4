# Module 3: Introduction to Object-Oriented Programming (OOP) and Advanced Testing in Python

## Module Overview
Welcome to **Module 3**, where you will transition from functional programming to **Object-Oriented Programming (OOP)** in Python. This module is designed to deepen your understanding of Python by introducing OOP principles and advanced testing techniques. You will engage with a hands-on codebase that serves as your primary textbook, including a simple calculator application (`calculator/__init__.py`), an operations module (`operations/__init__.py`), and corresponding test files (`tests/test_calculator.py` and `tests/test_operations.py`). Each file is thoroughly commented to guide you through essential programming concepts and best practices in Python.

By studying and interacting with this code, you'll gain practical experience in implementing OOP principles such as classes and static methods, building interactive command-line interfaces using the REPL (Read-Eval-Print Loop) pattern, applying the DRY (Don't Repeat Yourself) principle, handling errors gracefully, and ensuring code reliability through parameterized testing with `pytest`.

## Why Object-Oriented Programming and Advanced Testing?
**Object-Oriented Programming (OOP)** is a fundamental paradigm that enhances code organization, reusability, and scalability. By encapsulating related functionalities within classes, you can create more intuitive and manageable codebases. This module introduces you to OOP concepts such as classes, static methods, and encapsulation, building upon your previous knowledge of functions.

**Advanced Testing** ensures that your applications are reliable and maintainable. Parameterized tests allow you to run the same test logic with different input values efficiently, increasing your test coverage and reducing code duplication. Mastery of testing frameworks like `pytest` is crucial for developing robust Python applications. Additionally, achieving **100% test coverage** ensures that all parts of your code are tested, minimizing the risk of hidden bugs and enhancing code quality.

## Learning Outcomes
By the end of this module, you will be able to:
- CLO 6: Implement object-oriented programming principles in Python.
- CLO 7: Apply professional terminology and concepts related to web systems development.

## Module 3 Learning Pathway

Videos:

- [Module 3 Overview](https://youtu.be/Vy52g99WqFI)
- [Module 3 Hands on](https://youtu.be/P8jmJe9js-0)


### Recall

**Title:** Prior Experience with Python Programming and Functional Programming  
**Grading Type:** Points  
**Instructions:** 
- **Discussion Forum:** Share your previous experiences with Python programming, specifically focusing on functional programming, control structures, and command-line interfaces.
- **Reflection:** Discuss any challenges you faced in these areas and the strategies you used to overcome them.
- **Quiz:** Complete a brief quiz to assess your current understanding of Python control structures and functional programming concepts.
- **Purpose:** This activity will help gauge your familiarity with these concepts and prepare you for the new material.

### Read

Your **primary textbook** for this module is the provided codebase. Each file is meticulously commented to explain the underlying concepts and best practices. Here’s a breakdown of the key components:

1. **`app/calculator__init__.py`**
   - **Purpose:** Implements a simple calculator using Python’s REPL pattern.
   - **Key Concepts:** 
     - Control structures (`while` loops, `if-elif-else` statements)
     - User input handling
     - Error handling with `try-except` blocks
     - Modular code organization by importing from `operations.py`

2. **`app/operations/__init__.py`**
   - **Purpose:** Contains the `Operations` class with static methods for basic arithmetic operations.
   - **Key Concepts:**
     - **Classes and Static Methods:** Understand how to encapsulate related functionalities within a class using static methods.
     - **Encapsulation:** Group related functions together to enhance code organization and reusability.
     - **Input Validation and Error Raising:** Implement robust input validation and error handling within class methods.

3. **`tests/test_calculator.py`**
   - **Purpose:** Provides unit tests for the calculator REPL application.
   - **Key Concepts:**
     - Using `pytest` for testing
     - Simulating user input with `monkeypatch`
     - Capturing and asserting output

4. **`tests/test_operations.py`**
   - **Purpose:** Contains parameterized tests for the `Operations` class methods.
   - **Key Concepts:**
     - **Parameterized Testing:** Run the same test logic with different input values to enhance test coverage.
     - Testing positive and negative scenarios
     - Ensuring proper exception handling

**Supplementary Articles:**
To complement your understanding of the codebase, please read the following articles:
1. **[Mastering Python Control Structures](https://realpython.com/python-conditional-statements/)**
2. **[Introduction to Object-Oriented Programming in Python](https://realpython.com/python3-object-oriented-programming/)**
3. **[Building Command-Line Applications in Python](https://realpython.com/command-line-interfaces-python-argparse/)**
4. **[Implementing the REPL Pattern in Python](https://realpython.com/python-repl/)**
5. **[DRY (Don't Repeat Yourself) Principle in Python](https://www.makeuseof.com/python-dry-principle/)**
6. **[Look Before You Leap vs. Easier to Ask Forgiveness than Permission](https://realpython.com/python-lbyl-vs-eafp/)**
7. **[Error Handling in Python: A Deep Dive](https://realpython.com/python-exceptions/)**
8. **[Comprehensive Guide to Testing in Python](https://realpython.com/python-testing/)**

### Watch

Engage with the following instructional videos to reinforce the concepts covered in the codebase and readings:
1. **Video: Instructor Video**


### Submit

**Activity Type:** Advanced Hands-on Assignment  

**Activity Title:** Interactive Calculator Command-Line Application  

**Grading Type:** Points  

**Submission Instructions:** Submit a link to your GitHub repository containing the project.

**Instructions:** 
- **Repository Setup:**
  - Initialize a new Git repository locally and create a corresponding repository on GitHub.
  - Set up a Python project in your preferred IDE with a well-structured directory layout.
  - Create and activate a virtual environment for your project.
  
- **Application Development:**
  - Develop a command-line calculator application with the following features:
    - **REPL Interface:** Implement a Read-Eval-Print Loop for continuous user interaction.
    - **Arithmetic Operations:** Allow users to perform addition, subtraction, multiplication, and division.
    - **User Prompts:**
      - Prompt for the desired operation and the numbers to operate on.
      - Provide clear instructions and feedback to the user.
    - **Input Validation:** Validate user inputs to ensure they follow the expected format and handle invalid inputs gracefully.
    - **Error Handling:** Handle errors such as invalid inputs and division by zero gracefully, providing meaningful messages to the user.

- **Best Practices:**
  - **DRY Principle:** Apply the DRY principle and other best practices to ensure your code is maintainable and efficient.
  
- **Testing:**
  - **Unit Tests:** Write comprehensive unit tests using `pytest` to verify the functionality of individual components.
  - **Parameterized Tests:** Implement parameterized tests in `tests/test_operations.py` to cover various input scenarios efficiently.
  - **Test Coverage:** Achieve **100% test coverage** for your application, ensuring that all code paths are tested.
  
- **Documentation:**
  - Create detailed documentation, including a `README.md` file with setup and usage instructions.
  
- **Version Control & CI:**
  - Push your code to GitHub, ensuring it follows best practices for code organization and documentation.
  - **Configure GitHub Actions:**
    - Set up GitHub Actions to automatically run your tests on each push to the repository.
    - Ensure that GitHub Actions checks for 100% test coverage. The CI pipeline should only pass if all tests pass and the test coverage meets 100%. If the coverage is below 100%, the build should fail, prompting you to add the necessary tests.

**Grading Expectations:** 
- **Functionality:** Completeness and accuracy of the calculator command-line application.
- **User Interface:** Proper implementation of the REPL pattern and a user-friendly interface.
- **Code Quality:** Efficient use of Python control structures, adherence to the DRY principle, and other professional coding practices.
- **Error Handling:** Comprehensive error handling mechanisms.
- **Testing:** 
  - Thorough unit and parameterized testing using `pytest`.
  - Achieving 100% test coverage as enforced by GitHub Actions.
- **Documentation:** Well-structured code with comprehensive documentation.
- **Automation:** Successful setup of GitHub Actions for automated testing and coverage enforcement.

**Alignment:** 
- Implement Python control structures effectively in a command-line application.
- Apply the DRY principle and other best practices for writing maintainable Python code.
- Develop a command-line application using the REPL pattern.
- Implement comprehensive error handling strategies in Python.
- Write and execute unit and parameterized tests for Python applications using `pytest`.
- Achieve and enforce 100% test coverage through Continuous Integration with GitHub Actions.

### Reflect

**Title:** Module 3 In-Depth Reflection  
**Grading Type:** Points  
**Instructions:**
- **Reflection Essay:** Compose a comprehensive reflection (300-400 words) on your experience developing the interactive calculator command-line application.
  - **Application of Concepts:** Analyze how the concepts learned in this module can be applied to real-world programming scenarios.
  - **Challenges and Solutions:** Discuss any challenges you encountered during the project and the strategies you used to overcome them.
  - **Self-Evaluation:** Evaluate your current level of confidence in using these tools and identify areas where you need further practice or support.
- **Purpose:** This activity aims to encourage deep metacognition and help you connect new knowledge with prior experiences and future applications.

### Quiz

**Title:** Advanced Python Programming and Command-Line Application Development Quiz  
**Grading Type:** Points  
**Instructions:**
- **Comprehensive Assessment:** Complete a comprehensive quiz covering the advanced concepts and techniques introduced in this module.
  - **Topics Covered:** Control structures, Object-Oriented Programming (OOP) principles, command-line application development, REPL pattern implementation, application of the DRY principle, error handling strategies, and testing with `pytest`.
  - **Question Types:** The quiz will include multiple-choice, short answer, and code analysis questions to thoroughly evaluate your comprehension and application of the module's content.
- **Preparation:** Review all provided materials, including cheat sheets, tutorials, and your project code before taking the quiz.

---

This comprehensive module leverages the provided codebase as your primary textbook, allowing you to learn by doing. By engaging with the commented code, completing hands-on assignments, and reflecting on your learning process, you will build a strong foundation in Object-Oriented Programming and advanced testing in Python. Embrace the opportunity to write clean, efficient, and thoroughly tested code, ensuring high-quality applications through 100% test coverage and automated CI processes.
