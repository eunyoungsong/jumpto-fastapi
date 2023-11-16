from datetime import datetime

from domain.question.question_schema import QuestionCreate, QuestionUpdate
from models import Question, User
from sqlalchemy.orm import Session

# # 질문 목록 CRUD
# def get_question_list(db: Session):
#     question_list = db.query(Question)\
#         .order_by(Question.create_date.desc())\
#         .all()
#     return question_list

# 페이징을 위한 질문 목록 CRUD 
def get_question_list(db: Session, skip: int = 0, limit: int = 10): # (조회한 데이터의 시작위치, 한페이지에 보여줄 갯수)
    _question_list = db.query(Question)\
        .order_by(Question.create_date.desc())

    total = _question_list.count()
    question_list = _question_list.offset(skip).limit(limit).all()
    return total, question_list  # (전체 건수, 페이징 적용된 질문 목록)



# 질문 CRUD
def get_question(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question




# 질문 등록 CRUD
def create_question(db: Session, question_create: QuestionCreate, user: User):
    db_question = Question(subject=question_create.subject,
                           content = question_create.content,
                           create_date = datetime.now(),
                           user=user)
    db.add(db_question)
    db.commit()
   
    
# 질문 수정 CRUD
def update_question(db: Session, db_question: Question,
                    question_update: QuestionUpdate):
    db_question.subject = question_update.subject
    db_question.content = question_update.content
    db_question.modify_date = datetime.now()
    db.add(db_question)
    db.commit()