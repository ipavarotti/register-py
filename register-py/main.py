import os
from app.bot import setup_bot
from dotenv import load_dotenv

load_dotenv()

def main():
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        print("Error: DISCORD_TOKEN not found in .env file")
        return
    
    bot = setup_bot()
    bot.run(token)

if __name__ == "__main__":
    main()