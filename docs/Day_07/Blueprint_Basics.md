**Q1. What is a Question Paper Blueprint?**

A Question Paper Blueprint is a predefined plan or structure that specifies how a question paper should be generated. It defines the number of questions, marks, and question types required for the examination. The blueprint acts as a set of rules that the software follows while selecting questions.
| Question Type | Count | Marks |
| ------------- | ----: | ----: |
| MCQ           |     6 |   0.5 |
| SHORT         |     5 |     1 |
| LONG          |     3 |     4 |

**Q2. Why do we store blueprint information inside a dictionary?**

We store the blueprint inside a Python dictionary because it organizes related information using key-value pairs, making it easy to read, access, and modify.
For Example,
blueprint = {
    "MCQ": {
        "count": 6,
        "marks": 0.5
    }
}

"MCQ" is the key.
"count" and "marks" are properties of MCQ.

A dictionary also makes the blueprint flexible. If the exam pattern changes, we only modify the dictionary without changing the program logic.

**Q3. Why did we create**
    **get_default_blueprint()**
        **instead of writing**  
        **MCQ = 6**
        **SHORT = 5**
        **LONG = 3**

We created a function because it improves reusability, modularity, and future scalability.

Today, we have only one blueprint.

In the future, we may have:

Internal Exam 1
Internal Exam 2
Mid Semester
End Semester
Practical Examination

Each examination can have a different blueprint.
By calling
            get_default_blueprint()
the application always receives the blueprint from a single place.

This follows the Single Responsibility Principle, because the blueprint module is responsible only for providing blueprint information.

**Q4. If another department wants**
        **MCQ = 10**
        **SHORT = 4**
        **LONG = 2**

We only modify the Blueprint.

The Question Selector should remain unchanged because its job is only to filter and select questions.

The Blueprint decides how many questions of each type are required.

Keeping these responsibilities separate follows the principle of Separation of Concerns and makes the software easier to maintain.