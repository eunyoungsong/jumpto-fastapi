import datetime

from pydantic import BaseModel, validator


class AnswerCreate(BaseModel):
    content: str

    @validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    # content의 값이 없거나 또는 빈 값인 경우 "빈 값은 허용되지 않습니다." 라는 오류가 발생하도록 했다.
    

# answer 는 post 방식이기 때문에 pydantic 스키마로 읽는다. (Request Body)
# get 방식은 라우터의 스키마가 아닌 매개변수로 읽는다. (Path Parameter, Query Parameter)

class Answer(BaseModel):
    id: int
    content: str
    create_date: datetime.datetime

    class Config:
        orm_mode = True