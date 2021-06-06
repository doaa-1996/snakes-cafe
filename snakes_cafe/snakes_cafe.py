
print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls
Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden
Desserts
--------
Ice Cream
Cake
Pie
Drinks
------
Coffee
Tea
Unicorn Tears
***********************************
** What would you like to order? **
***********************************
""")






menu={'Wings':0,'Cookies':0,'Spring Rolls':0,'Salmon':0 ,'Steak':0,'Meat Tornado':0,'A Literal Garden':0,'Ice Cream':0,'Cake':0,'Pie':0,'Coffee':0,'Tea':0,'Unicorn_Tears':0}
def handle_menu():
    order=0
    while (order!="quit"):
        order= input(">")
        if (order == "quit"):
          break
        for item in menu :
            if order == item :
                menu[order]+=1
                print(f"** {menu[order]} order of {item} have been added to your meal **")
                break
        else:
            print("This order is not available")
handle_menu()  