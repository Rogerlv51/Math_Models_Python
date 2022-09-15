import numpy as np
import matplotlib.pyplot as plt


# 建立“蚂蚁”类
class Ant(object):
    def __init__(self, path):
        self.path = path                       # 蚂蚁当前迭代整体路径
        self.length = self.calc_length(path)   # 蚂蚁当前迭代整体路径长度

    def calc_length(self, path_):              # path=[A, B, C, D, A]注意路径闭环
        length_ = 0
        for i in range(len(path_)-1):
            delta = (path_[i].x - path_[i+1].x, path_[i].y - path_[i+1].y)
            length_ += np.linalg.norm(delta)
        return length_

    @staticmethod
    def calc_len(A, B):                        # 静态方法，计算城市A与城市B之间的距离
        return np.linalg.norm((A.x - B.x, A.y - B.y))


# 建立“城市”类
class City(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


# 建立“路径”类
class Path(object):
    def __init__(self, A):                     # A为起始城市
        self.path = [A, A]

    def add_path(self, B):                     # 追加路径信息，方便计算整体路径长度
        self.path.append(B)
        self.path[-1], self.path[-2] = self.path[-2], self.path[-1]


# 构建“蚁群算法”的主体
class ACO(object):
    def __init__(self, ant_num=50, maxIter=300, alpha=1, beta=5, rho=0.1, Q=1):
        self.ants_num = ant_num   # 蚂蚁个数
        self.maxIter = maxIter    # 蚁群最大迭代次数
        self.alpha = alpha        # 信息启发式因子
        self.beta = beta          # 期望启发式因子
        self.rho = rho            # 信息素挥发速度
        self.Q = Q                # 信息素强度
        ###########################
        self.deal_data('coordinates.dat')                         # 提取所有城市的坐标信息
        ###########################
        self.path_seed = np.zeros(self.ants_num).astype(int)      # 记录一次迭代过程中每个蚂蚁的初始城市下标
        self.ants_info = np.zeros((self.maxIter, self.ants_num))  # 记录每次迭代后所有蚂蚁的路径长度信息
        self.best_path = np.zeros(self.maxIter)                   # 记录每次迭代后整个蚁群的“历史”最短路径长度
        ###########################
        self.solve()              # 完成算法的迭代更新
        self.display()            # 数据可视化展示

    def deal_data(self, filename):
        with open(filename, 'rt') as f:
            temp_list = list(line.split() for line in f)                                   # 临时存储提取出来的坐标信息
        self.cities_num = len(temp_list)                                                   # 1. 获取城市个数
        self.cities = list(City(float(item[0]), float(item[1])) for item in temp_list)     # 2. 构建城市列表
        self.city_dist_mat = np.zeros((self.cities_num, self.cities_num))                  # 3. 构建城市距离矩阵
        for i in range(self.cities_num):
            A = self.cities[i]
            for j in range(i, self.cities_num):
                B = self.cities[j]
                self.city_dist_mat[i][j] = self.city_dist_mat[j][i] = Ant.calc_len(A, B)
        self.phero_mat = np.ones((self.cities_num, self.cities_num))                       # 4. 初始化信息素矩阵
        # self.phero_upper_bound = self.phero_mat.max() * 1.2                              ###信息素浓度上限
        self.eta_mat = 1/(self.city_dist_mat + np.diag([np.inf]*self.cities_num))          # 5. 初始化启发函数矩阵

    def solve(self):
        iterNum = 0                                                            # 当前迭代次数
        while iterNum < self.maxIter:
            self.random_seed()                                                 # 使整个蚁群产生随机的起始点
            delta_phero_mat = np.zeros((self.cities_num, self.cities_num))     # 初始化每次迭代后信息素矩阵的增量
            ##########################################################################
            for i in range(self.ants_num):
                city_index1 = self.path_seed[i]                                # 每只蚂蚁访问的第一个城市下标
                ant_path = Path(self.cities[city_index1])                      # 记录每只蚂蚁访问过的城市
                tabu = [city_index1]                                           # 记录每只蚂蚁访问过的城市下标，禁忌城市下标列表
                non_tabu = list(set(range(self.cities_num)) - set(tabu))
                for j in range(self.cities_num-1):                             # 对余下的城市进行访问
                    up_proba = np.zeros(self.cities_num-len(tabu))             # 初始化状态迁移概率的分子
                    for k in range(self.cities_num-len(tabu)):
                        up_proba[k] = np.power(self.phero_mat[city_index1][non_tabu[k]], self.alpha) * \
                        np.power(self.eta_mat[city_index1][non_tabu[k]], self.beta)
                    proba = up_proba/sum(up_proba)                             # 每条可能子路径上的状态迁移概率
                    while True:                                                # 提取出下一个城市的下标
                        random_num = np.random.rand()
                        index_need = np.where(proba > random_num)[0]
                        if len(index_need) > 0:
                            city_index2 = non_tabu[index_need[0]]
                            break
                    ant_path.add_path(self.cities[city_index2])
                    tabu.append(city_index2)
                    non_tabu = list(set(range(self.cities_num)) - set(tabu))
                    city_index1 = city_index2
                self.ants_info[iterNum][i] = Ant(ant_path.path).length
                if iterNum == 0 and i == 0:                                    # 完成对最佳路径城市的记录
                    self.best_cities = ant_path.path
                else:
                    if self.ants_info[iterNum][i] < Ant(self.best_cities).length: self.best_cities = ant_path.path
                tabu.append(tabu[0])                                           # 每次迭代完成后，使禁忌城市下标列表形成完整闭环
                for l in range(self.cities_num):
                    delta_phero_mat[tabu[l]][tabu[l+1]] += self.Q/self.ants_info[iterNum][i]

            self.best_path[iterNum] = Ant(self.best_cities).length

            self.update_phero_mat(delta_phero_mat)                             # 更新信息素矩阵
            iterNum += 1

    def update_phero_mat(self, delta):
        self.phero_mat = (1 - self.rho) * self.phero_mat + delta
        # self.phero_mat = np.where(self.phero_mat > self.phero_upper_bound, self.phero_upper_bound, self.phero_mat) # 判断是否超过浓度上限

    def random_seed(self):                                                     # 产生随机的起始点下表，尽量保证所有蚂蚁的起始点不同
        if self.ants_num <= self.cities_num:                                   # 蚂蚁数 <= 城市数
            self.path_seed[:] = np.random.permutation(range(self.cities_num))[:self.ants_num]
        else:                                                                  # 蚂蚁数 > 城市数
            self.path_seed[:self.cities_num] = np.random.permutation(range(self.cities_num))
            temp_index = self.cities_num
            while temp_index + self.cities_num <= self.ants_num:
                self.path_seed[temp_index:temp_index + self.cities_num] = np.random.permutation(range(self.cities_num))
                temp_index += self.cities_num
            temp_left = self.ants_num % self.cities_num
            if temp_left != 0:
                self.path_seed[temp_index:] = np.random.permutation(range(self.cities_num))[:temp_left]

    def display(self):                                                         # 数据可视化展示
        plt.figure(figsize=(6, 10))
        plt.subplot(211)
        plt.plot(self.ants_info, 'g.')
        plt.plot(self.best_path, 'r-', label='history_best')
        plt.xlabel('Iteration')
        plt.ylabel('length')
        plt.legend()
        plt.subplot(212)
        plt.plot(list(city.x for city in self.best_cities), list(city.y for city in self.best_cities), 'g-')
        plt.plot(list(city.x for city in self.best_cities), list(city.y for city in self.best_cities), 'r.')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.savefig('ACO.png', dpi=500)
        plt.show()
        plt.close()


ACO()