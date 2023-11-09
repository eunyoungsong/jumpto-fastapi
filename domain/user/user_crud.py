from sqlalchemy.orm import Session
from domain.user.user_schema import UserCreate
from models import User

# # v01
# def create_user(db: Session, user_create: UserCreate):
#     db_user = User(username=user_create.username,
#                    password=user_create.password1,
#                    email=user_create.email)
#     db.add(db_user)
#     db.commit()

# 비밀번호는 탈취되더라도 복호화 할 수 없는 값으로 암호화 해서 저장해야 한다.
# 비밀번호를 암호화 하여 저장하기 위해서는 passlib가 필요
# pip install "passlib[bcrypt]"


# v02 암호화
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, user_create: UserCreate):
    db_user = User( username = user_create.username,
                    password = pwd_context.hash(user_create.password1),
                    email = user_create.email )
    db.add(db_user)
    db.commit()
# bcrypt 알고리즘을 사용하는 pwd_context 객체를 생성하고 pwd_context 객체를 사용하여 비밀번호를 암호화하여 저장


# 중복값에 대한 예외처리를 위한 함수
def get_existing_user(db: Session, user_create: UserCreate):
    return db.query(User).filter(
        (User.username == user_create.username) |
        (User.email == user_create.email)
    ).first()
# username 또는(OR) email 인 점에 유의하자
# 동일한 사용자명 또는 이메일이 이미 존재할 경우


def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()