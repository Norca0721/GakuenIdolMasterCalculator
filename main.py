import math
from .calc import *

from hoshino import Service, priv
from hoshino.typing import CQEvent

sv = Service('Gakuen_Calc', manage_priv=priv.SUPERUSER, enable_on_default=False)
help = (
'/学mas算分 Vo Da Vi [regular|pro|master|nia]  |  计算特定三维下各评级所需スコア和ランク\n' +
'/学mas算分 Vo Da Vi [スコア|ランク] [regular|pro|master|nia] |   计算特定三维与スコア或ランク能够达成的最低评级\n' +
'✧ 说明事项：在不指定难度的情况，单项属性上限默认的1800\n' +
'✧ 说明事项：N.I.A.模式的最终选拔通过的ランク奖励算法缺失'
)

@sv.on_prefix(['/学mas算分', '/算分'])
async def calculate_score(bot, ev: CQEvent):

    args = ev.message.extract_plain_text().split()
    try:
        target_score = int(args[3])
        mode = str(args[4]).lower()
    except ValueError:
        mode = str(args[3]).lower()
        target_score = None
    except Exception:
        target_score = None
        mode = None

    if len(args) == 5 and isinstance(target_score, int):
        try:
            if mode == "regular":
                if int(args[0]) >= 1200:
                    args[0] = 1200
                if int(args[1]) >= 1200:
                    args[1] = 1200
                if int(args[2]) >= 1200:
                    args[2] = 1200
            elif mode == "pro":
                if int(args[0]) >= 1500:
                    args[0] = 1500
                if int(args[1]) >= 1500:
                    args[1] = 1500
                if int(args[2]) >= 1500:
                    args[2] = 1500
            elif mode == "master":
                if int(args[0]) >= 1800:
                    args[0] = 1800
                if int(args[1]) >= 1800:
                    args[1] = 1800
                if int(args[2]) >= 1800:
                    args[2] = 1800
            elif mode == "nia":
                if int(args[0]) >= 2000:
                    args[0] = 2000
                if int(args[1]) >= 2000:
                    args[1] = 2000
                if int(args[2]) >= 2000:
                    args[2] = 2000
        except:
            await bot.send(ev, "输入的属性必须为整数")
            return

        pre_status = [int(args[0]), int(args[1]), int(args[2])]
        pre_score = pre_status[0] + pre_status[1] + pre_status[2]
        bonus = 90
        
        if mode == "regular":
            if pre_status[0] == 1200:
                bonus -= 30
            if pre_status[1] == 1200:
                bonus -= 30
            if pre_status[2] == 1200:
                bonus -= 30
        elif mode == "pro":
            if pre_status[0] == 1500:
                bonus -= 30
            if pre_status[1] == 1500:
                bonus -= 30
            if pre_status[2] == 1500:
                bonus -= 30
        elif mode == "master":
            if pre_status[0] == 1800:
                bonus -= 30
            if pre_status[1] == 1800:
                bonus -= 30
            if pre_status[2] == 1800:
                bonus -= 30
        elif mode == "nia":
            if pre_status[0] == 2000:
                bonus = 0
            if pre_status[1] == 2000:
                bonus = 0
            if pre_status[2] == 2000:
                bonus = 0
        
        score = int(args[3])
        rank = 1
        mode = mode
        if mode in ["regular", "pro", "master"]:
            bonus = await score_bonus(score)
            status = await status_calc(mode, pre_status, rank)
            rank_score = await rank_bonust(rank)

            total_score = status + bonus + rank_score
            rank_result = await calculate_rank(total_score)

            await bot.send(ev, f"目前的三维({pre_score})与スコア能达到的最高评级为{rank_result} | 对应スコア：{total_score}")
        elif mode == "nia":
            bonus = await rank_bonus(score)
            status = await status_calc(mode, pre_status, rank=0)
            
            total_score = status + bonus
            fans_rk = await fans_rank(target_score)
            rank_result = await calculate_rank(total_score)
            await bot.send(ev, f"目前的三维({pre_score})与ランク能达到的最高评级为{rank_result} | 对应ランク：{total_score} | 对应ランク评价：{fans_rk}")
            
            
        
    elif len(args) == 4 and isinstance(mode, str):
        try:
            if mode == "regular":
                if int(args[0]) >= 1200:
                    args[0] = 1200
                if int(args[1]) >= 1200:
                    args[1] = 1200
                if int(args[2]) >= 1200:
                    args[2] = 1200
            elif mode == "pro":
                if int(args[0]) >= 1500:
                    args[0] = 1500
                if int(args[1]) >= 1500:
                    args[1] = 1500
                if int(args[2]) >= 1500:
                    args[2] = 1500
            elif mode == "master":
                if int(args[0]) >= 1800:
                    args[0] = 1800
                if int(args[1]) >= 1800:
                    args[1] = 1800
                if int(args[2]) >= 1800:
                    args[2] = 1800
            elif mode == "nia":
                if int(args[0]) >= 2000:
                    args[0] = 2000
                if int(args[1]) >= 2000:
                    args[1] = 2000
                if int(args[2]) >= 2000:
                    args[2] = 2000
        except:
            await bot.send(ev, "输入的属性必须为整数")
            return
        
        pre_status = [int(args[0]), int(args[1]), int(args[2])]
        pre_score = pre_status[0] + pre_status[1] + pre_status[2]
        bonus = 90
        if mode == "regular":
            if pre_status[0] == 1200:
                bonus -= 30
            if pre_status[1] == 1200:
                bonus -= 30
            if pre_status[2] == 1200:
                bonus -= 30
        elif mode == "pro":
            if pre_status[0] == 1500:
                bonus -= 30
            if pre_status[1] == 1500:
                bonus -= 30
            if pre_status[2] == 1500:
                bonus -= 30
        elif mode == "master":
            if pre_status[0] == 1800:
                bonus -= 30
            if pre_status[1] == 1800:
                bonus -= 30
            if pre_status[2] == 1800:
                bonus -= 30
        elif mode == "nia":
            if pre_status[0] == 2000:
                bonus -= 30
            if pre_status[1] == 2000:
                bonus -= 30
            if pre_status[2] == 2000:
                bonus -= 30

        rank = 1
        mode = mode
        msg = ""
        rank_results = ["SS+", "SS", "S+", "S", "A+", "A"]
        
        if mode in ["regular", "pro", "master"]:
            msg += f"在三维为 {pre_status[0]} + {pre_status[1]} + {pre_status[2]} + {bonus} = {pre_score + bonus} 的情况下\n"
            for rank_result in rank_results:
                required_score = await required_score_for_rank(rank_result, pre_status, rank, mode)
                if required_score > 0:
                    msg += f"达成等级 {rank_result} 需要的最低スコア为: {math.ceil(required_score)}\n"

        elif mode == "nia":
            msg += f"在三维为 {pre_status[0]} + {pre_status[1]} + {pre_status[2]} = {pre_score} 的情况下\n"
            for rank_result in rank_results:
                required_score = await required_score_for_fans(rank_result, pre_status, mode)
                fans_rk = await fans_rank(required_score)
                if required_score > 0:
                    msg += f"达成等级 {rank_result} 需要的最低ランク为: {math.ceil(required_score)} | 对应的ランク评级：{fans_rk}\n"
            nia_tip = "\n注：N.I.A.模式的最终选拔通过的奖励ランク算法缺失，ランク仅供参考"
            
        if len(msg.split("\n")) == 2:
            msg += "已经SS+确定了捏！\n"
            
        msg = msg.rstrip("\n")
        await bot.send(ev,  msg + nia_tip)

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
        fans = 0
        mode = "master"
        msg = ""
        msg += f"在三维为 {pre_status[0]} + {pre_status[1]} + {pre_status[2]} + {bonus} = {pre_score + bonus} 的情况下\n"
        rank_results = ["SS+", "SS", "S+", "S", "A+", "A"]
        for rank_result in rank_results:
            required_score = await required_score_for_rank(rank_result, pre_status, rank, mode, fans)

            if required_score > 0:
                msg += f"达成等级 {rank_result} 需要的最低スコア为: {math.ceil(required_score)}\n"

        msg = msg.rstrip("\n")
        await bot.send(ev,  msg)

    else:
        await bot.send(ev, help)