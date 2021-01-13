import Creatures

print('Find your information about the following creatures ')

while(1):
    print("Press\n1.For Fish\n2.For Birds\n3.For Reptiles\n4.For Amphibians\n5.For Mammals \n6.Exit\n\n")
    ch=int(input())
    if ch==1:
        Creatures.Fish.examples()
        Creatures.Fish.chars()
    elif ch==2:
        Creatures.Birds.examples()
        Creatures.Birds.chars()

    elif ch==3:
        Creatures.Reptiles.examples()
        Creatures.Reptiles.chars()

    elif ch==4:
        Creatures.Amphibians.examples()
        Creatures.Amphibians.chars()

    elif ch==5:
        Creatures.Mammals.examples()
        Creatures.Mammals.chars()

    elif ch==6:
        print('Thank you!') 
        break
    else:
        print('Wrong Input!')