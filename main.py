import os
from typing import Final
from discord import Intents,Client,Message,app_commands
from dotenv import load_dotenv
from responses import get_response

#loading token
 #   Token: Final[str] = os.getenv('Token')
 #   print(Token)

#bot setup
#intents are permission for the bot to view the messages
intents: Intents = Intents.default()
intents.message_content = True 
client: Client = Client(intents=intents)

#message functions
async def send_message(message: Message, user_message: str) -> None:
    if not user_message: 
        print('(Message was empty because intents were not enabled probably)')
        return

    if is_private := user_message[0] == '?': #private messaging
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response+" - Master Oogway")  if is_private else await message.channel.send(response+" - Master Oogway") 
    except Exception as e:
        print(e)

#bot startup
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


#handling reply and messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user: #checks if the user msges
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

#main 
def main() -> None:
    client.run('MTI0MzE1Nzg5MDk5MTI1OTY5OQ.G4_bnb.jOc4QWq5LJYl9BL-Zpc0lR1FOOq6-oLC7tn_jA')


if __name__ == '__main__':
    main()