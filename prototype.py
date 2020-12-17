import copy

class Robot:
    def __init__(self, job):
        self.job = job

    def clone(self):
        return self

    def deepClone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return "Job = " + self.job

if __name__ == "__main__":
    robot1 = Robot("Kill People")
    robot2 = robot1.deepClone()
    print(robot1)
    print(robot2)
    print("----")
    robot1.job = "Test People"
    print(robot1)
    print(robot2)