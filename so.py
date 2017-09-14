
import click
import logging
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


def main():
    print(APP_DESC)
    parse_command()


@click.command()
# @click.option('--count',default=1, help='Number of greetings.')
@click.option('--name',  help='The person to greet.')
@click.option('--spring', type=click.Choice(['boot', 'mvc']))    # 限定值
@click.option('--load', type=click.Choice(['swagger', 'sr']))    # 限定值
def parse_command(name,spring,load):
    if name:
        te()
    if spring:
        print(2)
    if load:
       parse.handle(load)




def te():
    print("123")



if __name__ == '__main__':
    main()
