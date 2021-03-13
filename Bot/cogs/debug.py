import os, sys, discord
from discord.ext import commands

# Only if you want to use variables that are in the config.py file.
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

# Here we name the cog and create a new class for the cog.
class Template(commands.Cog, name="debug"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="debug")
    async def testcommand(self, context):
        # yet to complete
        # Don't forget to remove "pass", that's just because there's no content in the method.
        pass

# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
def setup(bot):
    bot.add_cog(debug(bot))
