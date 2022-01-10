#1 - Capital indexes
def capital_indexes(string):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Lavet et alfabet, der skal sammenlignes med
    result = []
    for i, l in enumerate(string): #For loop som skal gå gennem hele string
        if l in upper: #Hvis samme, så tilføj dens index til tom 'result'
            result.append(i)
    return result

#Test code
print(capital_indexes("RYANnnKkK"))

#2 - Middle letter	
def mid(string):
    if len(string) % 2 == 0: #Hvis den er deleligt med 2 så returner tom
        return ""
    return string[len(string)//2] #Else så returner længdens heltal halvdel
    
#Test code    
print(mid("abxbcbcbc"))

#3 - Online status
def online_count(statuses): 
    count = 0
    for i in statuses: # Tjekke ignnem og hvis den matcher så tilføj count
        if statuses[i]=="online":
            count=count+1
    return count

#Test code
print(online_count({
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",}))

#4 - Randomness
import random 
def random_number(): 
    n=random.randint(0,22)
    return n

#Test code
print(random_numver())

#5 - Type check
def only_ints(a,b): 
    if type(a) == int and type(b) == int: # Hvis begge gælder så sand
        return True
    else:
        return False
    
#Test code
print(only_ints(1, 2))     

#6 - Double letters
def double_letters(string): #Lavede et for loop og hvis karakteren og dens efterfølgende karakter var ens så sand (i+1)
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False

#Test code
print(double_letters("hello")) 

#7 - Adding and removing dots 
def add_dots(string): #For loop der vil tilføje til den tomme result ved hver indeks
    result = ""
    for i in string:
        result += i + "."
    return result[:-1] # -1 sørger for at det sidste bogstav ikke for en prik

def remove_dots(string):
    result = ""
    for i in string: #Modsat før
        if i != ".":
            result += i
    return result


#Test code
print(add_dots("test"))
print(remove_dots("t.e.s.t"))

#8 - Counting syllables 
def count(string):
    amount=string.count("-")+1 #Vidste at antallet af stavelser er antallet af bindestrege +1.
    return amount

#Test code
print(count("ho-tel"))

#9 - Anagrams
def is_anagram(string1,string2):
    if sorted(string1)==sorted(string2): #Brugte sorted funktion til at sammenligne de 2 strings når de er i alfabetisk rækkefølge
        return True
    else:
        return False

#Test code
print(is_anagram("typhoon", "opython"))

#10 - Flatten a list

def flatten(t):
    result = []  #Brugte et nested for loop til at fylde result op
    for i in t:
        for j in i:
            result.append(j)
    return result

#Test code    
print(flatten([[1, 2], [3, 4]]))

#11 - Min-maxing
def largest_difference(list): #Tog diff af min of max af listen
    x=min(list)
    y=max(list)
    diff=y-x
    return diff

#Test code
print(largest_difference([1, 2, 3]))

#12 - Divisible by 3
def div_3(num):
    if num % 3:
        return False
    else:
        return True
    
#Test code
print(div_3(6))

#13 - Tic tac toe input
def get_row_col(letter):  #Lavede en dict hvor kolonen var det første bogstav og række var det andet bogstav (-1 så den ikke er uden for grænsen) 
    col = letter[0]
    row = int(letter[1])-1
    board_dic = {"A": 0, "B": 1, "C": 2}
    for i in board_dic:
        if i == col: #Sammenlignet dic med loop
            column = board_dic[i]
            return (row, column)
#Test code
print(get_row_col("A3"))

#14 - Palindrome 
def palindrome(string):
    if string == string[::-1]: #Byttede om på rækkenfølgen af string og sammenlignet
        return True
    else:
        return False
    
#Test code
print(palindrome("abba"))

#15 - Up and down
def up_down(num):
    up=num+1
    down=num-1
    return down, up

#Test code    
print(up_down(5))

#16 - Consecutive zeros
def consecutive_zeros(string):
    return max(string.split("1")).count("0")  #Delte string op mellem 1 tallerne og talte 0

#Test code
print(consecutive_zeros("1001101000110"))
    
#17 - All equal
def all_equal(iterable):
    iterator = iter(iterable)
    try:
        firstItem = next(iterator)
    except StopIteration:
        return True
        
    for x in iterator:
        if x!=firstItem: #Tjekke igennem om de var ddet samme
            return False
    return True

#Test code
print(all_equal([1, 1, 1]))

#18 - Boolean and 
def triple_and(par1,par2,par3):
    if par1==par2==par3==True:
        return True
    else:
        return False
      
#Test code    
print(triple_and(1,3,4))

#19 - Writing short code
def convert(a):
    return(list(map(str, a))) 

#Test code
print(convert([1, 2, 3]))

#20 - Custom zip
def zap(a,b):
    result=[]
    for i in range(len(a)):
        for j in range(len(b)):
            if i==j: #Videste jeg skulle have 0 og 5 sammen hvilket bestød at deres indeks skulle være det samme
                result.append((a[i],b[j]))
    return result
 
#Test code      
print(zap([0, 1, 2, 3],[5, 6, 7, 8]))

#21 - Solution validation
def validate(code):
    if "def" not in code:
        return "missing def"
    if ":" not in code:
        return "missing :"
    if "(" and ")" not in code:
        return "missing paren"
    if "(" + ")" in code:  #Sjovt trick så den kan tjekke for "()"
        return "missing param"
    if "    " not in code:
        return "missing indent"
    if "validate" not in code:
        return "wrong name"
    elif "return" not in code:
        return "missing return"
    else:
        return True

#Test code
print(validate("SUII"))

#22 - List XOR
def list_xor(n, list1, list2):
    if n not in list1 and n not in list2:
        return False
    elif n in list1 and n in list2:
        return False
    return True

#Test code
print(list_xor(1, [0, 0, 0], [4, 5, 6]) == False)

#23 - Counting parameters
def param_count(*n): #* gør at jeg får antallet af argumentere i min parameter
    return len(n)

#Test code
print(param_count(2,3,4))

#Thousand separators
def format_number(n):
    a = []
    for i, j in enumerate(reversed(str(n))): #Byttede om på string så den er nemmere at tilføje prikker til a
        if i != 0 and i % 3 == 0:
            a.append(',')
        a.append(j)
    return ''.join(a[::-1]) # -1 sikre sig at den ikke er ude af range
 
#Test code  
print(format_number(1000000))
      
#Nice
