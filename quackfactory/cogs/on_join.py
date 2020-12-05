from discord.ext import commands
import discord
import logging

log = logging.getLogger(__name__)

JOIN_MESSAGE_CHANNEL_ID = 784643833488998411

class OnJoin(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.Cog.listener()
  async def on_guild_join(self, guild):
    log.debug(f'CHANNEL INFO HERE {guild.channels}')
    join_channel = guild.get_channel(JOIN_MESSAGE_CHANNEL_ID)

    embedCard = discord.Embed(title="Rubber Duck Debugging", description="Rubber Duck Debugging is a problem solving exercise whereby the individual explains the issue at hand, in simple terms, line by line -- to a rubber duck.", color=0xffff00)
    embedCard.add_field(name="Opt-Out", value="If you don't want to take part, react to this message with a 👎", inline=False)

    join_message = await join_channel.send(embed=embedCard)
    await join_message.add_reaction("👎")

def setup(bot):
  bot.add_cog(OnJoin(bot))
