from __future__ import print_function
# import fcntl
# import termios
# import struct
# import cProfile
# import socket
import datetime
import getpass
import math
import multiprocessing
import os
import platform
import site
import struct
import sys
from calendar import month
from datetime import date
from os import *
from os.path import *
from subprocess import call
import time


class Program2:
    @staticmethod
    def Version():
        print("Python version")
        print(sys.version)
        print("Version info.")
        print(sys.version_info)


# ob = Program2()
# ob.Version()


class Program3:
    @staticmethod
    def date_time():
        now = datetime.datetime.now()
        print("Current date and time")
        print(now.strftime("%Y-%m-%d\n%H:%M:%S"))


# ob = Program3()
# ob.date_time()


class Program4:
    @staticmethod
    def area_of_circle(radius):
        pi = 22 / 7.0
        area = pi * radius ** 2
        print(area)


# ob = Program4()
# ob.area_of_circle(float(input("Enter the radius : ")))


class Program5:
    def __init__(self, nameofuser):
        self.name = nameofuser.lower()
        self.rev = ""

    def __reversed__(self):
        for i in range(len(self.name) - 1, -1, -1):
            self.rev += self.name[i]
        print(self.name)
        print(self.rev)


# ob = Program5(input('Enter your name : '))
# ob.__reversed__()

class Program6:
    def __init__(self, input):
        self.input = input
        self.flist = []
        self.num = ""
        self.flag = 0
        self.tuple = ()
        self.list = []

    def List(self):
        for i in range(0, len(self.input), 1):
            if self.input[i] == ',' or self.input[i] == ' ':
                self.flist.append(int(self.num))
                self.num = ""
                continue
            self.num += self.input[i]
        self.flist.append(int(self.num))
        print(self.flist)
        print(tuple(self.flist))

    def func_list(self):
        values = input("Input some comma separated numbers : ")
        self.list = values.split(",")
        self.tuple = tuple(self.list)
        print('List : ', self.list)
        print('Tuple : ', self.tuple)


# ob = Program6(input('Enter numbers with commas : '))
# ob.List()
# ob.func_list()


class Program7:
    @staticmethod
    def extension():
        filename = input("Input the Filename: ")
        f_extns = filename.split(".")
        print("The extension of the file is : " + repr(f_extns[-1]))


# ob = Program7()
# ob.extension()


class Program8:
    def __init__(self, array):
        self.array = array
        self.fs = ""
        self.ls = ""
        self.sub = self.array[self.array.rindex(","):]

    def values(self):
        self.fs = self.array[self.array.index('"') + 1: self.array.index('"', self.array.index('"') + 1)]
        self.ls = self.sub[self.sub.index('"') + 1: self.sub.rindex('"')]
        print(self.fs)
        print(self.ls)


# ob = Program8(input('Enter an array : '))
# ob.values()


class Program9:
    @staticmethod
    def schedule(input):
        try:
            input = input[input.index('(') + 1:input.index(')')]
            sinput = input.split(",")
            for i in range(len(sinput)):
                print(sinput[i], "/", end="")

        except Exception as e:
            print(e)
            sinput = input.split(",")
            for i in range(len(sinput)):
                print(sinput[i], "/", end="")

    @staticmethod
    def schedule_fun(exam_st_date):
        print("The examination will start from : %i / %i / %i" % exam_st_date)


# ob = Program9()
# ob.schedule(input("Input date of examination : "))
# ob.schedule_fun(input("Input date of examination : "))


class Program10:
    @staticmethod
    def add_(n):
        print(n + (10 * n + n) + (100 * n + 10 * n + n))

    @staticmethod
    def add_func():
        a = int(input("Input an integer : "))
        n1 = int("%s" % a)
        n2 = int("%s%s" % (a, a))
        n3 = int("%s%s%s" % (a, a, a))
        print(n1 + n2 + n3)


# ob = Program10()
# ob.add_(int(input("Enter an Integer --> ")))
# ob.add_func()


class Program11:
    @staticmethod
    def description():
        print(abs.__doc__)


# ob = Program11()
# ob.description()


class Program12:
    @staticmethod
    def calender(y, m):
        print(month(y, m, 4))  # here width is 4


