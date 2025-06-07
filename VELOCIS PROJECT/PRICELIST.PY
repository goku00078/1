#Define the price list of velocis education 
menu = { 
    'course in computer concept':2000,
    'certificate in taly prime with gst':2500,
    'master in full stack devlopment':28000,
    'spoken english':3000,
    'ms office':2000, 
}

#Greet
print("welcome to velocis")
print("course in computer concept: RS2000 \ncertificate in taly prime with gst: RS2500\nmaster in full stack devlopment: RS28000 \nspoken english: RS300 \nms office: Rs2000")

buy_total = 0
item_1 = input("enter name of course you want to buy = ")
if item_1 in menu:
        buy_total += menu[item_1]
        print(f"your item {item_1} has been added to your buying list")
else:
        print(f"course item {item_1} is not available yet!")
another_course = input("do you want to add another course? (yes/no) ")    
if another_course == "yes":
    course_2 = input("enter the name of second course")
    if course_2 in menu:
        buy_total += menu[course_2]
        print(f"item {course_2} has benn added to buy")
    else:
        print(f"buy item {course_2} is not available!")
another_course = input("do you want to add another course? (yes/no) ") 
print(f"the total amount of item to pay is {buy_total}")
if another_course == "yes":
    course_3 = input("enter the name of third course")
    if course_3 in menu:
        buy_total += menu[course_3]
        print(f"item {course_3} has benn added to buy")
    else:
        print(f"buy item {course_3} is not available!")
print(f"the total amount of item to pay is {buy_total}")
        