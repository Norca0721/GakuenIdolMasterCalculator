import math
from .calc import *

from hoshino import Service, priv
from hoshino.typing import CQEvent

sv = Service('Gakuen_Calc', manage_priv=priv.SUPERUSER, enable_on_default=False)
help = (
'/学mas算分 Vo Da Vi   |   计算特定三维下各评级所需分数\n' +
'/学mas算分 Vo Da Vi 终测分数  |   计算特定三维分数能够达成的最低评级'
)

@sv.on_prefix(['/学mas算分', '/算分'])
async def calculate_score(bot, ev: CQEvent):

    args = ev.message.extract_plain_text().split()
    print(len(args))

    if len(args) == 4:
        try:
            if int(args[0]) >= 1800:
                args[0] = 1800 - 30
            if int(args[1]) >= 1800:
                args[1] = 1800 - 30
            if int(args[2]) >= 1800:
                args[2] = 1800 - 30
        except:
            await bot.send(ev, "输入的属性必须为整数")
            return

        pre_status = [int(args[0]), int(args[1]), int(args[2])]
        pre_score = pre_status[0] + pre_status[1] + pre_status[2] + 90

        score = int(args[3])
        rank = 1
        mode = "master"

        bonus = await score_bonus(score)
        status = await status_calc(mode, pre_status, rank)
        rank_score = await rank_bonust(rank)

        total_score = status + bonus + rank_score
        rank_result = await calculate_rank(total_score)

        await bot.send(ev, f"目前的三维({pre_score})与分数能达到的最高评级为{rank_result}")

    elif len(args) == 3:
        try:
            if int(args[0]) >= 1800:
                args[0] = 1800
            if int(args[1]) >= 1800:
                args[1] = 1800
            if int(args[2]) >= 1800:
                args[2] = 1800
        except:
            await bot.send(ev, "输入的属性必须为整数")
            return

        pre_status = [int(args[0]), int(args[1]), int(args[2])]
        pre_score = pre_status[0] + pre_status[1] + pre_status[2]
        bonus = 90
        if pre_status[0] == 1800:
            bonus -= 30
        if pre_status[1] == 1800:
            bonus -= 30
        if pre_status[2] == 1800:
            bonus -= 30

        rank = 1
        mode = "master"
        msg = ""
        msg += f"在三维为 {pre_status[0]} + {pre_status[1]} + {pre_status[2]} + {bonus} = {pre_score + bonus} 的情况下\n"
        rank_results = ["SS+", "SS", "S+", "S", "A+", "A", "B+", "B", "C+", "C", "D+", "D", "F"]
        for rank_result in rank_results:
            required_score = await required_score_for_rank(rank_result, pre_status, rank, mode)
            if required_score > 0:
                msg += f"达到等级 {rank_result} 需要的最低score为: {math.ceil(required_score)}\n"

        msg = msg.rstrip("\n")
        await bot.send(ev,  msg)

    else:
        await bot.send(ev, help)