# ob = Program12()
# ob.calender(int(input("Enter the year --> ")), int(input("Enter the month --> ")))


class Program13:
    @staticmethod
    def multilineop():
        print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
here doc string --------> example
""")


# ob = Program13()
# ob.multilineop()


class Program14:
    @staticmethod
    def days_gap(thedate, gap=0):
        try:
            d1 = thedate[:thedate.index(')') + 1]
            d2 = thedate[thedate.index(',', thedate.index(')')) + 1:]
            d1 = d1[d1.index('(') + 1:d1.index(')')].split(',')
            d2 = d2[d2.index('(') + 1:d2.index(')')].split(',')
        except ValueError as e:
            print("Value not in correct format,", e)
            d1 = ['0', '0', '0']
            d2 = ['0', '0', '0']
        gap += (int(d1[0]) * 365) - (int(d2[0]) * 365)
        gap += (int(d1[1]) * 30) - (int(d2[1]) * 30)
        gap += int(d1[2]) - int(d2[2])
        if gap < 0:
            print("second date is greater : ", int(gap - (2 * gap)))
        else:
            print(gap)

    @staticmethod
    def days_gap_func():
        f_date = date(2013, 11, 30)
        l_date = date(2015, 12, 31)
        delta = l_date - f_date
        print(date.today())
        print(delta.days)


# ob = Program14()
# ob.days_gap(input("Enter the date : "))
# ob.days_gap_func()


class Program15:
    @staticmethod
    def Volume_Sphere(radius):
        pi = 22 / 7.0
        print((4.0 / 3.0) * pi * radius ** 3)


# ob = Program15()
# ob.Volume_Sphere(float(input("Enter the radius of the sphere : ")))


class Program16:
    @staticmethod
    def seventeen_diff(n):
        if n > 17:
            diff = 2 * (n - 17)
        else:
            diff = 17 - n
        print(diff)


# ob = Program16()
# b.seventeen_diff(int(input("Enter a number : ")))


class Program17:
    @staticmethod
    def within100(n):
        if (abs(1000 - n)) <= 100:
            print('the number is within 1000')
        elif (abs(2000 - n)) <= 100:
            print('The number is within 2000')
        else:
            print('The number is out of the world')

    @staticmethod
    def iswithin1000(n):
        return (abs(1000 - n) <= 100) or (abs(2000 - n) <= 100)


# ob = Program17()
# ob.within100(int(input('Enter a number --> ')))
# print(ob.iswithin1000(int(input('Enter a number --> '))))


class Program18:
    @staticmethod
    def sum3(a, b, c):
        if a == b == c:
            print(9 * a)
        else:
            print(a + b + c)


# ob = Program18()
# ob.sum3(int(input('Enter the 1st number : ')), int(input('Enter the 2nd number : ')), int(input('Enter the 3rd number : ')))


class Program19:
    @staticmethod
    def Is(str):
        if str[:2] == "Is" or str[:2] == "is" or str[:2] == "IS":
            print(str)
        else:
            print("Is" + str)


# ob = Program19()
# ob.Is(input("Enter a sentence : "))


class Program20:
    @staticmethod
    def copyString(str, n, nstr=""):
        if n < 0:
            for i in range(len(str) - 1, -1, -1):
                nstr += str[i]
        else:
            nstr = str
        print(nstr * abs(n))


# ob = Program20()
# ob.copyString(input("Enter a string : "), int(input("Enter no. of repetitions : ")))


class Program21:
    @staticmethod
    def odd_even(n):
        if n % 2 == 0:
            print("The number is even")
        else:
            print("The number is odd")


# ob = Program21()
# ob.odd_even(int(input("Enter a number --> ")))


class Program22:
    @staticmethod
    def listwith4(uilist):
        try:
            slist = uilist[uilist.index('[') + 1:uilist.index(']')]
        except ValueError as e:
            print('You forgot the brackets....', e)
            print('Anyways.....')
            slist = uilist
        slist = slist.split(',')
        print(slist)
        ct = 0
        for i in slist:
            print(int(i))
            if int(i) == 4:
                ct += 1
        if ct == 0:
            print("There are no 4s")
        elif ct > 1:
            print('There are {} fours'.format(ct))
        else:
            print('There is 1 four')


# ob = Program22()
# ob.listwith4(input("Enter a list : "))


class Program23:
    @staticmethod
    def first2copy(input, n):
        for i in range(n):
            print(input[:2], end="")


# ob = Program23()
# ob.first2copy(input("Enter the String : "), int(input("Enter the number of iterations : ")))


class Program24:
    @staticmethod
    def vowelcheck(character):
        character = character.lower()
        if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
            return True
        else:
            return False


"""ob = Program24()
a = input("Input a character : ")
if ob.vowelcheck(a):
    print("It is a vowel")
