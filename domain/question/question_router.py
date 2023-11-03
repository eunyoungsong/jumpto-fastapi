# 라우터 파일에 반드시 필요한 것은 APIRouter 클래스로 생성한 router 객체이다. 
# router 객체를 생성하여 FastAPI 앱에 등록해야만 라우팅 기능이 동작한다.
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Question

router = APIRouter(
    # prefix 속성은 요청 URL에 항상 포함되어야 하는 값
    prefix="/api/question",
)

# # 1. db 세션 사용하기 
# from database import SessionLocal
# @router.get("/list")
# def question_list():
#     # db 세션 생성
#     db = SessionLocal()
#     # 세션을 이용하여 db 조회
#     _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
#     # 사용한 세션 반환
#     db.close()
#     return _question_list 

# # 2. with문 사용하여 get_db 사용하기
# @router.get("/list")
# def question_list():
#     with get_db() as db:
#         _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
#     return _question_list

# 3. Depends 사용하기
# Depends는 매개 변수로 전달 받은 함수를 실행시킨 결과를 리턴한다.
# 따라서 db 객체에는 get_db 제너레이터에 의해 생성된 세션 객체가 주입된다. 
@router.get("/list")
def question_list(db: Session = Depends(get_db)):
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list