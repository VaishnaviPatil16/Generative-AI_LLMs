from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str= 'vaishnavi' #attribute
    age: Optional[int]= None
    email: EmailStr
    cgpa: float=Field(gt=0,lt=10)

new_student ={'age':32, 'email':'abc@gmail.com', 'cgpa':5}
#object student
student = Student(**new_student)

student_dict = dict(student)
print(student_dict['age'])
# print(type(student))

student_json = student.model_dump_json()
print(student_json)