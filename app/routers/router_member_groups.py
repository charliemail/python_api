from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from ..models.model_member_groups import MemberGroupsInputData, MemberGroupsOutputData
from typing import List
import copy

router = APIRouter(
    prefix="/member_groups",
    tags=["member_groups"],
    responses={404: {"description": "Not found"}},
)

db_name = "test_api"
collection_name = "member_groups"

# 連接到 MongoDB 服務器
client = MongoClient("mongodb://localhost:27017/")
database = client[db_name]
collection = database[collection_name]



# 清單
@router.get("/", response_model=List[MemberGroupsOutputData])
async def read_member_groups():
    all_data = collection.find()

    return all_data

# 詳情
@router.get("/{member_group_id}", response_model=List[MemberGroupsOutputData])
async def read_member_group(member_group_id: str):
    query = {"name": member_group_id}
    search_result = collection.find(query)
    search_result_copy = copy.deepcopy(search_result)

    if len(list(search_result_copy)) == 0:
        raise HTTPException(
            status_code=404, detail="Member group not found"
        )

    return search_result

# 新增
@router.post("/")
async def create_member_group(member_group_item: MemberGroupsInputData):
    member_group_dict = member_group_item.model_dump()

    insert_result = collection.insert_one(member_group_dict)
    if not insert_result.acknowledged:
        raise HTTPException(status_code=500, detail="Failed to insert data into MongoDB")

    return {"message": "Data inserted successfully", "inserted_id": str(insert_result.inserted_id)}

# 修改


# 刪除