#restro managemebt system
#define the menu of resturent 
menu={
    'pizza':120
    'Paneer' :60
    'burger':70
    'coffe':80
    'momos':50
    }
    #great
    print("welcome to SHANTI Resturent")
    print("pizza:Rs120\nPasta: Rs60\nburger :Rs70\ncofee :Rs80\nmomos :Rs50")
    
    order_total=0
    
    item_1=input("enter the name of item u waant to order=")
    if item_1 in menu:
        order_toatal += menu[item_1]#0+
        print(f"your item {item_1}has been added to your ordr ")
        
        else:
            print(f"ordered item{ite_1} is not avilable yet!")
            
       another_order= input("do u want to add another item ?(yes/no)")
       item_2=input("enter the name of ssecond item =") 
       if item_2 in  menu:       
       order_total +=menu[item_2]
           print(f"Item {item_2} has beeen added to the item")
           else:
               print(F"Order item{item_2} is not avilable !")
               
               print(f "the total amount of item is {order_total}")
        