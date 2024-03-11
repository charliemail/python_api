from pydantic import BaseModel, Field
from bson import ObjectId

class MemberGroupBase(BaseModel):
    name: str

# 輸出數據模型
class MemberGroupOutputData(MemberGroupBase):
    id: str