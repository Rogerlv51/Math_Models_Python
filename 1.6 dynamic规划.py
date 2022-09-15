# 动态规划常用于解决例如背包问题，还有最优解问题，其基本思想是把大问题递归地分成小问题解决
# 核心思想是创建一个表存储每一步的策略，以期最终找到最优解策略

# 例题，一个背包问题，最大容量不超过6斤，问如何价值最大化？当然背包问题常用贪心算法处理
def dynamic_p() -> list:       # 结果以列表形式存储
    # 先把所有能装的东西列出来
    items = [
        {"name": "水", "weight": 3, "value": 10},
        {"name": "书", "weight": 1, "value": 3},
        {"name": "食物", "weight": 2, "value": 9},
        {"name": "小刀", "weight": 3, "value": 4},
        {"name": "衣物", "weight": 2, "value": 5},
        {"name": "手机", "weight": 1, "value": 10},
    ]
    max_capacity = 6                # 约束条件，最大容量
    # 创建一个策略列表，动态规划本质上就是要把这个表填完整
    # 所有可能装的容量一共7种，0,1,2,3,4,5,6斤，总共6种物品，所以是49个表值，
    # 根据动态规划算法的原则，最优解显然就存在表的最后一个值
    dp = [[0] * (max_capacity + 1) for _ in range(len(items) + 1)]
    print(dp)

    # 第一行第一列都是0，所以从第一行第一列开始，具体见表参考网上步骤
    for row in range(1, len(items)+1):
        for col in range(1, max_capacity+1):
            weight = items[row-1]["weight"]    # 获取当前物品的重量
            value = items[row-1]["value"]      # 获取当前物品的价值
            if weight > col:      # 如果物品的重量大于当前背包的容量
                dp[row][col] = dp[row-1][col]    # 则当前位置的值保持跟上一行同一位置一样
            else:
                # 如果当前重量小于背包总量，则要比较当前价值打上剩余重量的最大价值和之前最优解的大小
                dp[row][col] = max(value + dp[row-1][col-weight], dp[row-1][col])
    return dp

if __name__ == "__main__":
    dp = dynamic_p()
    print(dp[-1][-1])