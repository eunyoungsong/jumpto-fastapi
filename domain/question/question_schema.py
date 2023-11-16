import datetime
from typing import Union
from pydantic import BaseModel, field_validator
from domain.answer.answer_schema import Answer
from domain.user.user_schema import User

# 질문 스키마
class Question(BaseModel):
    id:int
    subject:str
    content:str
    create_date:datetime.datetime
    answers: list[Answer] = []
    user: Union[User, None]

    # Question 모델의 항목들이 자동으로 Question 스키마로 매핑된다.
    class Config:
        orm_mode = True


# 질문 등록 스키마
class QuestionCreate(BaseModel):
    subject:str
    content:str
    
    @field_validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v


# 질문 목록 스키마
class QuestionList(BaseModel):
    total: int = 0
    question_list: list[Question] = []
    


# 질문 수정 스키마
class QuestionUpdate(QuestionCreate):
    question_id: int