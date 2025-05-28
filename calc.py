import math

# 偶像参数计算
async def status_calc(mode, pre_status, rank):
    if mode == "regular":
        status_limis = 1200
    elif mode == "pro":
        status_limis = 1500
    elif mode == "master":
        status_limis = 1800
    elif mode == "nia":
        status_limis = 2000

    if rank == 1:
        status_bouns = 30
    elif rank == 2:
        status_bouns = 20
    elif rank == 3:
        status_bouns = 10
    elif rank == 0:
        status_bouns = 0


    vo = pre_status[0] + status_bouns
    da = pre_status[1] + status_bouns
    vi = pre_status[2] + status_bouns

    if vo >= status_limis:
        vo = status_limis
    if da >= status_limis:
        da = status_limis
    if vi >= status_limis:
        vi = status_limis

    status = vo + da + vi

    status = int(math.floor(status * 2.3))
    return status


# 初分数计算
async def score_bonus(score):
    thresholds = [(5000, 0.3), (10000, 0.15), (20000, 0.08), (30000, 0.04), (40000, 0.02), (float('inf'), 0.01)]

    total_score = 0
    prev_threshold = 0

    for threshold, multiplier in thresholds:
        if score > prev_threshold:
            if score <= threshold:
                segment_score = math.floor((score - prev_threshold) * multiplier)
                total_score += segment_score
                break
            else:
                segment_score = math.floor((threshold - prev_threshold) * multiplier)
                total_score += segment_score
        prev_threshold = threshold

    return total_score

# N.I.A.分数计算
async def rank_bonus(rank):
    thresholds = [(20000, 0.1), (40000, 0.085), (60000, 0.07), (80000, 0.065), (100000, 0.06), (float('inf'), 0.055)]

    total_score = 0
    prev_threshold = 0

    for threshold, multiplier in thresholds:
        if rank > prev_threshold:
            if rank <= threshold:
                segment_score = math.floor((rank - prev_threshold) * multiplier)
                total_score += segment_score
                break
            else:
                segment_score = math.floor((threshold - prev_threshold) * multiplier)
                total_score += segment_score
        prev_threshold = threshold

    return total_score

# 排名加成
async def rank_bonust(rank):
    rank_score = 0
    if rank == 1:
        rank_score = 1700
    elif rank == 2:
        rank_score = 900
    elif rank == 3:
        rank_score = 500
    return rank_score


# 最终的评价等级
async def calculate_rank(evaluation_score):
    if evaluation_score >= 23000:
        return "SSS+"
    elif evaluation_score >= 20000:
        return "SSS"
    elif evaluation_score >= 18000:
        return "SS+"
    elif evaluation_score >= 16000:
        return "SS"
    elif evaluation_score >= 14500:
        return "S+"
    elif evaluation_score >= 13000:
        return "S"
    elif evaluation_score >= 11500:
        return "A+"
    elif evaluation_score >= 10000:
        return "A"
    elif evaluation_score >= 8000:
        return "B+"
    elif evaluation_score >= 6000:
        return "B"
    elif evaluation_score >= 4500:
        return "C+"
    elif evaluation_score >= 3000:
        return "C"
    else:
        return "D"

# ランク对应评价
async def fans_rank(fans):
    if fans >= 160000:
        return "SSS+"
    elif fans >= 140000:
        return "SSS"
    elif fans >= 120000:
        return "SS+"
    elif fans >= 100000:
        return "SS"
    elif fans >= 80000:
        return "S+"
    elif fans >= 60000:
        return "S"    
    elif fans >= 40000:
        return "A+"
    elif fans >= 30000:
        return "A"
    elif fans >= 25000:
        return "B+"
    elif fans >= 20000:
        return "B"
    elif fans >= 10000:
        return "C"
    elif fans >= 5000:
        return "D"
    else:
        return "E"

# スコア逆算部分
async def required_score_for_rank(target_rank, pre_status, rank, mode):

    status = await status_calc(mode, pre_status, rank)
    rank_score = await rank_bonust(rank)

    rank_thresholds = {
        "SSS+": 23000,
        "SSS": 20000,
        "SS+": 18000,
        "SS": 16000,
        "S+": 14500,
        "S": 13000,
        "A+": 11500,
        "A": 10000,
        "B+": 8000,
        "B": 6000,
        "C+": 4500,
        "C": 3000,
        "D": 0
    }

    required_total_score = rank_thresholds.get(target_rank, 0)

    async def produce_score(required_total_score):
        low = 0
        high = 18000000
        while True:
            bonus = await score_bonus(high)
            total = status + bonus + rank_score
            if total >= required_total_score:
                break
            high *= 2
            
        while high - low > 0.1:
            mid = (low + high) / 2
            bonus = await score_bonus(mid)
            total = status + bonus + rank_score
            if total < required_total_score:
                low = mid
            else:
                high = mid

        return low

    required_score = await produce_score(required_total_score)

    return required_score


# ランク逆算部分
async def required_score_for_fans(target_rank, pre_status, mode):
    status = await status_calc(mode, pre_status, rank=0)

    rank_thresholds = {
        "SSS+": 23000,
        "SSS": 20000,
        "SS+": 18000,
        "SS": 16000,
        "S+": 14500,
        "S": 13000,
        "A+": 11500,
        "A": 10000,
        "B+": 8000,
        "B": 6000,
        "C+": 4500,
        "C": 3000,
        "D": 0
    }
    

    required_total_score = rank_thresholds.get(target_rank, 0)
    
    async def produce_score(required_total_score):
        low = 0
        high = 18000000
        while True:
            bonus = await rank_bonus(high)
            total = status + bonus
            if total >= required_total_score:
                break
            high *= 2
            
        while high - low > 0.1:
            mid = (low + high) / 2
            bonus = await rank_bonus(mid)
            total = status + bonus
            if total < required_total_score:
                low = mid
            else:
                high = mid

        return low

    required_score = await produce_score(required_total_score)

    return required_score