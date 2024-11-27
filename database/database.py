import pymongo
import asyncio
import logging
from config import DB_URI, DB_NAME, FORCE_CHANNEL, FORCE_CHANNEL2

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Connect to MongoDB and select the database
dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]

# Define collections for user, admin, and channel data
user_data = database['users']
admin_data = database['admins']
channel_data = database['channels']
channel_data2 = database['channels2']

# Function to check if a user exists
async def is_user_present(user_id: int) -> bool:
    loop = asyncio.get_running_loop()
    found = await loop.run_in_executor(None, lambda: user_data.find_one({'_id': user_id}))
    exists = bool(found)
    logger.info(f"User {user_id} exists: {exists}")
    return exists

# Function to add a new user
async def add_user(user_id: int):
    loop = asyncio.get_running_loop()
    try:
        await loop.run_in_executor(None, lambda: user_data.insert_one({'_id': user_id}))
        logger.info(f"User {user_id} added successfully.")
    except Exception as e:
        logger.error(f"Failed to add user {user_id}: {e}")

# Function to retrieve all users
async def get_all_users() -> list:
    loop = asyncio.get_running_loop()
    try:
        user_docs = await loop.run_in_executor(None, lambda: list(user_data.find()))
        user_ids = [doc['_id'] for doc in user_docs]
        logger.info(f"Retrieved {len(user_ids)} users.")
        return user_ids
    except Exception as e:
        logger.error(f"Failed to retrieve users: {e}")
        return []

# Function to delete a user
async def delete_user(user_id: int):
    loop = asyncio.get_running_loop()
    try:
        await loop.run_in_executor(None, lambda: user_data.delete_one({'_id': user_id}))
        logger.info(f"User {user_id} deleted successfully.")
    except Exception as e:
        logger.error(f"Failed to delete user {user_id}: {e}")

# Function to check if an admin exists
async def is_admin_present(admin_id: int) -> bool:
    loop = asyncio.get_running_loop()
    found = await loop.run_in_executor(None, lambda: admin_data.find_one({'_id': admin_id}))
    exists = bool(found)
    logger.info(f"Admin {admin_id} exists: {exists}")
    return exists

# Function to add a new admin
async def add_admin(admin_id: int):
    loop = asyncio.get_running_loop()
    try:
        await loop.run_in_executor(None, lambda: admin_data.insert_one({'_id': admin_id}))
        logger.info(f"Admin {admin_id} added successfully.")
    except Exception as e:
        logger.error(f"Failed to add admin {admin_id}: {e}")

# Function to retrieve all admins
async def get_all_admins() -> list:
    loop = asyncio.get_running_loop()
    try:
        admin_docs = await loop.run_in_executor(None, lambda: list(admin_data.find()))
        admin_ids = [doc['_id'] for doc in admin_docs]
        logger.info(f"Retrieved {len(admin_ids)} admins.")
        return admin_ids
    except Exception as e:
        logger.error(f"Failed to retrieve admins: {e}")
        return []

# Function to delete an admin
async def delete_admin(admin_id: int):
    loop = asyncio.get_running_loop()
    try:
        await loop.run_in_executor(None, lambda: admin_data.delete_one({'_id': admin_id}))
        logger.info(f"Admin {admin_id} deleted successfully.")
    except Exception as e:
        logger.error(f"Failed to delete admin {admin_id}: {e}")

# Function to get the primary force-subscribe channel
async def get_force_channel_1() -> int:
    loop = asyncio.get_running_loop()
    try:
        config = await loop.run_in_executor(None, lambda: channel_data.find_one({}))
        channel = config.get('force_sub_channel_1', FORCE_CHANNEL) if config else FORCE_CHANNEL
        logger.info(f"Force subscribe channel 1: {channel}")
        return channel
    except Exception as e:
        logger.error(f"Failed to get force subscribe channel 1: {e}")
        return FORCE_CHANNEL

# Function to set the primary force-subscribe channel
async def set_force_channel_1(channel1: int):
    loop = asyncio.get_running_loop()
    try:
        await loop.run_in_executor(None, lambda: channel_data.update_one({}, {'$set': {'force_sub_channel_1': channel1}}, upsert=True))
        logger.info(f"Force subscribe channel 1 set successfully to: {channel1}")
    except Exception as e:
        logger.error(f"Failed to set force subscribe channel 1: {e}")

# Function to get the secondary force-subscribe channel
async def get_force_channel_2() -> int:
    loop = asyncio.get_running_loop()
    try:
        config = await loop.run_in_executor(None, lambda: channel_data2.find_one({}))
        channel = config.get('force_sub_channel_2', FORCE_CHANNEL2) if config else FORCE_CHANNEL2
        logger.info(f"Force subscribe channel 2: {channel}")
        return channel
    except Exception as e:
        logger.error(f"Failed to get force subscribe channel 2: {e}")
        return FORCE_CHANNEL2

# Function to set the secondary force-subscribe channel
async def set_force_channel_2(channel2: int):
    loop = asyncio.get_running_loop()
    try:
        await loop.run_in_executor(None, lambda: channel_data2.update_one({}, {'$set': {'force_sub_channel_2': channel2}}, upsert=True))
        logger.info(f"Force subscribe channel 2 set successfully to: {channel2}")
    except Exception as e:
        logger.error(f"Failed to set force subscribe channel 2: {e}")
    
