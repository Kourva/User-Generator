#!/usr/bin/env python3

## Random User Bot
## Get random user from telegram bot
## GITHUB: https://github.com/kozyol

# Imports
import requests
import telebot
import json

# Config
token = "Your Token"
bot = telebot.TeleBot(token)

# Start Message
print("Bot is online...\n")

# Random User Generator
def generator():
    response = requests.get("https://randomuser.me/api/")
    data = response.json()
    return data

# Start command
@bot.message_handler(commands=["start"])
def start_command(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(
        message, 
        "привет {user}".format(user=message.from_user.first_name)
    )

# Generate command
@bot.message_handler(commands=["generate"])
def generate_command(message):
    data = generator()
    
    # Personal info
    title_name = data["results"][0]["name"]["title"]
    first_name = data["results"][0]["name"]["first"]
    last_name = data["results"][0]["name"]["last"]
    picture = data["results"][0]["picture"]["large"]
    age = data["results"][0]["dob"]["age"]
    dob = data["results"][0]["dob"]["date"]
    id_name = data["results"][0]["id"]["name"]
    id_value = data["results"][0]["id"]["value"]
    # Location info 
    location_street_name = data["results"][0]["location"]["street"]["name"]
    location_street_number = data["results"][0]["location"]["street"]["number"]
    location_city = data["results"][0]["location"]["city"]
    location_state = data["results"][0]["location"]["state"]
    location_country = data["results"][0]["location"]["country"]
    location_post_code = data["results"][0]["location"]["postcode"]
    # Social info
    email = data["results"][0]["email"]
    phone = data["results"][0]["phone"]
    cell = data["results"][0]["cell"]
    username = data["results"][0]["login"]["username"]
    password = data["results"][0]["login"]["password"]

    
    result = \
f"""
{title_name} {first_name} {last_name} - {age} YO
- Day of Birth: {dob.split("T")[0]}
- ID: {id_name} - {id_value}

Location:
- Country: {location_country}
- State: {location_state}
- City: {location_city}
- Street: {location_street_number} - {location_street_name}

Social Media:
- Email: {email}
- Phone: {phone}
- Cell: {cell}
- Username: {username}
- Password: {password}
"""

    bot.send_chat_action(message.chat.id, "upload_photo")
    bot.send_photo(
        message.chat.id, 
        picture, 
        result
    )

# Run
bot.infinity_polling()
