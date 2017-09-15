
import click
import config
import init
import fn
import config
from loader import parse




APP_DESC = """
    _____                                ______ __  __
    |  __ \                              |  ____|  \/  |
    | |  | | __ _ _ __  _ __ ___  _   _  | |__  | \  / |
    | |  | |/ _` | '_ \| '_ ` _ \| | | | |  __| | |\/| |
    | |__| | (_| | | | | | | | | | |_| _| |    | |  | |
    |_____/ \__,_|_| |_|_| |_| |_|\__,_(_)_|    |_|  |_|

                        ---- A Terminal Tools For DouyuTV

    @author Alexander Luo (496952252@qq.com)
                                    last_update 2017-07-10 08:54:59
"""




@click.command()
@click.option('--add', type=click.Choice(['swagger', 'sr']))    # 限定值
@click.argument('command')

def parse_command(command,add):
    if command == "install":
        init.initial()
    if add:
       parse.handle(add)







def main():
    print(APP_DESC)
    parse_command()



if __name__ == '__main__':
    main()
