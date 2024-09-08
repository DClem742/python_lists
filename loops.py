start_number = int(input("Start from: "))
end_number = int(input("End on: "))

count = start_number

while count <= end_number: #why less than or equal to and not just less than?
    print(count)
    count += 1

title = "Flying Purple Hippos"
counter = 0
while counter < len(title):
    if (counter % 2) == 0 and title[counter] != " ": #why or how is "(counter % 2) == 0" used to see if counter number is even? 
        print(title[counter])
    counter = counter + 1 

while count <= end_number:
    print(count)
    count += 2 

def range_of_numbers(num):
    if num >= 15 and num <= 50:
        return True
    else:
        return False

