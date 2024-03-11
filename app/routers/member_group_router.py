from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from app.models.member_group_model import MemberGroupBase, MemberGroupOutputData
from app.services.member_group_service import MemberGroupService
from typing import List
import copy

router = APIRouter(
    prefix="/member_groups",
    tags=["member_groups"],
    responses={404: {"description": "Not found"}},
)
member_group_service = MemberGroupService()

# 清單
@router.get("/", response_model=List[MemberGroupOutputData])
async def member_groups_list():
    return await member_group_service.get_all_member_groups()

# 詳情
@router.get("/{member_group_id}", response_model=List[MemberGroupOutputData])
async def member_group_detail(member_group_id: str):
    result = await member_group_service.get_member_group(member_group_id)
    if not result:
        raise HTTPException(status_code=404, detail="Member group not found")
    return result

# 新增
@router.post("/")
async def create_member_group(member_group_item: MemberGroupBase):
    create_result = await member_group_service.create_member_group(member_group_item)
    if not create_result:
        raise HTTPException(status_code=500, detail="Failed to insert data into MongoDB")
    return {"message": "Data inserted successfully", "inserted_id": str(create_result.inserted_id)}

# 修改
@router.put("/{member_group_id}")
async def update_member_group(member_group_id: str, member_group_data: MemberGroupBase):
    update_result = await member_group_service.update_member_group(member_group_id, member_group_data)
    if not update_result:
        raise HTTPException(status_code=500, detail="Failed to update data into MongoDB")
    return {"message": "Data updated successfully", "updated_id": member_group_id}

# 刪除
@router.delete("/")
async def delete_member_group(member_group_id: str):
    delete_result = await member_group_service.delete_member_group(member_group_id)
    if not delete_result:
        raise HTTPException(status_code=500, detail="Failed to delete data")
    return {"message": "Data deleted successfully", "deleted_id": member_group_id}