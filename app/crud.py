from app.database import collection

async def create_user(user):
    return await collection.insert_one(user)

async def get_users():
    return await collection.find().to_list(100)

async def get_user_by_email(email):
    return await collection.find_one({"email": email})

async def update_user(email, new_data):
    return await collection.update_one({"email": email}, {"$set": new_data})

async def delete_user(email):
    return await collection.delete_one({"email": email})
