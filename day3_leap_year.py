

try_year = input("Do you want to try another year? (y/n) : ")

while try_year == 'y':
    year = int(input("Enter year to check : "))

    test_1 = year%4
    test_2 = year%100
    test_3 = year%400

    #if((test_1 == 0 and test_3 ==0) or (test_2 != 0 )):
       # print("The year is a leap year")
    #else:
       # print("The year is not a leap year")
    if(test_1==0 and test_2!=0) or (test_1==0 and test_3 ==0):
        print("leap year")
    else:
        print("not leap year")
