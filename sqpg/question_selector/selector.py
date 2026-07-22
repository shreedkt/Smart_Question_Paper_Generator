def filter_by_subject(questions, subject_code):
    
    filtered_questions = []

    for question in questions:

        if question["Subject_Code"] == subject_code:

            filtered_questions.append(question)

    return filtered_questions

def filter_by_unit(questions, unit):
        
    filtered_questions = []

    for question in questions:

        if question["Unit"] == unit:

            filtered_questions.append(question)
    return filtered_questions
def filter_by_difficulty(questions, difficulty):
    filtered_questions = []

    for question in questions:

        if question["Difficulty"] == difficulty:

            filtered_questions.append(question)
    return filtered_questions

def filter_by_marks(questions, marks):
    filtered_questions = []

    for question in questions:

        if question["Marks"] == marks:

            filtered_questions.append(question)
    return filtered_questions
def select_questions(
    questions,
    subject_code,
    unit,
    difficulty,
    marks
):
    """
    Apply all filters to the question bank.

    Parameters
    ----------
    questions : list
        Complete question bank.

    subject_code : str
        Subject selected.

    unit : str
        Unit selected.

    difficulty : str
        Difficulty selected.

    marks : str
        Marks selected.

    Returns
    -------
    list
        Final filtered questions.
    """

    questions = filter_by_subject(
        questions,
        subject_code
    )

    questions = filter_by_unit(
        questions,
        unit
    )

    questions = filter_by_difficulty(
        questions,
        difficulty
    )

    questions = filter_by_marks(
        questions,
        marks
    )

    return questions