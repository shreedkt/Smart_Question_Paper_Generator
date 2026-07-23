Q1. Why is list(blueprint.keys())
better than writing
["MCQ",
 "SHORT",
 "LONG"]

manually?
--------------------------------------------
Using list(blueprint.keys()) automatically gets all question types from the blueprint dictionary. If we later add a new question type (for example, CASE STUDY), the function will return it automatically without changing the code. Writing the list manually requires updating the code every time the blueprint changes.


Q2. Why do we create

get_blueprint_details()

instead of directly accessing

blueprint["MCQ"]
--------------------------------------------
We create get_blueprint_details() to hide the internal structure of the blueprint and provide a single function to access its data. This makes the code reusable, modular, and easier to maintain. The caller only needs to know the function, not how the blueprint is stored.

Q3. What is Information Hiding?
--------------------------------------
Information Hiding is the principle of hiding the internal implementation of a module and exposing only the necessary functions. Other modules use these functions without knowing how the data is stored or processed internally.
Example:

Instead of writing:

blueprint["MCQ"]

other modules call:

get_blueprint_details(blueprint, "MCQ")

The module hides the dictionary structure from the rest of the project.

Q4. Which module should know the structure of the blueprint?

Blueprint
Selector
Main.py
CSV Loader

Explain your answer.
-----------------------------------
Blueprint module

Explanation:

Only the Blueprint module should know how the blueprint dictionary is structured because it owns and manages the blueprint data.

Blueprint module: Creates and manages the blueprint structure.
Selector module: Only receives blueprint information to select questions. It should not know how the blueprint is stored.
Main.py: Coordinates the application by calling different modules. It should not access the blueprint structure directly.
CSV Loader: Only reads questions from the CSV file. It has no relation to the blueprint.

This follows the Single Responsibility Principle and Information Hiding, making the project easier to maintain and extend.