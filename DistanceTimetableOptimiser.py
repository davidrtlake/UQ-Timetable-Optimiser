

coordianates = {"30":(736,31), }

class Timetable():
    def __init__(self, courses):
        self.courses = courses

    def CreateTimetable(courses):
        pass

class Course():
    name = ""
    classes = []
    def __init__(self, name, classes):
        self.classes = classes
        self.name = name

    def PrintCourse(self):
        print("The course name is " + self.name + " and the class times are")
        for item in self.classes:
            for item in item.times:
                print(" " + str(item[0]) + " ")
        

class Class:
    times = []
    days = []
    buidlings = []
    length = 0;
    static = False
    def __init__(self, times, days, buildings, static):
        self.times = times
        self.days = days
        self.buildings = buildings
        self.static = static

    def PrintTimes():
        pass

CSSE2310Practical = Class([1000, 1150], [3], ["50"], True)
CSSE2310Lecture = Class([(1200, 1350), (1500, 1550)], [3, 4], ["27A", "49"],
                        True)
COMP3506Tute = Class([(1400, 1450), (1500, 1550), (1600, 1650),
                      (1700, 1750), (800, 850), (900, 950), (1200, 1250),
                      (1300, 1360), (900, 950), (1000, 1050),
                      (1100, 1150), (1100, 1150), (1100, 1150)],
                     [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 5],
                     ["01", "01", "09", "35", "83", "83", "09", "09",
                      "83", "09", "09", "09", "35"], False)
COMP3506Lecture = Class([(800, 1050)], [4], ["27A"], True)
CSSE2310 = Course("CSSE2310", [CSSE2310Practical, CSSE2310Lecture])
COMP3506 = Course("COMP3506", [COMP3506Tute, COMP3506Lecture])
COMP3506.PrintCourse()
