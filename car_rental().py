def car_rental():
    available_City = 7
    available_Cultus = 5
    available_Prado = 2
    print("----------------------------------------------------------------------------------------------------------")
    print("   Car Model""     ""No. of Cars Available""   ""Rent Cost""      ""Liablity Insurance/Day""   ""Comprehensive Insurance/Day")
    print("-----------------------------------------------------------------------------------------------------------")
    print("1-","City","           ",available_City,"                ""$12,000""               "" $420""                      ""  $500")
    print("2-","Cultus","         ",available_Cultus,"                ""$8,000""                "" $350""                      ""  $450")
    print("3-","Prado","          ",available_Prado,"                ""$7,900""                ""  $400""                      ""  $700")
    print("-----------------------------------------------------------------------------------------------------------")
    car=int(input("Which Car Model do you want? Enter a number from 1-3:"))
    while car > 3 or car < 1 :
            car=int(input("Error, Please enter a valid number to select the car:"))

    days=int(input("For how many days do you want to rent the car?:"))
    insurance=input("Press F for comprehensive insurace or Press L for liability insurance:")
    while not(insurance=='f' or insurance=='l' or insurance=='F' or insurance=='L'):
        insurance=input("Error, Please press F for comprehensive insurance or press L for liability insurance:")
    print("-----------------------------------------------------------------------------")
    if car==1:
        available_City = available_City - 1
        def City():
            print("Car name: City")
            rent_cost = 12000
            tax = rent_cost*0.05
            liability_insurance = 420
            comprehensive_insurance = 500
            print("Rent Cost of City : ", rent_cost)
            print("Tax (5% of rent_cost):", tax)
            if insurance=='f' or 'F':
                print("Insurance cost:", comprehensive_insurance)
                print("-----------------------------------------------------------")
                total_City= tax + (rent_cost*days) + comprehensive_insurance
                print("Total:" "$", total_City)
            else:
                    if insurance=='L' or insurance=='l':
                        print("Insurance cost:", liability_insurance)
                        print("---------------------------------------------------------")
                        total_City = tax + (rent_cost*days) + liability_insurance
                        print("Total:" "$", total_City)
        City()
        
    if car==2:
        available_Cultus = available_Cultus - 1
        def Cultus():
            print("Car name: Cultus")
            rent_cost = 8000
            tax = rent_cost*0.05
            liability_insurance = 350
            comprehensive_insurance = 450
            print("Rent Cost of Cultus : ", rent_cost)
            print("Tax (5% of rent_cost):", tax)
            if insurance=='f' or 'F':
                print("Insurance cost:", comprehensive_insurance)
                print("-----------------------------------------------------------")
                total_Cultus= tax + (rent_cost*days) + comprehensive_insurance
                print("Total:" "$", total_Cultus)
            else:
                    if insurance=='l' or 'L':
                        print("Insurance cost:", liability_insurance)
                        print("---------------------------------------------------------")
                        total_Cultus = tax + (rent_cost*days) + liability_insurance
                        print("Total:" "$",total_Cultus)
        Cultus()
        
    if car==3:
        available_Prado=available_Prado-1
        def Prado():
            print("Car name: Prado")
            rent_cost = 7900
            tax = rent_cost*0.05
            liability_insurance = 400
            comprehensive_insurance = 700
            print("Rent Cost of Prado : ", rent_cost)
            print("Tax (5% of rent_cost):", tax)
            if insurance=='f' or 'F':
                print("Insurance cost:", comprehensive_insurance)
                print("-----------------------------------------------------------")
                total_Prado= tax + (rent_cost*days) + comprehensive_insurance
                print("Total:" "$",total_Prado)
            else:
                    if insurance=='l' or 'L':
                        print("Insurance cost:", liability_insurance)
                        print("---------------------------------------------------------")
                        total_Prado = tax + (rent_cost*days) + liability_insurance
                        print("Total:" "$",total_Prado)
        Prado()                
car_rental()


