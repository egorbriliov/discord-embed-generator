import disnake
from disnake.ext import commands

from utils.enviroment import Enviroment


bot = commands.InteractionBot(
    reload=True,
    status=disnake.Status.idle

)


if __name__ == '__main__':
    @bot.event
    async def on_ready():
        """Ассинхронная функция запуска проекта."""
        print(f'\033[3;32mБот \033[0m\033[35;1m{bot.user.name}\
              \033[0m\033[3;32mзапустился и готов к использованию!\033[0m')


bot.load_extensions("cogs/bot/slash_commands")

bot.run(Enviroment.get('TOKEN'))
