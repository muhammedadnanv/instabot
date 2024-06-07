from instabot import Bot
import time

# Create a bot instance
bot = Bot()

# Login to Instagram
bot.login(username="comicfix.in", password="Barcelona@10")

# Define the username of the user you want to follow
target_username = "its_adnan_are"

# Get user ID of the target user
user_id = bot.get_user_id_from_username(target_username)

# Follow the user
bot.follow(user_id)

# Wait for a few seconds
time.sleep(5)

# Logout from Instagram
bot.logout()