else:
    print("It is not a vowel")"""


class Program25:
    @staticmethod
    def searchval(List, sval):
        try:
            nlist = List[List.index('[') + 1:List.index(']')]
        except ValueError:
            nlist = List
        vals = nlist.split(',')
        for i in vals:
            if sval.lower() == i.lower():
                return True
        return False


"""ob = Program25()
List = input('Enter the list : ')
sval = input('Enter the search value : ')
if ob.searchval(List, sval):
    print("The value is in the list")
else:
    print("value not found")"""


class Program26:
    @staticmethod
    def horizontalhisto(nums):
        n = nums.split(',')
        for i in range(len(n)):
            for j in range(int(n[i])):
                print('@', end=" ")
            print()

    @staticmethod
    def verticalhisto(nums):
        pass


# ob = Program26()
# ob.horizontalhisto(input('Enter numbers separated by commas : '))


class Program27:
    @staticmethod
    def concat(inplist):
        op = ""
        list = inplist.split(',')
        for i in list:
            op = op + i
        print(op)


# ob = Program27()
# ob.concat(input("Enter values separated by commas : "))


class Program28:
    @staticmethod
    def even_list(inputlist):
        try:
            flist = inputlist[inputlist.index('[') + 1:inputlist.index(']')].split(',')
        except ValueError:
            flist = inputlist
        evenlist = []
        odds = 0
        for i in range(len(flist)):
            flist[i] = int(flist[i])
        for i in flist:
            if i == 237:
                break
            if i % 2 == 0:
                evenlist.append(i)
            else:
                odds += 1
        for i in evenlist:
            print(i, end=", ")
        print()
        print("No.of even numbers is {}".format(len(evenlist)))
        print("No.of odd numbers is {}".format(odds))


# ob = Program28()
# ob.even_list(input('Enter a list of numbers : '))


class Program29:
    def __init__(self, set):
        self.set = set

    def __sub__(self, other):
        self.set = self.set[self.set.index('[') + 1: self.set.index(']')].split(',')
        other.set = other.set[other.set.index('[') + 1: other.set.index(']')].split(',')
        self.sublist = []
        for i in self.set:
            flag = 0
            for j in other.set:
                if i.lower().strip() == j.lower().strip():
                    flag += 1
            if flag == 0:
                self.sublist.append(i)
        return set(self.set), set(other.set), set(self.sublist)


# set_1 = Program29(input("Enter the first set : "))
# set_2 = Program29(input("Enter the second set : "))
# print(set_1 - set_2)


class Program30:
    @staticmethod
    def area_triangle(b, h):
        print(0.5 * b * h)


# ob = Program30()
# ob.area_triangle(float(input('Enter the base : ')), float(input('Enter the height : ')))


class Program31:
    @staticmethod
    def GCD(a, b):
        if b == 0:
            return a
        else:
            # return ob.GCD(b, a % b)
            pass


# ob = Program31()
# print("GCD = ", ob.GCD(int(input('Enter a value : ')), int(input('Enter another value : '))))


class Program32:
    @staticmethod
    def LCM_1(a, b, product):
        global prod
        if b == 0:
            GCD = a
            LCM = product / GCD
            return LCM
        else:
            # return ob.LCM_1(b, a % b, prod)
            pass


# ob = Program32()
# a = int(input('Enter a value : '))
# b = int(input('Enter another value : '))
# prod = a * b
# print("LCM = ", ob.LCM_1(a, b, prod))


class Program33:
    @staticmethod
    def sum(a, b, c):
        if a == b or b == c or a == c:
            sum = 0
        else:
            sum = a + b + c
        print(sum)


# ob = Program33()
# ob.sum(int(input('Enter a no. : ')), int(input('Enter a no. : ')), int(input('Enter a no. : ')))


class Program34:
    @staticmethod
    def sum2(a, b):
        sum = a + b
        if sum in range(15, 20):
            print('0')
        else:
            print(sum)


# ob = Program34()
# ob.sum2(int(input('Enter a no. : ')), int(input('Enter another no. : ')))


class Program35:
    @staticmethod
    def diffsumequal(a, b):
        if a == b or a + b == 5 or abs(a - b) == 5:
            return True
        else:
            return False


"""
ob = Program35()
if ob.diffsumequal(int(input('Enter a no. : ')), int(input('Enter another no. : '))):
    print("True")
