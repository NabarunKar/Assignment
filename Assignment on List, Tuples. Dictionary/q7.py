def Total_Bill(StoreList,Customer_List):
    total = 0
    for item in Customer_List:
        if item in StoreList:
            cost = StoreList[item] * Customer_List[item]
            total += cost
        else:
            return -1
    return total

Products = { "Game": 40000, "TV": 45000, "Refrigerator": 14000, "Washing Machine": 6000, "Pendrive": 700 }
CustomerProducts = { "Game": 3, "TV": 1, "Pendrive": 5 }


print("Your total bill: Rs " , Total_Bill(Products,CustomerProducts))