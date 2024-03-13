from fastapi import APIRouter, HTTPException
from app.models.member_model import MemberInputData, MemberOutputData, MemberUpdateData
from app.services.member_service import MemberService
from typing import List, Optional
from pydantic import BaseModel

router = APIRouter(
    prefix="/members",
    tags=["members"],
    responses={404: {"description": "Not found"}},
)
member_service = MemberService()

# 清單
@router.get("/", response_model=List[MemberOutputData])
async def members_list():
    return await member_service.get_all_members()

# 詳情
@router.get("/{member_id}", response_model=List[MemberOutputData])
async def member_detail(member_id: str):
    result = await member_service.get_member(member_id)
    if not result:
        raise HTTPException(status_code=404, detail="Member not found")
    return result

# 新增
@router.post("/")
async def create_member(member_item: MemberInputData):
    create_result = await member_service.create_member(member_item)
    if not create_result:
        raise HTTPException(status_code=500, detail="Failed to insert data into MongoDB")
    return {"message": "Data inserted successfully", "inserted_id": str(create_result.inserted_id)}

# 修改(修改中)
@router.put("/{member_id}")
async def update_member(member_id: str, member_data: MemberUpdateData):
    update_result = await member_service.update_member(member_id, member_data)
    if not update_result:
        raise HTTPException(status_code=500, detail="Failed to update data into MongoDB")
    return {"message": "Data updated successfully", "updated_id": member_id}

# 刪除
@router.delete("/")
async def delete_member(member_id: str):
    delete_result = await member_service.delete_member(member_id)
    if not delete_result:
        raise HTTPException(status_code=500, detail="Failed to delete data")
    return {"message": "Data deleted successfully", "deleted_id": member_id}
