"""
Module Name:
    blueprint.py

Purpose:
    Store blueprint information for question paper generation.

Author:
    Deepak Kumar Tiwari
"""


def get_default_blueprint():
    """
    Return default internal examination blueprint.

    Returns
    -------
    dict
        Blueprint configuration.
    """

    blueprint = {

        "MCQ": {
            "count": 6,
            "marks": 0.5
        },

        "SHORT": {
            "count": 5,
            "marks": 1
        },

        "LONG": {
            "count": 3,
            "marks": 4
        }

    }

    return blueprint
def get_question_type(blueprint):
    """
    Return all question types.

    Parameters
    ----------
    blueprint : dict

    Returns
    -------
    list
    """

    return list(blueprint.keys())
def get_blueprint_details(
    blueprint,
    question_type
):
    """
    Return blueprint information
    for a question type.
    """

    return blueprint[question_type]