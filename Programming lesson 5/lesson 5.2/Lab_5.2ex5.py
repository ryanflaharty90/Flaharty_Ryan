print("You decide to explore the world...")
choice = input("Visit europe or South America?")

if choice == "europe":
    europe = input("Visit England, or Germany?")
    if europe == "England":
        england = input("Visit london or liverpool?")
        if england == "London":
            print("You enjoy visiting landmarks such as Big Ben and Parliament")
        else:
            print("You have a blast at one of the infamous liverpool soccer matches")
    else:
        germany = input("Visit Berlin or Munich?")
        if germany == "Berlin":
            print("You are marveled at the incredible culture and history in germanys nototious capitol") 
        else:
            print("The architecture and overall structure of the city gives you goosebumps")

else:
    southamerica = input("Visit Peru or Brazil?")
    if southamerica == "Peru":
        peru = input("Visit Lima, or Cusco?")
        if peru == "Lima":
            print("You enjoy your visit in peru's vibrant capitol")
        else:
            print("Cusco was cool, but Machu Pichu was better")
    else:
        brazil = input("Visit Rio, or Sau Paulo?")
        if brazil == "Rio":
            print("The olympics was a once in a lifetime experience and was amazing")
        else:
            print("Sau Paulo's rich traditions entices you")
            
            
