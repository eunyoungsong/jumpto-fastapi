from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

# database.py 에서 만든 Base 모델 상속
from database import Base

'''
1. 모델 클래스 정의
2. 모델 등록 후 리비전 파일 생성 >> alembic revision --autogenerate
3. 리비전 파일 생성 후 리비전 파일을 실행 >> alembic upgrade head
4. 테이블이 새로 생성되었는지 DB브라우저를 통해 확인
'''

class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False) # nll값 허용
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    user = relationship("User", backref="question_users")
    modify_date = Column(DateTime, nullable=True)


class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", backref="answers")
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    user = relationship("User", backref="answer_users")
    modify_date = Column(DateTime, nullable=True)
    

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=True) # unique=True 중복안됨
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