else:
    print("False")
"""


class Program36:
    @staticmethod
    def intobsum(ob1, ob2):
        if not (isinstance(ob1, int) and isinstance(ob2, int)):
            raise TypeError('Input must be integer')
        print("Sum =", ob1 + ob2)


# ob = Program36()
# ob.intobsum(6, 5)


class Program37:
    @staticmethod
    def personaldetails(nameofuser, age, *address):
        print("Name =", nameofuser)
        print("Age =", age)
        print("Address = ", end="")
        for i in address:
            print(i, end="")


# ob = Program37()
# ob.personaldetails(input("Enter the name : "), input("Enter the age : "), input("Enter the address : "))


class Program38:
    @staticmethod
    def squareidentity(x, y):
        print("({} + {})^2 = {}".format(x, y, (x + y) ** 2))


# ob = Program38()
# ob.squareidentity(int(input("Enter first number : ")), int(input("Enter second number : ")))


class Program39:
    @staticmethod
    def SI(P, rate, years):
        amount = P * (1 + (rate / 100)) ** years
        print("The final amount is = ", amount)


# ob = Program39()
# ob.SI(float(input("Enter Principle amount : ")), float(input("Enter rate of interest : ")), float(input("Enter number of years : ")))


class Program40:
    @staticmethod
    def distanceformula(first, second):
        first = first[first.index('[') + 1:first.index(']')].split(',')
        second = second[second.index('[') + 1:second.index(']')].split(',')
        distance = math.sqrt(((int(second[0]) - int(first[0])) ** 2) + ((int(second[1]) - int(first[1])) ** 2))
        print("The distance between the two coordinates =", distance)


# ob = Program40()
# ob.distanceformula(input("Enter the first co-ordinate : "), input("Enter the second co-ordinate : "))


class Program41:
    @staticmethod
    def findfile():
        pass
        # open('abc.txt', 'w')
        # print(isfile('abc.txt'))


# ob = Program41()
# ob.findfile()


class Program42:
    @staticmethod
    def bitoperation():
        print(struct.calcsize("P") * 8, "bits")


# ob = Program42()
# ob.bitoperation()


class Program43:
    @staticmethod
    def OSinfo():
        print(name)
        print(platform.system())
        print(platform.release())


# ob = Program43()
# ob.OSinfo()


class Program44:
    @staticmethod
    def locatepackage():
        print(site.getsitepackages())


# ob = Program44()
# ob.locatepackage()


class Program45:
    @staticmethod
    def extcommand():
        call(["ls", "-l"])


# ob = Program45
# ob.extcommand()


class Program46:
    @staticmethod
    def path():
        print("Current File Name : ", realpath(__file__))


# ob = Program46()
# ob.path()


class Program47:
    @staticmethod
    def CPUcount():
        print(multiprocessing.cpu_count())


# ob = Program47()
# ob.CPUcount()


class Program48:
    @staticmethod
    def parsedatatype():
        n = "246.2458"
        print(float(n))
        print(int(float(n)))


# ob = Program48()
# ob.parsedatatype()


class Program49:
    @staticmethod
    def filesindirectory():
        files_list = [f for f in listdir('/home/students') if isfile(join('/home/students', f))]
        print(files_list)


# ob = Program49()
# ob.filesindirectory()


class Program50:
    @staticmethod
    def nonewlineorspace():
        for i in range(0, 10):
            print('*', end="")
        print("\n")


# ob = Program50()
# ob.nonewlineorspace()

"""
class Program51:
    @staticmethod
    def profiling():
        def sum():
            print(1 + 2)

        cProfile.run('sum()')
