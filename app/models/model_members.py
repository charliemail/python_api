from pydantic import BaseModel, validator

# 輸入數據模型
class InputData(BaseModel):
    name: str
    gender: str
    account: str
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
class OutputData(BaseModel):
    name: str
    gender: str
    account: str