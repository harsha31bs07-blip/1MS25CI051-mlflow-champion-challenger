"""Check generated identity fields and transcriptions against the supplied keys."""
import json
import re
import xml.etree.ElementTree as ET
from zipfile import ZipFile
from config import ROOT, STUDENT

NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}


def paragraphs(filename):
    with ZipFile(ROOT / filename) as package:
        document = ET.fromstring(package.read('word/document.xml'))
    return [''.join(p.itertext()) for p in document.findall('.//w:p', NS)]


def test_day_one_answers_match_supplied_key():
    text = '\n'.join(paragraphs('Day_1_MCQs_with_Answer_Key.docx'))
    key = {int(n): a.replace(' ', '') for n, a in re.findall(r'Question (\d+): ([A-D](?:, [A-D])*)', text)}
    supplied = json.loads((ROOT / 'quiz_answers.json').read_text())['day_1']
    assert len(key) == len(supplied) == 15
    for number, answer, explanation in supplied:
        assert answer.split(' (')[0].replace(' ', '') == key[number]
        assert explanation.strip()


def test_day_two_answers_match_supplied_table():
    with ZipFile(ROOT / 'Day_2_MCQs_with_Answer_Key.docx') as package:
        document = ET.fromstring(package.read('word/document.xml'))
    key = {}
    for row in document.findall('.//w:tr', NS):
        cells = [''.join(cell.itertext()).strip() for cell in row.findall('w:tc', NS)]
        if len(cells) >= 2 and cells[0].isdigit() and cells[1] in {'A', 'B', 'C', 'D'}:
            key[int(cells[0])] = cells[1]
    supplied = json.loads((ROOT / 'quiz_answers.json').read_text())['day_2']
    assert len(key) == len(supplied) == 15
    assert all(answer == key[number] and explanation.strip() for number, answer, explanation in supplied)


def test_generated_records_contain_identity_and_disclosure():
    for filename in ['Completed_Lab_Record.docx', 'Completed_Quiz_Answers.docx']:
        text = '\n'.join(paragraphs(filename))
        assert STUDENT['name'] in text and STUDENT['usn'] in text
    lab = '\n'.join(paragraphs('Completed_Lab_Record.docx'))
    assert 'AI declaration' in lab and 'Day 1 Quiz Answers' in lab and 'Day 2 Quiz Answers' in lab
