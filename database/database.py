import pymongo
import asyncio
from config import DB_URI, DB_NAME, FORCE_CHANNEL, FORCE_CHANNEL2

# MongoDB connection and database selection
dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]

# Collections for users, admins, and channels
user_data = database['users']
admin_data = database['admins']
channel_data = database['channels']
channel_data2 = database['channels2']

# ------------------ User Management ------------------

# Check if a user exists
async def present_user(user_id: int):
    loop = asyncio.get_running_loop()
    found = await loop.run_in_executor(None, lambda: user_data.find_one({'_id': user_id}))
    return bool(found)

# Add a new user
async def add_user(user_id: int):
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, lambda: user_data.insert_one({'_id': user_id}))
    return

# Retrieve all users
async def full_userbase():
    loop = asyncio.get_running_loop()
    user_docs = await loop.run_in_executor(None, lambda: user_data.find())
    user_ids = [doc['_id'] for doc in user_docs]
    return user_ids

# Delete a user
async def del_user(user_id: int):
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, lambda: user_data.delete_one({'_id': user_id}))
    return

# ------------------ Admin Management ------------------

# Check if an admin exists
async def present_admin(admin_id: int):
    loop = asyncio.get_running_loop()
    found = await loop.run_in_executor(None, lambda: admin_data.find_one({'_id': admin_id}))
    return bool(found)

# Add a new admin
async def add_admin(admin_id: int):
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, lambda: admin_data.insert_one({'_id': admin_id}))
    return

# Retrieve all admins
async def full_adminbase():
    loop = asyncio.get_running_loop()
    admin_docs = await loop.run_in_executor(None, lambda: admin_data.find())
    admin_ids = [doc['_id'] for doc in admin_docs]
    return admin_ids

# Delete an admin
async def del_admin(admin_id: int):
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, lambda: admin_data.delete_one({'_id': admin_id}))
    return

# ------------------ Channel Management ------------------

# Check if a force subscribe channel (1) exists
async def present_channel():
    loop = asyncio.get_running_loop()
    try:
        config = await loop.run_in_executor(None, lambda: channel_data.find_one({}))
        return config.get('force_sub_channel_1', FORCE_CHANNEL) if config else FORCE_CHANNEL
    except Exception as e:
        print(f"Error retrieving force_sub_channel_1: {e}")
        return FORCE_CHANNEL

# Set a force subscribe channel (1)
async def add_1(channel1: int):
    loop = asyncio.get_running_loop()
    try:
        await loop.run_in_executor(
            None,
            lambda: channel_data.update_one(
                {}, {'$set': {'force_sub_channel_1': channel1}}, upsert=True
            )
        )
        print(f"Force subscribe channel 1 set successfully: {channel1}")
    except Exception as e:
        print(f"Error setting force_sub_channel_1: {e}")

# Check if a force subscribe channel (2) exists
async def present_channel2():
    loop = asyncio.get_running_loop()
    try:
        config = await loop.run_in_executor(None, lambda: channel_data2.find_one({}))
        return config.get('force_sub_channel_2', FORCE_CHANNEL2) if config else FORCE_CHANNEL2
    except Exception as e:
        print(f"Error retrieving force_sub_channel_2: {e}")
        return FORCE_CHANNEL2

# Set a force subscribe channel (2)
async def add_2(channel2: int):
    loop = asyncio.get_running_loop()
    try:
        await loop.run_in_executor(
            None,
            lambda: channel_data2.update_one(
                {}, {'$set': {'force_sub_channel_2': channel2}}, upsert=True
            )
        )
        print(f"Force subscribe channel 2 set successfully: {channel2}")
    except Exception as e:
        print(f"Error setting force_sub_channel_2: {e}")

# ------------------ Main Event Loop ------------------

# Example usage
async def main():
    # User operations
    await add_user()
    print("User exists:", await present_user(12345))
    print("All users:", await full_userbase())
    await del_user()

    # Admin operations
    await add_admin()
    print("Admin exists:", await present_admin(67890))
    print("All admins:", await full_adminbase())
    await del_admin()

    # Channel operations
    await add_1()
    print("Force channel 1:", await present_channel())
    await add_2()
    print("Force channel 2:", await present_channel2())

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
    
