import os
owner_name=0
owner_pass=0
customer={
    "none":{"none":{"apple":0,"banana":0,"cherry":0},},
}
customer_name=0
customer_pass=0
shop={"apple":40,"banana":30,"cherry":70}
costs={"apple":15,"banana":20,"cherry":10}
bill={"total":0,"apple":0,"banana":0,"cherry":0}
while 1:
    bill_print=1
    os.system('cls')
    select=input("\nSelect Mode For customer press 1 ,\nfor owner press 2 ,\nto exist press 0  :  ")
    if select=='1':
        os.system('cls')
        user_name=input("\nenter the customer name : ")
        os.system('cls')
        user_password=input("\nenter the password : ")
        if user_name in customer.keys():
            if user_password in customer[user_name].keys():
               while bill_print:
                    os.system('cls')
                    select=input("\nTo show our products press 1 ,\nTo Buy from our products press 2 ,\nto print the bill press 3 : ")
                    if select=='1':
                        print("shop : ",shop)
                    elif select=='2':
                        os.system('cls')
                        user_take=input("\nenter the product name and number of taken elements with separating space between them : ").split(" ")
                        user_take[1]=int(user_take[1])
                        if shop[user_take[0]]>=user_take[1] :
                            shop[user_take[0]]-=user_take[1]
                            customer[user_name][user_password][user_take[0]]+=costs[user_take[0]]*user_take[1]
                            customer[user_name][user_password]["total"]=0;
                            for x in customer[user_name][user_password]:
                               if x!="total":
                                   customer[user_name][user_password]["total"]+=customer[user_name][user_password][x]
                            input()
                        else:
                            print("\nthere are no "+user_take[1])
                            break
                    elif select=='3':
                        print("\nthe bill : ",customer[user_name][user_password])
                        bill_print=0
                    
            else:
                print(" wrong password :")
                
        else:
            print("there are no customer with the name : "+user_name)
       
    elif select=='2':
        if owner_name==0:
              print("there are no owner ")
        else:
            os.system('cls')
            temp_owner_name=input("enter the owner name :")
            os.system('cls')
            temp_owner_pass=input("enter the owner password :")
            if temp_owner_name!=owner_name or temp_owner_pass!=owner_pass:
               print("wrong name or password ")
            else:
                os.system('cls')
                select=input('\nto add new products press 1\nto Show Products press 2 \nto change cost press 3 : ')  
                if select=='1':
                        os.system('cls')
                        user_take=input('\nenter the new product name , quantity ,and cost with seperating spaces between them :').split(' ',3)
                        if user_take[1].isdigit():
                            if user_take[2].isdigit():
                                shop[user_take[0]]=int(user_take[1])
                                costs[user_take[0]]=int(user_take[2])
                                for select in customer:
                                    for subselect in customer[select]:
                                        customer[select][subselect][user_take[0]]=0
                            else:
                                print("wrong format for a cost value")
                        else:
                            print("wrong format for a quantity value")                 
                elif select=='2':
                    print("shop : ",shop)
                elif select=='3':
                    os.system('cls')
                    user_take=input('enter the product name and the new cost with seperating spaces between them :').split(' ',2)
                    if user_take[0] in costs.keys():
                        if user_take[1].isdigit():
                            costs[user_take[0]]=int(user_take[1])
                        else:
                            print("wrong format for a cost value")
                    else:
                       print("there are no product with this name")
                else:
                    print("undefined option")   
    elif select=='0':
        os.system('cls')
        select=input("to exist customer press 1\nto exist owner press 2 :")
        if select=='2':
           if owner_name==0:
              os.system('cls')
              owner_name=input("enter the owner name :")
              os.system('cls')
              owner_pass=input("enter the owner password :")
           else:
            print("there are exist owner")
        elif select=='1':
            os.system('cls')
            customer_name=input("enter the customer name :")
            os.system('cls')
            customer_pass=input("enter the customer password :")
            if customer_name in customer.keys():
              print('error : there are an exist customer with the same name')
            else:
              customer[customer_name]={}
              customer[customer_name][customer_pass]=bill
        else:
            print("undefined option")   
    else:
        print("undefined option")               
    input()
