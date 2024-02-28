import re
#texts for tests
text1 = "VO_VA aboba and biba aroma_aob Fein"
text2 = "a special.text b lkdfjgkld,b"

#task 1

a = re.search("a[b].*", text1)
print(a)


#task 2

x = re.search("a[b]{2,3}", text1)
print(x)


#task 3

c = re.findall("[a-z]+_[a-z]+$", text1)
print(c)


#task 4

z = re.findall("[A-Z][a-z]+", text1)
print(z)


#task 5

b = re.search(r"[a].*[b]$", text2)
print(b)


#task 6

n = re.sub(r"[ ,.]", ":", text2)
print(n)


#task 7

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    if components:
        camel_case_str = components[0] + ''.join(x.title() for x in components[1:])
    else:
        camel_case_str = ''
    return camel_case_str

string = "ah_here_we_go_again"
camel_case = snake_to_camel(string)
print(camel_case)


#task 8

def split_at_uppercase(s):
    return re.findall('[A-Z][^A-Z]*', s)
print(split_at_uppercase("DoReMiFaSolLaSiDo"))


#task 9

def insert_spaces(s):
    return re.sub(r'(?<=[a-zA-Z])(?=[A-Z])', ' ', s)
print(insert_spaces("MyNameIsBellaHadid"))


#task 10

def camel_to_snake(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
print(camel_to_snake("lookAtMe"))
