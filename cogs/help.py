from discord import *
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

        # command_name: (description, syntax)
        self.commands = {
            'open_server': ("Открывает сервер, убирает КПП.", '!open_server'),
            'close_server': ("Закрывает сервер, устанавливает КПП.", '!close_server'),
            'swear': ("Сгенерировать обзывалку.", '!swear'),
            'test': ("Протестировать себя на что-либо.", '!tester <текст>'),
            'luckyping': ("Узнать кто есть кто", '!luckyping <текст>'),
            'info': ("Информация по серверу", '!info')
        }

        # category: ' `command1 command2 command...` '
        self.categories = {
            'Развлечения   🪗':        ' `!swear !test !luckyping` ',
            'Модерация   🪖': ' `!open_server !close_server` ',
            'Утилиты   🛠️':  ' `!info` '
        }

        self.fun_name       = 'fun'
        self.mod_name       = 'mod'
        self.utilities_name = 'util'

        self.default_help = f"""   Привет!
Мои категории:
  -  Развлечения 🪗         (!help {self.fun_name})
  -  Модерация 🪖  (!help {self.mod_name})
  -  Утилиты 🛠️   (!help {self.utilities_name})

Спасибо за то что используете MacBot сделанный yer#7700!
"""

    @commands.command(name="help", alias=["commands", "info"])
    async def help(self, ctx, text=None):
        if not text == None:
            # If text is command
            if text in self.commands.keys():
                cmd_info = self.commands[text]

                embed = Embed(title = f'{text.capitalize()} команда', colour = 0xf2525a)
                embed.add_field(name=text, value=cmd_info[0] + '\n Синтаксис: ' + cmd_info[1])
            else:
                # If text is category
                match text:
                    case self.fun_name:
                        ctg = list(self.categories.keys())[0]

                        embed = Embed(title = ctg, colour = 0xf2525a,
                            description = self.categories[ctg]
                        )
                    case self.mod_name:
                        ctg = list(self.categories.keys())[1]

                        embed = Embed(title = ctg, colour = 0xf2525a,
                            description = self.categories[ctg]
                        )
                    case self.utilities_name:
                        ctg = list(self.categories.keys())[2]

                        embed = Embed(title = ctg, colour = 0xf2525a,
                            description = self.categories[ctg]
                        )
                    case _:
                        embed = Embed(title = f'MacBot Help', colour = 0xf2525a,
                            description = f"Не смог распознать: {text}"
                        )
        else:
            embed = Embed(title = f'MacBot Help', colour = 0xf2525a,
                description = self.default_help
            )

        embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar.url)
        await ctx.send(embed=embed)

# Setup cog...
async def setup(bot):
	await bot.add_cog( Help(bot) )