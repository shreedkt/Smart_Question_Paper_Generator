"""
Module Name:
    csv_loader.py
Purpose:
    Load questions from question_bank.csv.
"""
import csv
from pathlib import Path
def load_question_bank():
    """
    Load all questions from CSV.
    Returns
    -------
    list
        List of question dictionaries.
    """
    csv_path = Path("data") / "question_bank.csv"
    questions = []
    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions.append(row)
    return questions