import re

line = "From:ShreyanshFrom:Shreyansh From:FERTYUI F F"
print(re.findall('From:', line))
print(re.findall('F\S', line))  # has no space after F
print(re.findall('F\s', line))  # has space after F
print(re.findall('F.', line))  # has F followed by anything
print(re.findall('^From:', line))  # starts with From:

list1 = ["X-Men", "X-ML", " X-treme", "test", "test1", "X "]
list_x = [word for word in list1 if re.findall('^X.+', word)]
print(list_x)
print([word for word in list1 if re.findall('^X-\S', word)])  # starts with X followed by - and then not white space
# list_y = []
# for item in list1:
#     list_y.extend(re.findall('^X.+', item))
# print(list_y)

test = "Shryansh: 9813-451-345 Sh: 1234-345-456 9846712371"
print(re.findall("\d{4}-{0,1}\d{3}-{0,1}\d{3}", test))

test_email = "axy@abc.com as@as.kjal ssas@sas.com asa_sas@@gmail..com asas@sas asas .a@gmail.com"
print(re.findall("[a-zA-Z0-9][._a-zA-z]+@[a-z]+\.{1}[a-z]+", test_email))

# re.search for verification .findall for extraction

x = 'From: Using : Character'
print(re.findall('^F.+:', x))
print(re.findall('^F.+?:', x))

string = "http:ntc.com.np,http:abc.com.np http:me.com.np,http:ntc.com.np,http:ntc.comnp,http:ntc.com"
print(re.findall('http:\S*.com.np', string))  # Greedy Search
print(re.findall('http:\S*?.com.np', string))  # Non Greedy Search
print(re.findall('http:(\S*?.com.np)',string))  # returns the string only inside ()