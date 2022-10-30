dictionary = {
    "name": "Suriyah",
    "Age":"30",
    "Occupation":"Data Engineer",
    "Phone":"78945609343"
}
dictionary["birthdate"] = "13 Oct 1992"
print(dictionary['name'])
print(dictionary['birthdate'])

#Exercise: print 1234, get output in words

num_dic = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine"
}
input_value = input("Phone: ")
output_value = ''
for ch in input_value:
    output_value += num_dic.get(ch) + ' '
print(output_value)




