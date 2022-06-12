from dotenv import load_dotenv
import os
import interactions
import SpotifyIntegration

# TODO: Debug close parenthesis issue, implement other commands

load_dotenv()
TOKEN = os.environ["disc_token"]

bot = interactions.Client(token = TOKEN)

@bot.command(
    name = "search",
    description = "Searches for a song and adds it to the Spotify queue"
    options= [
        interactions.Options(
            name = "Query",
            description= "The query you want to search",
            type = interactions.OptionType.STRING
            required = True,
        )
    ]
)
async def search(ctx: interactions.CommandContext, query: str):
    await SpotifyIntegration.search_song(query)



bot.start()