"""


# ob = Program51()
# ob.profiling()


class Program52:
    @staticmethod
    def printstderr():
        def eprint(*args, **kwargs):
            print(*args, file=sys.stderr, **kwargs)

        eprint("abc", "efg", "xyz", sep="--")


# ob = Program52()
# ob.printstderr()


class Program53:
    @staticmethod
    def environmentvariables():
        # Access all environment variables
        print('*----------------------------------*')
        print(os.environ)
        print('*----------------------------------*')
        # Access a particular environment variable
        print(os.environ['HOME'])
        print('*----------------------------------*')
        print(os.environ['PATH'])
        print('*----------------------------------*')


# ob = Program53()
# ob.environmentvariables()


class Program54:
    @staticmethod
    def username():
        print(getpass.getuser())


# ob = Program54()
# ob.username()

"""
class Program55:
    @staticmethod
    def get_local_host():
        print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
                            if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
                                                                  s.getsockname()[0], s.close()) for s in
                                                                 [socket.socket(socket.AF_INET,
                                                                                socket.SOCK_DGRAM)]][0][1]]) if l][0][
                  0])


# ob = Program55()
# ob.get_local_host()
"""

"""class Program56:
    @staticmethod
    def size_of_terminal():
        def terminal_size():
            th, tw, hp, wp = struct.unpack('HHHH',
                                           fcntl.ioctl(0, termios.TIOCGWINSZ,
                                                       struct.pack('HHHH', 0, 0, 0, 0)))
            return tw, th

        print('Number of columns and Rows: ', terminal_size())


# ob = Program56()
# ob.size_of_terminal()"""


class Program57:
    @staticmethod
    def execution_time():
        def sum_of_n_numbers(sum):
            start_time = time.time()
            s = 0
            for i in range(1, sum + 10000):
                s = s + i
            end_time = time.time()
            return s, end_time - start_time

        n = 5
        print("\nTime to sum of 1 to ", n, " and required time to calculate is :", sum_of_n_numbers(n))


# ob = Program57()
# ob.execution_time()


class Program58:
    @staticmethod
    def sum_of_n(n, sum=0):
        for i in range(n + 1):
            sum += i
        print("Sum of {} numbers is {}".format(n, sum))


# ob = Program58()
# ob.sum_of_n(int(input("Enter the number of iterations : ")))


class Program59:
    @staticmethod
    def feet_to_cm(fi):
        try:
            feet = float(fi[:fi.index('f')])
            inches = feet * 12 + float(fi[fi.index('t') + 1:fi.index('i')])
        except ValueError:
            feet = float(fi)
            inches = feet * 12
        cm = inches * 2.54
        print(cm)


# ob = Program59()
# ob.feet_to_cm(input("Enter height in feet and inches : "))


class Program60:
    @staticmethod
    def hypotenuse(s1, s2):
        print(math.sqrt((s1 ** 2) + (s2 ** 2)))


# ob = Program60()
# ob.hypotenuse(float(input("Enter one side : ")), float(input("Enter the other side : ")))


class Program61:
    @staticmethod
    def feet_to_many(fi):
        try:
            feet = float(fi[:fi.index('f')])
        except ValueError:
            feet = float(fi)
        inches = feet * 12
        yards = feet / 3.0
        miles = feet / 5280.0
        print("{} feet in inches is {}.".format(feet, inches))
        print("{} feet in yards is {}.".format(feet, yards))
        print("{} feet in miles is {}.".format(feet, miles))

# ob = Program61()
# ob.feet_to_many(input("Enter distance in feet : "))


class Program61:
    @staticmethod
    def toseconds(days, hours, minutes, seconds):
        tseconds = (days * 3600 * 24) + (hours * 3600) + (minutes * 60) + seconds
        print("Total no. of seconds =", tseconds)


# ob = Program61()
# ob.toseconds(int(input("Enter days : ")), int(input("Enter hours : ")), int(input("Enter minutes : ")), int(input("Enter seconds : ")))


class Program62:
    @staticmethod
    def absolute_file_path(path_fname):
        return os.path.abspath('path_fname')


ob = Program62()
print("Absolute file path: ", ob.absolute_file_path("test.txt"))
