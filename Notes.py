from math import pow
from numpy import *
import sys
# from functools import *
from Calc import *

nums = [3, 2, 6, 8, 4, 6, 2, 9]
evens = list(filter(lambda n: n % 2 == 0, nums))
sys.setrecursionlimit(1000)
add(2, 1)
# from array import *
# u can call function using math and m so m.pow works use import math as m
a = 8
b = 2
c = 5
range(10)
comp = 6 + 9j
dou = 2.78
PI = 3.14
# PI is a constant so it is capital
String = " Aarish "
String2 = "Rocks"
# val = array('i', [5, 9, 8, 4, 2])
List = [24, 12, 36, 94, 14]
mixList = [2.8, 'Aarish', 34]
llist = [List, mixList]
tupple = (21, 36, 14, 25)
set = {22, 25, 14, 21, 5}
data = {1: 'Hydrogen', 2: 'Helium', 3: 'Lithium', 4: 'Beryllium', 5: 'Boron', 6: 'Carbon', 7: 'Nitrogen', 8: 'Oxygen',
        9: 'Fluorine', 10: 'Neon'}
AtomicNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Element = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']
prog = {'JS': 'Atom', 'CS': 'VS', 'Python': ['PyCharm', 'Sublime'], 'Java': {'JSE': 'Netbeans', 'JEE': 'Eclipse'}}
xa = pow(2, 1)
arr1 = array([1, 2, 3, 4, 5, 6])
arr = array([1, 2, 3, 4, 5])
arr2 = array([7, 8, 9, 10, 11, 2, 3, 4])
marr = array([
    [1, 2, 3],
    [4, 5, 6]
])
arr7 = marr.flatten()
"""(delimiter)(multi line comment)
0. #print is same as System.out.println

1. print(a+b)
   #addition
   
2. print(a-b)
   #subtraction
   
3. print(a/b) 
   #division(float value)
   
4. print(a*b)
   #multipication
   
5. print(a//b)
   #division(int value)
   
6. print(a**b)
   #a raised to b(Exponents)
   
7. print(a + b - c)
   #adds a and b then subtracts c from the sum(left to right)
   
8. print(a + b * c)
   #multiplies b and c then adds a(BODMAS)
   
9. print((a + b) * c)
   #adds a and b then multiplies c(brackets are priority)
   
10.print(a%b)
   #modulus(gives remainder)
   
11.print('Aarish')
   #prints "String"
   
12.print('Aarish's Laptop)
   #will give error as print stops at single quote after Aarish
   
13.print("Aarish's Laptop")
   #this will work as we used double quote
   
14.print('Aarish "Laptop"')
   #string should be different from inside , if double quote inside then single quote outside and vice-versa
   
15.print('Aarish\'s "laptop"')
   #backslash asks Python to to ignore single quote as a function
   
16.print("Aarish" + 'Aarish')
   #'+' acts as concatenation , both single quote and double quote can be used
   
17.print(10 * "Aarish")
   #prints the string ten times
   
18.print("Aarish\'\t s \nLaptop")
   #\t is tab and \n in new line
   
19.print(r"Aarish\'\t s \nLaptop")
   #the 'r' before the string prints the raw string and ignores the function
   
20.print(String + String2)
   #you can concatenate 2 strings
   
21.print(String + 'isAwesome')
   #it will print variable + string
   
22.print(String[0])
   #works like charAt(0)
   
23.print(String[-1])
   #negative numbers start from end to first
   
24.print(String[8])
   #gives error String Index Out of Bounds
   
25.print(String[0:3])
   #works like Substring does not give char at the last input position
   
26.print(String[0:-1])
   #still works 
   
27.print(String[1:])
   #if ending value is not specified string is from first value to the end
   
28.print(String[:4])
   #if starting value is not specified prints from start to the specified value
   
29.print(String[3:10])
   #although there is no value at 10 it will not give a error but it will print from position3 to the end
   
30.String[1:3] = 'Ha'
   #this statement gives a syntax error
   
31.String[1] = 'H'
   #this statement also gives a error as String values are fixed(immutable)
   
32.print('Ha'+String[2:])
   #this is a good solution to print different string without changing it
   
33.print(len(String))
   #this will print the length of the string
   
34.print(len(String + String2))
   #prints length of the final string
   
34.1 print(String.upper())
   #changes the string to all upper case
   
35.1 print(String.lower())
   #changes the string to all lower case
   
35.print(List[0])
   #print the first element of the List(array)
   
36.print(List[-1])
   #works like char i.e starts from the end
   
37.print(llist)
   #print the two lists inside the main list
   
38.List.append(45)
   #adds 45 to the list at the end position
   
39.List.insert(2,77)
   #inserts the value at the position mentioned at the start,.here 77 is inserted position 2
   
40.print(List.pop(2))
   #prints the value at position 2 in the array and removes that value from the array
   
41.List.extend([34,56,78,80,63,85])
   #adds the specified values to the end of the array
   
42.print(min(List))
   #prints minimum value in the list
   
43.print(max(List))
   #prints maximum value in the list
   
44.print(sum(List))
   #prints the sum of the values in the array
   
45.print(List.sort())
   #sorts the array in ascending order
   
46.print(tupple[1])
   #prints element at position 1
   
47.tupple[1] = 33
   #error: object does not support item assignment(cant change value in a tupple
   
48.print(set)
   #prints element of set in a random order(improves performance of program)
   
49.print(set[2])
   #error: object does no support indexing(does not work as set does not have definite position for elements)
   
50.print(data[1])
   #prints corresponding value
   
51.print(data.get(1))
   #prints corresponding value
   
52.print(data[11])
   #error: gives KeyError
   
53.print(data.get(11))
   #does not give error but prints 'none'
   
54.print(data.get(1, 'Not found'))
   #prints 'Aarish'
   
55.print(data.get(11, 'Not found'))
   #prints 'Not found' as there is no key called '11'
   
56.print(dict(zip(AtomicNumber, Element)))
   #combines two lists
   
57.data[11] = 'Sodium'
   #adds key and value at the end of the dictionary
   
58.del data[11]
   #deletes the key and corresponding value
   
59.print(prog)
   #printsthe dictionary
   
60.print(prog['JS'])
   #prints corresponding element
   
61.print(prog['Python'])
   #prints the 2 elements for the key 'Python'
   
62.print(prog['Python'][1])
   #prints the first element in the List of the key 'Python'
   
63.print(prog['Java']['JEE'])
   #searches the key 'Java' for the key 'JEE' and prints corresponding element of 'JEE'
   
64.print(id(a))
   #prints the address in the computer storage of variable 'a'(works for all variable types eg. String)
   
65.statement:
   a = 8
   d = a
   print(id(a))
   print(id(d))
   #here the id for both 'a' and 'd' is the same(in python if two variable have the same data both of them point at the same address)(more memory efficient)
   print(id(8))
   #'8' will also have the same id as 'a' and 'd'(all object have a id)(address is not related to the variable but to the box where the content is stored so the a is the variable which points where 8 is stored and d points at where a is stored)
   
66.statement:
   a = 10
   print(id(a))
   #this will print the address of 10 as a is now pointing at or referring to 10
   print(id(b))
   #b is now not pointing at a but at a's previous value i.e. 8
   (as a personal rule of programmers all constants in Python are written in capital letters as there is no constant function per se)(eg. PI = 3.14)
   
67.print(type(a))
   #it will print the type of value the variable is(here a is int)
   print(type(dou))
   #it will print float as this variable contains a value which has points
   
68.print(type(comp))
   #comp contains 6 + 9j j in python represents the square root of -1 which make comp a complex number
   
69.print(int(dou))
   #type conversion converts float to int rounds down
   print(float(a))
   #converts int to float
   print(complex(b))
   #make the value complex
   
70.statement:
   bool = a>b
   #the value of bool is true here
   bool = b>a
   #the vale of bool here is false
   int(True) = 1
   int(False) = 0
   
71.print(type(list))
   #type for list is 'list'
   print(type(set))
   #type for set is 'set'
   print(type(tupple))
   #type for tupple is 'tuple'
   print(type(String))
   #type of String is 'str'
   
72.print(range(10))
   #prints     (0,10)
   
73.print(list(range(10)))
   #prints numbers from 0 to 10 in list format i.e.0....9
   
74.print(list(range(2,10,2)))
   #prints the numbers between 2 and 10 with a difference of 2 i.e.2,4,6,8
   
75.print(data.keys())
   #gives the keys ONLY
   
76.print(data.value())
   #prints the values ONLY
   
77.a = 4
   #'=' is assignment operators
   
78.a += 2
   #increments the value by 2(work for all operators)
   
79.a,b = 5,6
   #assigns two values at once here a = 5 and b = 6
   
80.n = 7
   n = -n
   #n becomes the negative value of itself i.e. -7
   
81.print(a>b)
   #gives output True
   print(a<b)
   #gives output False
   print(a==b)
   #gives output false
   print(a<=b)
   #gives output false
   print(a>=b)
   #gives output True
   print(a!=b)
   #gives output true
   
82.print(a>b and b>1)
   #gives output True
   
83.print(a<b and b>1)
   #although second statement is true as we used and the output is false
   
84.print(a<b or b>1)
   #here as we used or we only need one statement to be true as second statement is true the output is or
   
85.x = True
   print(not x)
   #prints False by negating x
   x = not x
   #changes value of x to False
   
86.print(bin(a))
   #prints a in binary format(the prefix of the printed number is '0b' which tells that the number is in binary

87.print(0b0101)
   #prints decimal form of the Binary number here it is 5

88.print(oct(25))
   #prints the number 25 in Octal form(0o31)(octal is o)

89.print(hex(25))
   #prints hex form of 25(0x19)(x is for hexadecimal)

90.temp = a
   a = b
   b = temp
   #swaps values of a and b but wastes a variable
OR
   a = a + b
   b = a - b
   a = a - b
   #makes a = a + b then b = a - b which is (a + b) - b which is a so b = a then a is a - b which is (a + b)-(a - b) which equals to  so a = b here we do not waste a variable but we waste a bit
OR
   a = a ^ b
   b = a ^ b
   a = a ^ b
   #'^' this symbol is XOR which gives correct answer and does not waste a bit
OR
   a,b = b,a
   #this function works for Python only and has no complications

91.print(~12)
   #gives -13 (~ is compliment operator) 12 is (00001100)(complement of 12 is 11110011)13 is 00001101 it's compliment is 11110010 it's 2's compliment is the number +1 so it is 11110011 which is -13 2's compliment of a number is it's negative form

92.print(12 & 13)
   #12 is 00001100 and 13 is 00001101 so on comparing these if the numbers in the same position are both 1 then the answer number has 1 else it has 0 like and operator
   which means that on comparing you get 00001100 which is 12.this is 'bitwise and'

93.print(12 | 13)
   #same as 'bitwise and' but here if any number is 1 the output is 1 so answer is 00001101 which is 13.this is 'bitwise or'

94.print(12 ^ 13)
   in XOR is the two numbers are same then 0 and if it is different then 0(here 12 is 00001101 and 13 is 00001101)so on comparing you get(00000001 as except for last position the answers are zero)

95.print(10 << 2)
   10 is 00001010.0000(the zeros are after point so we mostly ignore them)so on shifting two zeros the answer is 00101000 which is 40

96.print(10 >> 2)
   10 is again 00001010(ignoring zero) so on deleting last two bits we get 00000010 which is 2

97.print(math.sqrt(25))
   #same as java finds square root(returns float value)

98.print(math.floor(9.9))
   #gives lower value like JAVA(gives int)

99.print(math.ceil(9.1))
   #gives higher value like JAVA(gives int)

100.math.pow(2,3)
    #gives 2 raised to 3(gives float)

101.x = input()
    print(x+1)
    #input function is like scanner class in JAVA but it only accepts string so if x is 5 it will print 51

102.x = input()
    a = int(x)
    print(a + 1)
    #here a stores int value of x so a will be 5 and output is 6

103.x = input('Enter a number here --->')
    #you can type messages in input box :)

104.x = int(input('Enter a number here --->'))
    #converts input value to Int from string

105.result = eval(input('Enter a expression : '))
    print(result)
    #evaluates any expression typed in input like 2 + 3 - 1 so it will print 4 :o

106.if(a == b):
    print('equal')
    #checks if a == b which is false so it prints nothing if it was true then it would have printed equal, equal is belonging to true block in Python block is Suite(don't forget the colon)

107.if(a == b):
    print('equal')
    if(a < b):
    print('less')
    if(a > b):
    print('Great')
    #it checks every if and when a condition is true it goes to the true block but not efficient as it checks all ifs

108.if(a != b): 
    print('not equal')
    else:
    print('Equal')
    #this is more efficient as here if has true block and else has false block so if the first statement is true it does not check else

109.if(a == b):
    print('Equal')
    elif(a > b):
    print('Great')
    elif(a < b):
    print('Less')
    #here it is a mixture of if and else( same as if-else-if ladder here it is if-elif ladder)this is also efficient

110.if(a != b):
        if(a > b):
        print('Great')
        else:
        print('less')
    else:
    print('Equal')
    #This is basically nested if where a if is in the true block or the false block

111.while i <= 5:
    print('Aarish is the greatest')
    i += 1
    #checks the condition prints THE TRUTH and then increments value of i and checks until the statement is false
OR
    while i >= 1:
    print('Aarish is the greatest')
    i -= 1
    #checks the condition prints THE TRUTH and then decrements value of i and checks until the statement is false

112.while i <= 5:
    print('Aarish is the greatest',end = "")
    j = 0
        while j <= 5:
        print('and awesome',end=" ")
        j += 1
        
    i += 1
    print()
    #simple nested while loop, end specifies how the print ends so here the print ends with a space and cursor remains on the same line

113.for i in mixList:
        print(i)
    #prints all the values in the 'mixList'

114.for i in range(10):
        print(i)
    #prints all the values form 0 to 9

115.for i in range(1,11,1):
        print(i)
     #prints all values from 1 to 11 excluding 11 with a difference of 1   

116.for i in range(2,11,2):
        print(i)  
    #prints all even numbers cause there is a difference of 2 

117.for i in range(20,9,-1):
        print(i) 
    #prints the numbers in a range in reverse order

118.for i in range(1,11):
        if(i%5!=0):
                print(i)
    #prints all numbers between 1 and 11 which are not multiples of 5

119.for i in range(10):
        if(i%2!=0):
            pass
        else:
        print(i)
    #prints all even numbers pass is used to say that the block is not used because you cannot keep blocks/suites empty in Python

120.for num in List:
    if num % 5 == 0:
        print(num)
        break

else:
    print('not found')
    #there is for-else in python where if the loop condition is false it will go to false block it will only print if the condition is false it is not like writing a statement after the loop directly

121.print(val)
    #prints the array as 'array('i', [5, 9, 8, 4, 2])'

122.print(val.buffer_info())
    #prints array and size, eg.(2579529057936, 5)

123. print(val.typecode)
     #prints type of the array here it will print 'i'

124.val.reverse()
    print(val)
    #reverses the array and prints it(array('i', [2, 4, 8, 9, 5]))

125.print(val[0])
    #prints the value at the index

126.for i in range(5):
        print(val(i))
OR  for i in val
        print(i)
    #prints all values of the array

127.val = array('u', ['a', 'e', 'i', 'o', 'u'])
    # u stands for unicode and can store char

128.newArr = array(val.typecode, (a for a in val))
    #makes the newArr same as val(duplicate array)

129.bl = array('i', [])
    x = int(input('Enter length of array : '))
    for i in range(x):
        v = int(input('Enter the value for the array : '))
        bl.append(v)
    print(bl)
    #this takes the input from user in array

130.s = int(input('Enter search value : '))
    for i in range(5):
        if s == val[i]:
             pos = i
             break
     print(pos+1)
     #linear search program(manual process)

131.print(val.index(9))
    #prints the index value of value entered in the brackets

132.in numpy initialization is different
    array = array([1, 2, 3, 4, 5, 6])
    #no 'i' needed
OR
    array = array([1, 2, 3, 4, 5, 6],int)

133.print(array.dtype)
    #gives the type of the values in the array(int32)

134.arr = array(1, 2, 3, 4, 5.0)
    print(array.dtype)
    print(arr)
    #makes all values as float by implicit type conversion

135.arr = array([1, 2, 3, 4, 5],float)
    print(array.dtype)
    print(arr)
    #prints type as float64 and makes all values(1. 2. 3. 4. 5.)

136.arr = linspace(0, 15, 16)
    #in linspace the second value is included and the third value is the number of parts it is divided into(output is float)
    if the third value is not specified it divides the range into 50 parts

137.arr = arange(1, 15, 2)
    #it is the same as range but for arrays

138.arr = logspace(1, 40, 5)
    #it divides the elements using log so first it is 10^1 then 10^40 and the whole is divided into 5 parts(diff between values is a log)

139.arr = zeros(5)
    #creates a array filled with the number of zeros mentioned in bracket(returns float)
    arr = zeros(5,int)
    #converts zeros into float

140.arr = ones(5)
    #same as zeros but prints 5 ones(returns float)
    arr = ones(5,int)
    #converts into int

141.arr = array([1, 2, 3,4, 5])
    arr += 5
    #adds 5 to all elements in the array(out : 6, 7, 8, 9, 10)

142.arr3 = arr + array
    #you can add arrays in which each element is added to the corresponding element in the other array(different sized arrays cannot be added)

143.print(sin(arr))
    #prints sine of each value in the array

144.print(cos(arr))
    #prints cosine of each value in the array

145.print(log(arr))
    #prints log of each value in the array

146.print(sqrt(arr))
    #prints square root of each value in the array

147.print(sum(arr))
    #prints sum of each value in the array

148.print(min(arr))
    #prints minimum value in the array

149.print(max(arr))
    #prints maximum value in an array

150.arr.sort()
    print(arr0
    #sorts the array

151.print(concatenate([arr, arr2])
    #concatenates any number of arrays into one array

152.copy an array:
    arr1 = arr2
    print(arr1)
    print(arr2)
    print(id(arr1))
    print(id(arr2))
    #although the 2 arrays have same value they are not exactly different arrays they both have same id

153.copy an array:
    arr1 = arr2.view()
    print(arr1)
    print(arr2)
    print(id(arr1))
    print(id(arr2))
    #although the 2 arrays have same value now id is also different due to view but it is shallow copy meaning if we change arr2's value then the first arrays value also changes

154.copy an array:
    arr1 = arr2.copy()
    print(arr1)
    print(arr2)
    print(id(arr1))
    print(id(arr2))
    #this is deep copy as now the two arrays have same values but are completely unrelated so even if you change value of arr2, arr1 will not change it will be arr2's previous value

155.marr = array([
                [1, 2, 3], 
                [4, 5, 6]
        ])
        print(marr)
        #makes multidimensional array

156.print(marr.ndim)
    #prints number of dimensions or ranking in an array(SDA = 1, DDA = 2.....), gives tuple

157.print(marr.dtype)
    #prints data type

158.print(marr.shape)
    #gives number of rows and columns, gives tuple

158.1.print(marr.shape[1])
      #gives number of columns

158.2.print(len(marr))
      #gives number of rows

159.print(marr.size)
    #prints the total number of elements

160.arr2 = marr.flatten()
    #converts multidimensional array into single dimensional

170.arr3 = SDA.reshape(3,4)
    #makes a Single dimensional array into 2d array

171.3ar = SDA.reshape(2, 2, 3)
    #this makes a 3 dimensional array(2 x 2 x 3) which contains 2 two dimensional arrays(2 x 3) which contains 2 single dimensional arrays each(3)

172.m = matrix(marr)
OR
    m = matrix('1 2 3 ; 6 4 5 ; 1 6 7')
    #innitialising matrix(semicolon in second techniques means new array or new line

173.print(diagonal(m))
    #prints only diagonal elements

174.print(m.max()) OR print(m.min())
    #prints the max or min value in the matrix

175.m1 = matrix('1 2 3 ; 6 4 5 ; 1 6 7')
    m2 = matrix('1 2 3 ; 6 8 5 ; 2 6 7')
    m3 = m1 + m2
    #gives the sum of each corresponding element in a matrix(same as normal math) and stores in another matrix

176.m3 = m1 * m2
    #prints the correct product automatically(simple)

177.def greet():
        print('Hello')
        print('Good Morning')
    greet()
    #create your own function and call it

178.def greet():
        print('Hello')
        print('Good Morning')
    greet()
    greet()
    #create your own function and call it(here we have called it twice so it will print twice)

179.def add(x, y): #variables in the bracket are called arguments
        c = x + y
        print(c)
    add(5,4)
    #you can put anything in the brackets(here x = 5, y = 4)this will only print the sum

180.def add(x, y):
        c = x + y
        return c #this is extremely important
    add(5,4)
    #create your own function and call it(here we have called it twice so it will print twice)
    result = add(5, 4)
    #it stores the sum value in result(a function can return something or execute a task here it will return something)

181.def add_sub(x, y): #the variable in the bracket are called arguments
        c = x + y
        d = x - y
    return c,d
    result1, result2 = add_sub(5, 4)
    print(result1,result2)
    #if a function returns two values it should be accepted in two variables

182.def update(x):
        x = 8
        print(x)
    a = 10
    update(a)
    print(a)
    #here when we say update(a) then we are neither passing by value nor passing by reference, so x will get value of 10 and become 8 , but a will remain the same so output is 8 then 10 so value of a is still 10(moment we change the value the id of x is different from id of a )(in Python we neither pass by value nor pass by reference :)) 

183.def update(lst):
        lst[1] = 25
        print('x', lst)
    lst = [10, 20, 30]
    update(lst)
    print(lst)
    #here the value of lst will change to [10, 25, 30](string is non mutable but list is so this actually changes value of original list)

184.def person(name, age):
        print(name)
        print(age)
    person('Aarish', 15)
    #this is a position argument so the position of input inside brackets matter here Aarish is name and 15 is age if we exchange then 15 is name and aarish is age which does not make sense
    here we can exchange the values there will be no error

185.def person(name, age):
        print(name)
        print(age)
    person(age = 15, name = 'Aarish')
    #here this is keyword argument so the variable name in the argument of the function has to be mentioned when you input so the order does not matter

186.def person(name, age = 18):
        print(name)
        print(age)
    person('Aarish')
    #here if you pass a value after calling a function the age will be that vale but if you do not then it will be the default value here it is 18 so on skipping the age it is automatically 18

187.def add(x, *b):
        s = x + y
        print(s)
    add(5, 6, 34, 70)
    #*b is used to accept multiple values in a tuple(this will give error as *b is a tuple and int and tuple cannot be added)

188.def add(x, *b):
        s = x 
        for i in b:
           s += i
        print(s)
    add(5, 6, 34, 70)
    #this will print the sum as we are extracting each value from the tuple

189.def add(*b):
        s = 0 
        for i in b:
           s += i
        print(s)
    add(5, 6, 34, 70)
    #this will also work without a only s has to be 0

190.def person(name, **data):
        print(name)
        for i,j in data.items():
                print(i,j)
    person('Aarish', age = 15, city = 'Mumbai', phone = 9769572334 )
    #if you want to accept both keyword and data then use **(here only name is surely going to come

191.def person(name, **data):
        print(name)
        for i,j in data.items():
                l = [i]
                l2 = [j]
                d = dict(zip(l, l2))
        print(d)
    person('Aarish', age = 15, city = 'Mumbai', phone = 9769572334 )
    #prints the values with keywords as dictionary

192.a = 10
    def something():
        a = 15
        b = 8
        print(a)
    print(b)
    print(a)
    #here a = 10 is a global variable so it can be used inside or outside the function but b = 8 and a = 15 are local variables they can 
    only be used inside the function outside the function if used it gives a error.(output will give a as 10 , without the statement to print b ,as the value
    of a is updated only inside the function else it is 10 when function ends)

193.a = 10
    def something():
        a = 15
        b = 8
        print(a)
    something()
    print(a)
    #inside the function preference is given to the local variable which means that something() will print 15 while the outside print will give 10 as updation
    inside function does not matter

194.def add(a, b):
        c = a + b
        print(c)
    x = add
    x(1, 2)
    #this somehow works and prints the added value :o

195.def add(a, b):
        c = a + b
        print(c)

    diction = {'add': add}
    x = input('enter add')
    x = x.lower()
    diction.get(x)(1, 2)
    #user input for functions

196.a = 10
    def something():
        print(a)
    something()
    print(a)
    #in functions if there is no local variable it accesses the global variable

197.a = 10
    def something():
        global a
        a = 15
        b = 8
        print(a)
    something()
    print(a)
    #if you want to access the global variable inside a function use global keyword

198.a = 10
    def something():
        a = 9
        x = globals()['a']
        print(x)
    something()
    print(a)
    #globals stores all global variable as a list in x here i have specified which variable to take in x(this is to use 
    global variable and local variable in the same function

199.def count(ls):
    even = 0
    odd = 0
    for i in ls:
        if i % 2 == 0:
            even += 1

        else:
            odd += 1
    return even, odd


   ls = [20, 25, 14, 19, 16, 24, 28, 47, 26]
   even, odd = count(ls)
   print("even : {} and Odd : {}".format(even, odd))
   #just see this program

200.def name_check():
    lsn = []
    for i in range(10):
        a = input('input names :  ')
        lsn.append(a)
    for i in lsn:
        if len(i) > 5:
            print(i)


    name_check()

201.Recursion:
    def greet()
        print('Hello')
        greet()
    #this will print 'Hello' infinite times(Python has a limit of 1000)

202.print(sys.getrecursionlimit())
    #this will show the limit of recursion

203.sys.setrecursionlimit(3000)
    #this will set the recursion limit

204.Normal Factorial Program:
    def factorialNormal(n):
        f = 1
            for i in range(1, n + 1):
             f *= i
        return f, n


    fact, n = factorialNormal(0)
    print('Factorial of {} = {}'.format(n, fact))
    
    Recursion Factorial program:
    def Fact(n):
        if (n == 0):
            return 1
        return n * Fact(n - 1)


    result = Fact(5)
    print(result)
    #in this program we are finding 5! which is 5 * 4! which is 4 * 3! which is 3 * 2! which is 2 * 1! which is 1 * 0! and 0!
    is known to be 1 so then the program repeats upto zero factorial which is obviously one then it does (0! * 1)(1!) * 2)(2!) * 3)(3!) * 4)(4!) * 5
    and then finally 5!

205.Anonymous function(Lambda):
    f = lambda a: a * a
    f = f(3)
    print(f)
    #Anonymous functions are functions without names, in Python functions are objects and hence can be assigned to a variable
    here lambda 'a' is the argument and 'a * a' is the expression or operation . It can also accept 2 arguments like:
    f = lambda a, b: a + b
    f = f(3)
    print(f)
    #Lambda is useful to use and can only be used if there is only one operation.

206.Filter, map, reduce and usefulness of Lambda
    def iseven(n):
        return n % 2 == 0
    nums = [3, 2, 6, 8, 4, 6, 2, 9]
    evens = list(filter(iseven, nums))
    print(evens)
    #here we are defining a function just for the filter function, this function will not be used anywhere and functions are actually made for reusability
    but here it is of no use except for the filter statement. 
    
    nums = [3, 2, 6, 8, 4, 6, 2, 9]
    evens = list(filter(lambda n : n % 2 == 0, nums))
    print(evens)
    #lambda is used here particularly for the filter function and cannot be reused
    
    nums = [3, 2, 6, 8, 4, 6, 2, 9]
    evens = list(filter(lambda n: n % 2 == 0, nums))
    print(evens)
    doubles = list(map(lambda n: n * 2, evens))
    print(doubles)
    sum = reduce(lambda a, b: a + b, doubles)
    print(sum)
    #map performs a function on each element of a list and converts those elements
    #reduce performs a function on two elements at a time to get a singular answer 

207.def div(a, b):
    if a<b:
        a, b = b, a

    print(a/b)

    div(2, 4)
    #we are supposed to exchange the values of a and b if b is greater than a which means that the answer will always be 1 or greater than 1

208.def div(a, b):
    print(a / b)


    def smart_div(func):
        def inner(a, b):
            if a < b:
                a, b = b, a
            return func(a, b)

        return inner


    div = smart_div(div)
    div(2, 4)
    #decorators are used to change the values in a function without touching the function here smart_div accepts a function 
    and inner takes value from func and operates on them then it returns the new values then div1 is a function which executes 
    the function of div with the exchanged values here 'inner' is called a wrapper function which is inside the decorator 
    function, the decorator function accepts the main function as an argument

209.a, b = 9, 7
    c = add(a, b)
    print(c)
    #you can import any user made modules here calc contains the function for add which has been imported

210.print(__name__)
    #this is a special variable if the statement is there in notes and we are running notes it prints __main__ but if we have imported calc
    and this statement is there in calc then it will print the module name here it is calc

211.if __name__ == "__main__"
    print('you are running Notes')
    #this means that this statement will only execute if the module that this is written in is being executed here it will run if you run Notes

212.class Computer:
        def config(self):
            print('i5, 16gb, 1TB')
    # Suite or Block

    comp1 = Computer()
    comp2 = Computer()
    print(type(comp1))
    Computer.config(comp1)
    Computer.config(comp2)
    comp1.config()
    comp2.config()
    #these are the ways of calling Methods(functions) inside of a class
    #type will print '<class '__main__.Computer'>'

213.class Computer:
        def __init__(self, cpu, ram):
            self.cpu = cpu
            self.ram = ram

        def config(self):
            print(self.cpu, self.ram)


    # Suite or Block

    comp1 = Computer('i5', 16)
    comp2 = Computer('Ryzen 3', 8)
    print(type(comp1))
    comp1.config()
    comp2.config()
    #__init__ is used get input in a class using self normal way of giving Arguments does not work
    
213.class Computer:
        def __init__(self):
            self.name = "Aarish"
            self.age = 15

        def update(self):
            self.age = 30
        def compare(self, other):
            if self.age == c2.age:
                return True
            else:
                return False


    c1 = Computer()
    c2 = Computer()

    if c1.compare(c2):
        print('They are same')
    else:
        print('They are different')

    c1.update()

    print(c1.name)
    print(c2.name)
    # Computer () is a constructor, all objects are stored in heap memory, so the () in Computer() call  __init__  which finds memory for the objects according 
    to the size of the object(the size of the objects depends on the size of the variables and the number of variable).When we write c1 = Computer() c1 is the object
    when self is written it is used to get values stored in a particular object one at a time, like when we say c1.compare(c2) both values of c1 are stored in self
    while values of c2 are stored in other, similarly if it was c2.compare(c1) then c2 would be self while c1 will be other, self is basically an argument.Self accepts
    the values stored in the object which calls the function here c1 is calling compare so values of c1 are stored in self.

214.class Car:
        wheels = 4

        def __init__(self):
            self.mil = 10
            self.com = 'BMW'


    c1 = Car()
    c2 = Car()

    c1.mil = 8

    Car.wheels = 5

    print(c1.com, c1.mil, c1.wheels)
    print(c2.com, c2.mil, Car.wheels)
    #any variable which is initialized inside __init__ is called an instance it is unique for each object so if the value is changed for 1 objects it will not
    change for the other object, here the mileage of c1 is changed but that does not affects c2 while any variable initialized outside __init__ but inside a class
    is called a static variable which is common for all objects that use the class so the wheels for all cars are 4 and if the number of wheels for one object
    are changed the number of wheels for all the objects will change.This is the concept of instance and static variable.
    
215.class Student:
        school = 'LFS'

        def __init__(self, m1, m2, m3):
            self.m1 = m1
            self.m2 = m2
            self.m3 = m3

        def avg(self):
            return (self.m1 + self.m2 + self.m3) / 3.0

        def get_m1(self):
            print(self.m1)

        def set_m1(self, correctedmarks):
            self.m1 = correctedmarks
            print(self.m1)

        @classmethod
        def school_name(cls):
            return cls.school

        @staticmethod
        def info():
            print('this is the student info')


    s1 = Student(15, 67, 90)
    s2 = Student(76, 9, 90)
    print(s1.avg())
    print(s2.avg())
    s1.get_m1()
    s2.set_m1(99)
    print(Student.school_name())
    Student.info() 
    # the function avg is instance method, in instance method there are two sub-methods get_m1 is accessor method while set_m1 is mutatory method, 
    the other type of method is class method
    
216.class student:
        def __init__(self, name, Rno):
            self.name = name
            self.Rno = Rno
            self.laptop = self.Laptop()

        def show(self):
            print(self.name, self.Rno)
            self.laptop.show()

        class Laptop:
            def __init__(self):
                self.brand = 'HP'
                self.cpu = 'i5'
                self.ram = '8gb'

            def show(self):
                print(self.ram, self.cpu, self.brand)


    s1 = student('Aarish', 30)
    s2 = student('someone', 35)

    s1.show()

    lap1 = student.Laptop()
    lap2 = s2.laptop()
    #this is the method to create a class inside a class which is called the inner class here laptop is the inner class and Student the main class
    
217. class MyEditor:

        def execute(self):
            print('Spell Check\nConvention check\nCompiling\nRunning')


    class laptop:

        def code(self, IDE):
            IDE.execute()

    IDE = MyEditor()
    lap = laptop()
    lap.code(IDE)
    #polymorphism means that one thing has multiple forms so then whatever the name of the IDE will execute, the execute
    function is used to execute a class from another class. This is called duck typing.
    
218.int.__add__(1, 5)
    str.__add__('1', '5')
    #whenever we say '+' the computer calls the __add__()function
    
219.a = 8
    print(a.__str__())
    #whenever we print something the object is converted to string using string function
    
220.if a > b:
        print('a is greater')
    else:
        print('b is greater')
    #whenever we use '>' a.__gt__(b) is called which checks this and returns true or false
    
221.if we print any object the address is printed not the value
    if we try to check for relation between objects or try to add them it gives an error
    
222.class Student:
        def __init__(self, m1, m2):
            self.m1 = m1
            self.m2 = m2

        def __add__(self, other):
            s1 = self.m1 + other.m1
            s2 = other.m2 + self.m2
            return s1, s2

        def __mul__(self, other):
            mu1 = self.m1 * other.m1
            mu2 = other.m2 * self.m2
            return mu1, mu2

        def __gt__(self, other):
            c1 = self.m1 + self.m2
            c2 = other.m1 + other.m2
            if c1 > c2:
                return True
            else:
                return False

        def __str__(self):
            return '{} {}'.format(self.m1, self.m2)

    st1 = Student(57, 89)
    st2 = Student(99, 68)
    s3 = st1 + st2
    mu = st1 * st2
    print(s3, mu, st1, st2)
    if st1 > st2:
        print('st1 is greater')
    else:
        print('st2 is greater')
    #this is operator overloading where we define what a operator does
    

223.Method overloading : this is where you have one method where number of arguments or data types of the arguments are different so same named method contains
    different types or number of arguments

    class Student:

        def Sum(self, a=None, b=None, c=None):
            s = 0
            if a != None and b != None and c != None:
                s = a + b + c
            elif a != None and b != None:
                s = a + b
            else:
                s = a

            return s

    s1 = Student()
    print(s1.Sum(1, 2, 4))
    #This is a way to do method overloading in Python
    



224.Method overriding : This is where 2 classes contain the same method with same arguments and one class inherits from the other then when that method is 
    called using the child class the method in the child class is used and the inherited method of the same name is overridden.

    class A:
        def show(self):
            print('in A show')
    
    class B(A):
        def show(self):
            print('in B show')
            
    e = B()
    e.show()
        
    #this is method overriding where if two classes contain the method with the same name and the second class inherits from the first class if you execute that
    method inside the child class it will execute the method in the child class and not the inherited method. here output will be 'in B show'.
    
225.Abstract class and method : these classes and methods are ones which contain no statements a abstract method has no statements and an abstract class has 
only abstract methods. This is a kind of rule in OOPs programming and it helps fish out errors before execution is complete

    from abc import ABC, abstractmethod


    class Computer(ABC):

        @abstractmethod
        def process(self):
            pass


    class Laptop(Computer):
        def process(self):
            print('Processing....')


    class whiteboard:
        def write(self):
            print('Its writing')


    class Programmer:
        def work(self, comp):
            print('Solving bugs')
            comp.process()


    com1 = Laptop()
    prog1 = Programmer()
    com2 = whiteboard()
    prog1.work(com2)
    com1.process()
    #this Abstract class and method where the class and method contains nothing, here it will say that the class whiteboard has nothing called process which
    is used to fish out a error.
    
226.Iterator : This is used to create your own iterator, like you have control in java.This iterator can be used multiple time in same program. Iterator is used
    to fetch one value at a time, but u need to make the function yourself

    class TopTen:
        def __init__(self):
            self.m1 = 1
    
        def __iter__(self):
            return self
    
        def __next__(self):
            if self.m1 <= 10:
                val = self.m1
                self.m1 += 1
                return val
            else:
                raise StopIteration
    
    values = TopTen()
    
    for i in values:
        print(i)
        
        
    #iter converts a list to iterator and it gives one value from the list and next is used to give that value and go to the next one. This is basically what happens
    in a for loop.
    
227.Generator : This is a way to make iterators without too much work using the keyword 'yield'. It can be used to check things or perform operations on 
                iterator to control the output.

    def TopTen():
        yield 1
        yield 2
        yield 3
        yield 4
    
    
    values = TopTen()
    print(values.__next__())
    for i in values:
        print(i)
        
OR

    def TopTensquare():
        n = 1
        while n <= 10:
            sq = n * n
            yield sq
            n += 1
    
    
    values = TopTensquare()
    print(values.__next__())
    for i in values:
        print(i)
    #The first one is a typical iterator which prints numbers from 1 to 10. The second one performs a function on the iterator

228.Exception handling : In a program if input type is int and user enters a String instead of giving a error and completely stopping the program we can use
try and except block to continue further execution of program while also notifying the user about the error.
    
    a = 5
    b = 2
    
    try:
        print('Values from files taken')
        print(a/b)
        k = int(input('Enter Integer to return to the file : '))
    except ZeroDivisionError as error:
        print('Division By Zero is not possible', error)
        print(type(error))
    except ValueError as error:
        print('Invalid Input', error)
    except Exception as error:
        print('Unknown error found, Congrats', error)
    finally:
        print('Values returned to the file after performing functions')
    
    print('Thank You for using our program...')
    #Here ZeroDivisionError checks whether the value of b is 0 is so it will print the statement and continue to print Thank You. value error is checked by the second
    except so if the input type is int but the user inputs String then this block is executed and if the error is not mentioned then any other error comes under
    Exception which will execute the Exception block and then moves on to the next statement.

229.Multi Threading : Our CPUs have threads which perform certain functions, so if you use more threads in a program then more functions can be performed at once.
    This is mainly used in practice or for improving speed of a program.
    from threading import *
    from time import sleep
    
    
    class Hello(Thread):
        def run(self):
            for i in range(5):
                print('Hello')
                sleep(1)
    
    
    class Hi(Thread):
        def run(self):
            for i in range(5):
                print('Hi')
                sleep(1)
    
    
    t1 = Hello()
    t2 = Hi()
    
    t1.start()
    sleep(0.2)
    t2.start()
    t1.join()
    t2.join()
    print('Bye')
    #here the two classes are executed using 2 different threads which are unsynced using sleep which is imported from time.This program will print hello and then hi
    and not hello 5 times and hi 5 times.
    
230.File Manager : Here using this technique you can make a text file, from which you can get the text and print it.

    f = open('Notes_Text', 'r')#this will go to the mentioned file and read it 'r'
    print(f.read())#this will print everything that had been read earlier
    print(f.readline(), end="")#this will print only one line of the file that was read
    print(f.readline())#this will print the next line of the file
    print(f.readline(4))#this will print the first 4 characters of the line that was read
    f1 = open('abcd', 'w')#creates file abc to write in
    f1.write('Something')#the statement will be written in the file
    f1.write("something else")#This statement will be written in the file and it will remove the earlier statement
    f2 = open('abcd', 'a')#this creates a file for you to append
    f2.write('Appended')#this will not replace the earlier data but actually append or add more data
    for data in f:
        f2.write(data, end="")#this will write one thing from a file into another
    #This is the way to manage file
    
231.MySQL : this is a database where you can store things and values without having to calculate them everytime you run a program
    
    import mysql.connector
    
    mydb = mysql.connector.connect(host='localhost', user='Aarish', passwd='Aarish3011', database= 'Aarish')
    
    mycursor = mydb.cursor()
    
    mycursor.execute("select * from student")
    
    result = mycursor.fetchone()
    
    print(result)
    
    for i in result:
        print(i)
    #here we import the module, then mydb is used to access the database, we need to give the IP address, the username, the password and if a particular database is being
    accessed then you need to give the database name too.
    mycursor variable is used to point where the file is and it can be used to access particular line in the database
    result variable then stores the values or table.

232.Socket Programming : 
"""


class P30:
    def m30(self, n1, n2):
        for i in range(1, n2):
            if n1 % i == 0 and n2 % i == 0:
                GCD = i
        return GCD


def decorate(func):
    def swap(n1, n2):
        if n2 > n1:
            n1, n2 = n2, n1
        print("hello")
        return func(n1, n2)

    return swap


#P30 = P30()
#P30.m30 = decorate(P30.m30)
#print(P30.m30(40, 24))

#print(hash("Aarish"))

class TopTen:
    def __init__(self):
        self.m1 = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.m1 <= 10:
            val = self.m1
            self.m1 += 1
            return val
        else:
            raise StopIteration

values = TopTen()

for i in values:
    print(i)


def TopTen():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
    yield 7
    yield 9
    yield 13


values = TopTen()
print(values.__next__())

"""for i in values:
    print(i)"""
