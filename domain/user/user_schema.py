from pydantic import BaseModel, field_validator, EmailStr
from pydantic_core.core_schema import FieldValidationInfo

class UserCreate(BaseModel):
    username: str
    password1: str
    password2: str
    email: EmailStr # EmailStr 타입을 사용하려면 email_validator 설치해야 함 >> pip install "pydantic[email]"

    @field_validator('username', 'password1', 'password2', 'email')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

    @field_validator('password2')
    def passwords_match(cls, v, info: FieldValidationInfo):
        if 'password1' in info.data and v != info.data['password1']:
            raise ValueError('비밀번호가 일치하지 않습니다')
        return v

# 로그인 입력항목은 fastapi의 security 패키지에 있는 OAuth2PasswordRequestForm 클래스를 사용하므로 따로 만들 필요가 없다.
# 출력항목에 해당하는 스키마만 만들어주자
class Token(BaseModel):
    access_token:str
    token_type:str
    username:str