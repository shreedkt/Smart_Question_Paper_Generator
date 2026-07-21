"""
Module Name:
    selector.py

Purpose:
    Filter questions based on different criteria.
"""


def filter_by_subject(questions, subject_code):
    """
    Filter questions by subject.

    Parameters
    ----------
    questions : list
        Complete question bank.

    subject_code : str
        Subject selected by user.

    Returns
    -------
    list
        Filtered questions.
    """

    filtered_questions = []

    for question in questions:

        if question["Subject_Code"] == subject_code:

            filtered_questions.append(question)

    return filtered_questions