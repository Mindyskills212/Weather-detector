print("FR Weather Detector")
a = int(input("1.Cloudy 2.Sunny 3.Windy 4. Both 1 and 3: "))
b = int(input("1. Jan to March 2. Apr to Jul 3. Aug to half Oct 4. Half Oct to Dec : "))

if a == 1 and b == 1 :
    print("Low rainfall")
    
elif a == 1 and b == 2:
    print("Medium rain fall.")
    
elif a == 1 and b == 3 :
    print("High rain fall.")
    
elif a == 1 and b == 4 :
    print("Low rainfall.")
    
elif a == 2 and b == 1 :
    print("Enjoy eating oranges on the roof.")
    
elif a == 2 and b == 2 :
    print("You need to start your fans.")
    
elif a == 2 and b == 3:
    print("You need to start your AC.")
    
elif a == 2 and b == 4:
    print("You have not need to start your AC or fans.")

elif a == 3 and b == 1 :
    print("Enjoy the weather.")

elif a == 3 and b == 2 :
    print("Enjoy the wind.")
    
elif a == 3 and b == 3 :
    print("Now you have relax from heat.")
    
elif a == 3 and b == 4 :
    print("You need to take tea.")
    
elif a == 4 and b == 1 :
    print("Mediun thunderstorm or snow fall.")
    
elif a == 4 and b == 2 :
    print("Med rainfall.")
    
elif a == 4 and b == 3 :
    print("High rainfall.")
    
elif a == 4 and b == 4 :
    print("Snow fall.")
    
else :
    print("No comments.")