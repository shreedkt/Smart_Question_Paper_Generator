Question Bank

↓

CSV Loader

↓

Subject Filter

↓

Unit Filter

↓

Difficulty Filter

↓

Question Type Filter

↓

Marks Filter

↓

Selected Questions


**1. Why do we create one filter function for each criterion instead of one large function?**
For Increase the modularity or easy to debug and for future enhancement of module 

**2. What is the advantage of chaining filters like this?**
**questions = filter_by_subject(questions, "BCA101")**
**questions = filter_by_unit(questions, "2")**
**questions = filter_by_difficulty(questions, "MEDIUM")**
by above this we choose few question from huge data set 

**3. Which software engineering principle are we following by writing separate filter functions?**
Single Responsibility Principle (SRP) and the Separation of Concerns (SoC)

**4. If tomorrow we need to filter by Bloom's Taxonomy level, what new function would you create?**
filter_by_Bloom'sTaxonomy()

**Q1. Why is Marks stored as a string?**
csv.DictReader() reads every value from a CSV file as a string by default. Therefore, even if the CSV contains 1, Python reads it as "1".
**Q2. Why don't we compare like this?**
    **if question["Marks"] == 1:**
    Because question["Marks"] is a string, while 1 is an integer.
**Q3. Why do all filter functions return a list instead of a single question?**
A filter may find zero, one, or many matching questions.
**Q4. What will happen if no question matches the filter?**
The function returns an empty list.