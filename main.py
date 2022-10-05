from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel
from io import StringIO
import json

app = FastAPI()

first_part = []
second_part = []
third_part = []
final_array = []

@app.post('/{category}/')
async def main_structure(category: str, name: str, label: str, email: str, phone: str, website: str, summary: str):
    testvar1 = {
        category: {
            'name': name,
            'label': label,
            'email': email,
            'phone': phone,
            'website': website,
            'summary': summary,
        }
    }
    first_part.append(testvar1)
    return testvar1


@app.post('/work')
async def works_structure(company: str, position: str, website: str, start_date: str, end_date: str, summary: str):
    testvar2 = {
            'company': company,
            'position': position,
            'website': website,
            'start_date': start_date,
            'end_date': end_date,
            'summary': summary,
        }
    second_part.append(testvar2)
    return testvar2


@app.post('/education')
async def education_structure(university: str, area: str, study_type: str, start_date: str, end_date: str):
    testvar3 = {
        'education': [
            {
                'institution': university,
                'area': area,
                'study_type': study_type,
                'start_date': start_date,
                'end_date': end_date,
            }
        ]
    }
    third_part.append(testvar3)
    return testvar3


@app.get('/cv')
async def education_structure():
    final_array = [first_part[0], {'working experience': second_part}, third_part[0]]
    return final_array
