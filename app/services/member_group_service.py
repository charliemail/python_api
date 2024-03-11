from app.models.member_group_model import MemberGroupBase, MemberGroupOutputData
from app.mongodb import mongo_db
import copy
from bson import ObjectId

class MemberGroupService:
    COLLECTION_NAME = 'member_groups'

    def __init__(self):
        self.collection = mongo_db.db[self.COLLECTION_NAME]

    ## 取得所有 member_groups 資料
    async def get_all_member_groups(self):
        datas = self.collection.find()

        response_datas = []
        for data in datas:
            data["id"] = str(ObjectId(data["_id"]))
            response_datas.append(data)
        return response_datas
    
    ## 取得單一 member_group 資料
    async def get_member_group(self, member_group_id: str):
        try:
            query = {"_id": ObjectId(member_group_id)}
            datas = self.collection.find(query)
            
            datas_copy = copy.deepcopy(datas)
            if len(list(datas_copy)) == 0:
                return False
            
            response_datas = []
            for data in datas:
                data["id"] = str(ObjectId(data["_id"]))
                response_datas.append(data)
            return response_datas
        except:
            return False
    
    ## 新增 member_group 資料
    async def create_member_group(self, member_group_item: MemberGroupBase):
        member_group_item_dict = member_group_item.model_dump()

        insert_result = self.collection.insert_one(member_group_item_dict)
        if not insert_result.acknowledged:
            return False
        return insert_result
    
    ## 修改 member_group 資料
    async def update_member_group(self, member_group_id: str, member_group_item: MemberGroupBase):
        member_group_item_dict = member_group_item.model_dump()

        query = {"_id": ObjectId(member_group_id)}
        neq_values = {"$set": member_group_item_dict}
        update_result = self.collection.update_one(query, neq_values)
        if not update_result.acknowledged:
            return False
        return True
    
    ## 刪除 member_group 資料
    async def delete_member_group(self, member_group_id: str):
        try:
            query = {"_id": ObjectId(member_group_id)}
            result = self.collection.delete_one(query)
        
            if result.deleted_count == 1:
                return True
            else:
                return False
        except:
            return False
