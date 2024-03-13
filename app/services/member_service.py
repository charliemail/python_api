from app.mongodb import mongo_db
from app.models.member_model import MemberInputData, MemberUpdateData
from bson import ObjectId
import copy

class MemberService:
    COLLECTION_NAME = 'members'

    def __init__(self):
        self.collection = mongo_db.db[self.COLLECTION_NAME]

    ## 取得所有 members 資料
    async def get_all_members(self):
        datas = self.collection.find()

        response_datas = []
        for data in datas:
            data["id"] = str(ObjectId(data["_id"]))
            response_datas.append(data)
        return response_datas
    
    ## 取得單一 member 資料
    async def get_member(self, member_id: str):
        try:
            query = {"_id": ObjectId(member_id)}
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
        
    ## 新增 member 資料
    async def create_member(self, member_item: MemberInputData):
        member_item_dict = member_item.model_dump()

        insert_result = self.collection.insert_one(member_item_dict)
        if not insert_result.acknowledged:
            return False
        return insert_result
    
    ## 修改 member 資料
    async def update_member(self, member_id: str, member_item: MemberUpdateData):
        member_item_dict = {k: v for k, v in member_item.model_dump().items() if isinstance(v, str) and v is not None or isinstance(v, list) and v != []}

        query = {"_id": ObjectId(member_id)}
        update_values = {"$set": member_item_dict}
        update_result = self.collection.update_one(query, update_values)
        if not update_result.acknowledged:
            return False
        return True
    
    ## 刪除 member 資料
    async def delete_member(self, member_id: str):
        try:
            query = {"_id": ObjectId(member_id)}
            result = self.collection.delete_one(query)
        
            if result.deleted_count == 1:
                return True
            else:
                return False
        except:
            return False