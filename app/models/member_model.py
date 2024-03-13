from pydantic import BaseModel, EmailStr, validator
from typing import List, Optional
from app.models.member_group_model import MemberGroupOutputData

# 共通數據模型
class MemberBase(BaseModel):
    name: str
    gender: str
    account: str
    email: EmailStr
    member_groups: List[MemberGroupOutputData] = []

# 輸入數據模型
class MemberInputData(MemberBase):
    password: str

    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password length must be at least 8 characters')
        if not any(char.isupper() for char in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(char.islower() for char in v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one digit')
        return v

# 輸出數據模型
class MemberOutputData(MemberBase):
    id: str

# 更新數據模型
class MemberUpdateData(BaseModel):
    name: Optional[str] = None
    gender: Optional[str] = None
    password: Optional[str] = None
    member_groups: Optional[List[MemberGroupOutputData]] = []
    email: Optional[EmailStr] = None

    @validator('password')
    def validate_password(cls, v):
        if v is not None:
            if len(v) < 8:
                raise ValueError('Password length must be at least 8 characters')
            if not any(char.isupper() for char in v):
                raise ValueError('Password must contain at least one uppercase letter')
            if not any(char.islower() for char in v):
                raise ValueError('Password must contain at least one lowercase letter')
            if not any(char.isdigit() for char in v):
                raise ValueError('Password must contain at least one digit')
        return v