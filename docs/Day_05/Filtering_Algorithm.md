**Why do we read the CSV only once?**
We read the CSV file only once because reading data from memory is much faster than reading the file repeatedly from disk.
**What is in-memory processing?**
In-memory processing means performing operations on data that has already been loaded into RAM instead of reading it from the file repeatedly.
**Why is filtering done inside selector.py instead of csv_loader.py?**
csv_loader.py is responsible only for reading data, while selector.py is responsible only for filtering data. This follows the Single Responsibility Principle (SRP).
**Why does filter_by_subject() return a list?**
Because one subject can have many questions. Therefore, the function returns a list containing all matching questions instead of just one question.