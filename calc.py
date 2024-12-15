import math

# 偶像参数计算
async def status_calc(mode, pre_status, rank):
    if mode == "regular":
        status_limis = 1200
    elif mode == "pro":
        status_limis = 1500
    elif mode == "master":
        status_limis = 1800

    if rank == 1:
        status_bouns = 30
    elif rank == 2:
        status_bouns = 20
    elif rank == 3:
        status_bouns = 10

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


# 奖励分计算
async def score_bonus(score):
    # 每个阶段的最大值和倍率
    thresholds = [(5000, 0.3), (10000, 0.15), (20000, 0.08), (30000, 0.04), (40000, 0.02), (float('inf'), 0.01)]

    total_score = 0
    prev_threshold = 0

    for threshold, multiplier in thresholds:
        if score > prev_threshold:
            # 计算当前区间的分数范围
            if score <= threshold:
                # 如果分数在当前区间内，计算当前区间的得分
                segment_score = math.floor((score - prev_threshold) * multiplier)
                total_score += segment_score
                break
            else:
                # 如果分数超过当前区间的最大值，计算该区间的最大得分
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


# 计算最终的评价等级
async def calculate_rank(evaluation_score):
    if evaluation_score >= 18000:
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


# 根据等级反推需要的score
async def required_score_for_rank(target_rank, pre_status, rank, mode):
    # 计算status和rank_score
    status = await status_calc(mode, pre_status, rank)
    rank_score = await rank_bonust(rank)

    # 目标等级对应的总分
    rank_thresholds = {
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

    async def find_required_score(required_total_score):
        low, high = 0, 10000000
        while high - low > 0.1:
            mid = (low + high) / 2
            bonus = await score_bonus(mid)
            total = status + bonus + rank_score
            if total < required_total_score:
                low = mid
            else:
                high = mid
        return low

    required_score = await find_required_score(required_total_score)

    return required_score