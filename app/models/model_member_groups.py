from pydantic import BaseModel
from typing import Optional

# 輸入數據模型
class MemberGroupsInputData(BaseModel):
    name: str

# 輸出數據模型
class MemberGroupsOutputData(BaseModel):
    name: str