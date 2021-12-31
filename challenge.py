#1 - Capital indexes
def capital_indexes(string):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i, l in enumerate(string):
        if l in upper:
            result.append(i)
    return result

print(capital_indexes("RYANnnKkK"))

#2 - Middle letter	
def mid(string):
    if len(string) % 2 == 0:
        return ""
    return string[len(string)//2]
    
    
print(mid("abxbcbcbc"))

#3 - Online status
def online_count(statuses):
    count = 0
    for i in statuses:
        if statuses[i]=="online":
            count=count+1
    return count

#4 - Randomness
import random 
def random_number():
    n=random.randint(0,22)
    return n
    
#5 - Type check
def only_ints(a,b):
    if type(a) == int and type(b) == int:
        return True
    else:
        return False
 
print(only_ints(1, 2))     

#6 - Double letters
def double_letters(string):
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False

print(double_letters("hello")) 

#7 - Adding and removing dots 
def add_dots(string):
    result = ""
    for i in string:
        result += i + "."
    return result[:-1]

def remove_dots(string):
    result = ""
    for i in string:
        if i != ".":
            result += i
    return result

print(add_dots("test"))
print(remove_dots("t.e.s.t"))

#8 - Counting syllables
def count(string):
    amount=string.count("-")+1
    return amount

print(count("ho-tel"))

#9 - Anagrams
def is_anagram(string1,string2):
    if sorted(string1)==sorted(string2):
        return True
    else:
        return False
print(is_anagram("typhoon", "opython"))

#10 - Flatten a list

def flatten(t):
    flat_list = []
    for i in t:
        for item in i:
            flat_list.append(item)
    return flat_list
    
print(flatten([[1, 2], [3, 4]]))

#11 - Min-maxing
def largest_difference(list):
    x=min(list)
    y=max(list)
    diff=y-x
    return diff

print(largest_difference([1, 2, 3]))

#12 - Divisible by 3
def div_3(num):
    if num % 3:
        return False
    else:
        return True

print(div_3(6))

#13 - Tic tac toe input
def get_row_col(letter):
    col = letter[0]
    row = int(letter[1])-1
    board_dic = {"A": 0, "B": 1, "C": 2}
    for i in board_dic:
        if i == col:
            column = board_dic[i]
            return (row, column)

print(get_row_col("A3"))

#14 - Palindrome
def palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
print(palindrome("abba"))

#15 - Up and down
def up_down(num):
    up=num+1
    down=num-1
    return down, up
    
print(up_down(5))

#16 - Consecutive zeros
def consecutive_zeros(string):
    return max(string.split("1")).count("0")
    
print(consecutive_zeros("1001101000110"))
    
#17 - All equal
def all_equal(iterable):
    iterator = iter(iterable)
    try:
        firstItem = next(iterator)
    except StopIteration:
        return True
        
    for x in iterator:
        if x!=firstItem:
            return False
    return True

all_equal([1, 1, 1])

#18 - Boolean and 
def triple_and(par1,par2,par3):
    if par1==par2==par3==True:
        return True
    else:
        return False
    
print(triple_and(1,3,4))

#19 - Writing short code
def convert(a):
    return(list(map(str, a)))
    
print(convert([1, 2, 3]))

#20 - Custom zip
def zap(a,b):
    result=[]
    for i in range(len(a)):
        for j in range(len(b)):
            if i==j:
                result.append((a[i],b[j]))
    return result
    
print(zap([0, 1, 2, 3],[5, 6, 7, 8]))

#21 - Solution validation
def validate(code):
    if "def" not in code:
        return "missing def"
    if ":" not in code:
        return "missing :"
    if "(" and ")" not in code:
        return "missing paren"
    if "(" + ")" in code:
        return "missing param"
    if "    " not in code:
        return "missing indent"
    if "validate" not in code:
        return "wrong name"
    elif "return" not in code:
        return "missing return"
    else:
        return True

print(validate("SUII"))

#22 - List XOR
def list_xor(n, list1, list2):
    if n not in list1 and n not in list2:
        return False
    elif n in list1 and n in list2:
        return False
    return True
    
print(list_xor(1, [0, 0, 0], [4, 5, 6]) == False)

#23 - Counting parameters
def param_count(*n):
    return len(n)
    
print(param_count(2,3,4))

#Thousand separators
def format_number(n):
    a = []
    for i, j in enumerate(reversed(str(n))):
        if i != 0 and i % 3 == 0:
            a.append(',')
        a.append(j)
    return ''.join(a[::-1])
print(format_number(1000000))