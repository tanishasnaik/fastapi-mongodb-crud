from app.database import collection

async def create_user(user):
    print("Received user:", user)
    try:
        result = await collection.insert_one(user)
        print("Inserted user with ID:", result.inserted_id)
        return {"message": "User created", "id": str(result.inserted_id)}
    except Exception as e:
        print("Error inserting user:", e)
        raise e  

async def get_users():
    try:
        print("Fetching all users...")
        users_cursor = collection.find()
        users = await users_cursor.to_list(length=100)
        
        for user in users:
            user["_id"] = str(user["_id"])
        
        print(" Users fetched:", users)
        return users
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise e

async def get_user_by_email(email):
    try:
        user = await collection.find_one({"email": email})
        if user:
            user["_id"] = str(user["_id"]) 
        return user
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise e

async def update_user(email, new_data):
    try:
        result = await collection.update_one({"email": email}, {"$set": new_data})
        if result.modified_count == 1:
            return {"message": "User updated successfully"}
        elif result.matched_count == 1:
            return {"message": "No new data to update"} 
        else:
            return {"message": "User not found"}
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise e

async def delete_user(email):
    try:
        result = await collection.delete_one({"email": email})
        if result.deleted_count == 1:
            return {"message": "User deleted successfully"}
        else:
            return {"message": "User not found"}
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise e
