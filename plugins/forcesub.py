from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID
from database.database import add_1, add_2, present_channel, present_channel2
from bot import Bot

@Bot.on_message(filters.command("forcesub1") & filters.private)
async def force_subscribe_command_1(client: Bot, message: Message):
    user_id = message.from_user.id
    if user_id != OWNER_ID:
        await message.reply_text("Only the Owner can use this command, sorry!")
        return

    if len(message.command) != 2:
        await message.reply_text("<b>Incorrect format. Use the command like this:</b> /forcesub1 {channel_id}")
        return

    try:
        channel_id = int(message.command[1])
    except ValueError:
        await message.reply_text("Invalid channel ID. Please check again!")
        return

    try:
        await add_1(channel_id)
        await client.refresh_invite_link(channel_id, link_number=1)
        await message.reply_text(f"Channel ID {channel_id} has been set for Forcesub 1...!")
    except Exception as e:
        await message.reply_text(f"Failed to set force subscribe channel 1: {e}")

@Bot.on_message(filters.command("forcesub2") & filters.private)
async def force_subscribe_command_2(client: Bot, message: Message):
    user_id = message.from_user.id
    if user_id != OWNER_ID:
        await message.reply_text("Only the Owner can use this command, sorry!")
        return

    if len(message.command) != 2:
        await message.reply_text("<b>Incorrect format. Use the command like this:</b> /forcesub2 {channel_id}")
        return

    try:
        channel_id = int(message.command[1])
    except ValueError:
        await message.reply_text("Invalid channel ID. Please check again!")
        return

    try:
        await add_2(channel_id)
        await client.refresh_invite_link(channel_id, link_number=2)
        await message.reply_text(f"Channel ID {channel_id} has been set for Forcesub 2...!")
    except Exception as e:
        await message.reply_text(f"Failed to set force subscribe channel 2: {e}")

@Bot.on_message(filters.command("viewforce") & filters.private)
async def view_force_subs(client: Bot, message: Message):
    user_id = message.from_user.id
    if user_id != OWNER_ID:
        await message.reply_text("Only the Owner can use this command, sorry!")
        return

    channel_id_1 = await present_channel()
    channel_id_2 = await present_channel2()

    channel_name_1 = "Unknown"
    channel_name_2 = "Unknown"

    try:
        if channel_id_1:
            channel_name_1 = (await client.get_chat(channel_id_1)).title
    except Exception as e:
        await message.reply_text(f"Failed to get the name of channel {channel_id_1}: {e}")

    try:
        if channel_id_2:
            channel_name_2 = (await client.get_chat(channel_id_2)).title
    except Exception as e:
        await message.reply_text(f"Failed to get the name of channel {channel_id_2}: {e}")

    await message.reply_text(f"Current Force Subscribe Channels:\n\n1: {channel_name_1} ({channel_id_1})\n2: {channel_name_2} ({channel_id_2})")

# Function to refresh invite link
async def refresh_invite_link(self, channel_id, link_number):
    try:
        link = (await self.get_chat(channel_id)).invite_link
        if not link:
            await self.export_chat_invite_link(channel_id)
            link = (await self.get_chat(channel_id)).invite_link
        if link_number == 1:
            self.invitelink1 = link
        elif link_number == 2:
            self.invitelink2 = link
    except Exception as e:
        self.LOGGER(__name__).warning(f"Failed to refresh invite link for channel {channel_id}: {e}")

Bot.refresh_invite_link = refresh_invite_link