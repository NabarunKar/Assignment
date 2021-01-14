import creatures

print('Find your information about the following creatures: ')

while(1):
    print("Press\n1.For fish\n2.For birds\n3.For reptiles\n4.For amphibians\n5.For mammals \n6.Exit\n")
    ch=int(input())
    if ch==1:
        creatures.fish.examples()
        creatures.fish.chars()
    elif ch==2:
        creatures.birds.examples()
        creatures.birds.chars()

    elif ch==3:
        creatures.reptiles.examples()
        creatures.reptiles.chars()

    elif ch==4:
        creatures.amphibians.examples()
        creatures.amphibians.chars()

    elif ch==5:
        creatures.mammals.examples()
        creatures.mammals.chars()

    elif ch==6:
        print('Thank you!') 
        break
    else:
        print('Wrong Input!')