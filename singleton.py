'''
# Single
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Robot(metaclass=Singleton):
    def __init__(self):
        self.job = "Kill People"
    def __str__(self):
        return "Job = " + self.job
'''

class RobotBase:
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

class Robot(RobotBase):
    def __init__(self):
        self.job = "Kill People"

    def __str__(self):
        return "Job = " + self.job


if __name__ == "__main__":
    robot1 = Robot()
    robot2 = Robot()

    print(robot1)
    print(robot2)
    print(robot1 == robot2)