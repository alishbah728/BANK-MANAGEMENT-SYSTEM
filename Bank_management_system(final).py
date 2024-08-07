class bankaccount:
    #Account opening
    def account(self):
        
        print("Welcome to our bank !! How can we help you??")
        
        choice=int(input("1)Create new account\n2)Login to account \n3)Close/Delete your account\n Enter your choice:"))
        
        #create new account
        if (choice==1):
                print("Your request for account creating is accepted")
                print("Please fill this application form in order to create new account ")
                print("<<<APPLICATION FORM>>>")
                name=input("Enter your name:")
                email=input("Enter your Email:")
                address=input("Enter your address:")
                PA=input("Enter your permanent address:")
                CNIC=input("Enter your CNIC number:")
                age=int(input("Enter your age:"))
                if (age<18):
                    print("Sorry !! you are not eligible")
                else:
                
                    Type=int(input("Enter the type of account.\n1)current account\n2)saving account\nEnter your choice:"))
                    if (Type==1):
                        print("You have chosen current account , Now you have to deposit minimum amount of Rs.500 in order to proceed")
                        Deposit=int(input("Enter the amount you are depositing:"))
                        if Deposit>=500:
                            print("Your amount has been deposited")
                            Ch=int(input("Are you sure to want to create account? \n1)Create my account\n2)Cancel my request for opening account \n Enter your choice:"))
                            if (Ch==1):
                                print("Your current account has been created successfully")
                                print("Please submit the following documents alongwith application form to any branch of our bank")
                                print("*)Copy of birth certificate/B-form/Educational certificate \n*)Driving license \n*)Salary slip/Pension book \n*)A copy of CNIC")
                                print("Your account ID and title and other information will be send to you via email")
                                print("THANK YOU !! HAVE A GOOD DAY!")
                            elif(Ch==2):
                                print("Your cancellation request is accepted")
                                print("Your deposited amount have been returned to you")
                            else:
                                print("Invalid choice")
                                
                        else:
                            print("Insufficient amount")
                    elif(Type==2):
                        print("You have chosen saving account , Now you have to deposit minimum amount of Rs.1000 in order to proceed")
                        deposit=int(input("Enter the amount you are depositing:"))
                        if deposit>=1000:
                            print("Your amount has been deposited")
                            Ch=int(input("Are you sure to want to create account? \n1)Create my account\n2)Cancel my request for opening account.\nEnter your choice: "))
                            if (Ch==1):
                                print("Your saving account has been created successfully")
                                print("Please submit the following documents alongwith application form to any branch of our bank")
                                print("*)Copy of birth certificate/B-form/Educational certificate \n*)Driving license \n*)Salary slip/Pension book \n*)A copy of CNIC")
                                print("Your account ID and title and other information will be send to you via email")
                                print("THANK YOU !! HAVE A GOOD DAY!")
                            elif(Ch==2):
                               print("Your cancellation request is accepted")
                               print("Your deposited amount have been returned to you")
                            else:
                               print("Invalid choice")
                        else:
                            print("Insufficient amount")
                    else:
                        print("Invalid choice")
        # login in to account
        
        if(choice==2):
            a=input("Enter account number:")
            b=input("Enter Account title:")
            p=input("Enter password:")
            if  a=="3343673191" and b=="ANOOSHA MEHAK" and p=="*****":
                print("You have logged into your account!!")
                          
                while True:
                    
                    self.balance=2500
                    print("What do you want to do??")
                    
                    c=int(input("1)Deposit money \n2)Withdraw money \n3)Transfer money \n4)Check your current balance \n5)Apply for loan \n6)Logout\nEnter your choice:"))
                    
                    if c==1:
                                self.amount=float(input("Enter amount to be Deposit: "))
                                self.balance += self.amount
                                opt=input("Are you sure to want to deposit money??")
                                if opt=="YES":
                                    print("Your amount has been deposited successfully")
                                    print("\n Net Available Balance:Rs",self.balance) 
                                    
                                else:
                                    print("Your request for depositing money has been cancelled!")
                    if c==2:
                                amount = float(input("Enter amount to be Withdrawn: "))
                                if amount>=50000:
                                    print("You cannot withdraw money more than 50,000Rs at a time!!")
                                else:
                                    if self.balance>=amount:
                                        self.balance-=amount
                                        opt=input("Are you sure to want to withdraw money??")
                                        if opt=="YES":
                                            print("Your amount has been withdrawn successfully")
                                            print("\n Net Available Balance:Rs",self.balance)  
                                        else:
                                            print("Your request for money withdrawn has been cancelled!")
                                        
                                    else:
                                        print("\n Insufficient balance  ")
                                print("\n Net Available Balance=",self.balance)
                                
                    if c==3:
                                amount = float(input("Enter amount to be transfer:Rs "))
                                if self.balance>=amount:
                                    int(input("Enter the recievers account number:"))
                                    int(input("Enter the receiver's bank branch code:"))
                                    opt=input("Are you sure to want to transfer money??")
                                    if opt=="YES":
                                        print("Your amount has been transferred successfully!")
                                        self.balance = self.balance - amount
                                        print("\nNet Available Balance= Rs.",self.balance)
                                    else:
                                        print("Your request for transferring money has been cancelled")
                    
                                else:
                                    print("Insufficient balance")
                                   
                                
                    if c==4:
                                print('Your current balance is: Rs.',self.balance)
                    if c==5:
                        print("<<FULFIL YOUR DREAMS WITH OUR LOAN PRODUCTS>>")
                        print(" With our personal finance , you can realize your dreams be it transforming your house into your dream house with all desired luxuries,making wedding a memorable event, gearing up with latest gadgets or enjoying holidays with family and friends at your dream detinations!! \n Just apply to our personal finance and repay in easy monthly installments with peace of mind")
                        print("<<FEATURES AND BENEFITS>>")
                        print("*)Easy loan repayment in equal monthly installment \n *)Flexibility to choose repayment period from 1 to 3 years \n *) Loan amount from Rs. 30,000/- to Rs. 3,000,000/- \n *)Interest of 5% per year \n *)No hidden cost ")
                        print("We offer you the following loans: \n 1) Car loan \n 2)Home loan \n 3)Marriage loan ")
                        ch=int(input("Which type of loan do you want?? \n Enter your choice:"))
                        if (ch==1):
                                print("A flexible and hassle-free financing facility that enables you to own your dream car!!")
                                print("If you want to apply for this loan ,Please fill this eligibility form(IN BLOCK LETTERS) ")
                                print("<<<ELIGIBILITY FORM>>>")
                                nationality=input("what is your nationality??\n")
                                if nationality != "PAKISTANI" :
                                    print("Sorry!! you are not eligible for car loan")
                                else:
                                   age=int(input("what is your age??\n"))
                                   if age<21 :
                                        print("Sorry!! you are not eligible for car loan")
                                   else:
                                        bank=input("Are you our 6 or more than 6 months old customer??\n")
                                        if bank !="YES":
                                            print("Sorry!! you are not eligible for car loan")
                                        else:
                                            salary=int(input("What is your monthly income??\n"))
                                            if salary < 40000:
                                                print("Sorry!! you are not eligible for car loan")
                                            else:
                                                dep=int(input("How many dependants you have??\n"))
                                                if dep>6:
                                                    print("Sorry!! you are not eligible for car loan.")
                                                else: 
                                                    print("Congratulations !! You are eligible for this loan. \n Please fill this application form(IN BLOCK LETTERS) \n")
                                                    print("<<<APPLICATION FORM>>>")
                                                    Q=input("Enter your name: ")
                                                    W=input("Enter your CNIC number :")
                                                    A=input("Enter your profession:")
                                                    if (A!="BUSINESSMAN"):
                                                        R=input("Enter your employee type(govt/private) :")
                                                    Y=int(input("Enter your mobile number:"))               
                                                    U=input("Enter your organization name:")
                                                    I=input("Enter your city:")
                                                    O=int(input("Enter your loan amount(from Rs. 30,000/- to Rs. 3,000,000/-):"))
                                                    P=input("Enter your email address:")
                                                    U=input("Enter your address:")
                                                    V=input("Enter your permanent address:")
                                                    E=input("Enter your desired loan repayment period( from 1 to 3 years) :")
                                                   
                                                    
                                                    
                                                    print("\n Please submit the following documents to any branch of our bank.")
                                                    print("1)Last 6 month's bank statement \n 2)Copy of CNIC / Smart card \n 3)2 recent passport size pictures \n 4)Last two month's salay slip or salary certificate, clerly indicating gross and net salary with details of all deductions \n 5)Complete and duly signed APPLICATION FORM with signature verification from branch. ")
                                                    print("THANK YOU !! HAVE  GOOD DAY !!")
                        if (ch==2):
                                            print("A flexible and hassle-free financing facility that enables you to own your dream house!!")
                                            print("If you want to apply for this loan ,Please fill this eligibility form(IN BLOCK LETTERS) ") 
                                            print("<<<ELIGIBILITY FORM>>>")                               
                                            nationality=input("what is your nationality??\n")
                                            if nationality != "PAKISTANI" :
                                                print("Sorry!! you are not eligible for home loan")
                                            else:
                                               age=int(input("what is your age??\n"))
                                               if age<21 :
                                                    print("Sorry!! you are not eligible for home loan")
                                               else:
                                                    bank=input("Are you our 6 or more than 6 months old customer??\n")
                                                    if bank !="YES":
                                                        print("Sorry!! you are not eligible for home loan")
                                                    else:
                                                        salary=int(input("What is your monthly income??\n"))
                                                        if salary < 40000:
                                                            print("Sorry!! you are not eligible for home loan")
                                                        else:
                                                            dep=int(input("How many do dependants you have??\n"))
                                                            if dep>6:
                                                                print("Sorry!! you are not eligible for home loan")
                                                            else: 
                                                                print("Congratulations !! You are eligible for this loan. \n Please fill this application form(IN BLOCK LETTERS) ")
                                                                print("<<<APPLICATION FORM>>>")
                                                                Q=input("Enter your name: ")
                                                                W=input("Enter your CNIC number :")
                                                                A=input("Enter your profession:")
                                                                if (A!="BUSINESSMAN"):
                                                                    R=input("Enter your employee type(govt/private):")
                                                                Y=int(input("Enter your mobile number:"))               
                                                                U=input("Enter your workplace:")
                                                                I=input("Enter your city:")
                                                                O=int(input("Enter your loan amount(from Rs. 30,000/- to Rs. 3,000,000/-):"))
                                                                P=input("Enter your email address:")
                                                                U=input("Enter your address:")
                                                                V=input("Enter your permanent address:")
                                                                E=input("Enter your desired loan repayment period( from 1 to 3 years) :")
                                                                
                                                                
                                                                
                                                                print("Please submit the following documents to any branch of our bank.")
                                                                print("1)Last 6 month's bank statement \n 2)Copy of CNIC / Smart card \n 3)2 recent passport size pictures \n 4)Last two month's salay slip or salary certificate, clearly indicating gross and net salary with details of all deductions \n 5)Complete and duly signed APPLICATION FORM with signature verification from branch.\n 6)Copy of property documents ")
                                                                print("THANK YOU !! HAVE  GOOD DAY !!")
                                    
                                    
                        if (ch==3):
                                        print("A flexible and hassle-free financing facility that heps you in building your future!!")
                                        print("If you want to apply for this loan ,Please fill this eiligibility form(IN BLOCK LETTERS) ")
                                        print("<<<ELIGIBILITY FORM>>>")
                                        nationality=input("what is your nationality??\n")
                                        if nationality != "PAKISTANI" :
                                            print("Sorry!! you are not eligible for car loan")
                                        else:
                                            age=int(input("what is your age??\n"))
                                            if age<21 :
                                                 print("Sorry!! you are not eligible for home loan")
                                            else:
                                                 bank=input("Are you our 6 or more than 6 months old customer??\n")
                                                 if bank !="YES":
                                                     print("Sorry!! you are not eligible for home loan")
                                                 else:
                                                     salary=int(input("What is your monthly income??\n"))
                                                     if salary < 40000:
                                                         print("Sorry!! you are not eligible for home loan")
                                                     else:
                                                         dep=int(input("How many dependants do you have??\n"))
                                                         if dep>6:
                                                             print("Sorry!! you are not eligible for home loan")
                                                         else: 
                                                             print("Congratulations !! You are eligible for this loan. \n Please fill this application form(IN BLOCK LETTERS) ")
                                                             print("<<<APPLICATION FORM>>>")
                                                             Q=input("Enter your name: ")
                                                             W=input("Enter your CNIC number :")
                                                             A=input("Enter your profession:")
                                                             if (A!="BUSINESSMAN"):
                                                                 R=input("Enter your employee type(govt/private):")
                                                             Y=int(input("Enter your mobile number:"))               
                                                             U=input("Enter your workplace:")
                                                             I=input("Enter your city:")
                                                             O=int(input("Enter your loan amount(from Rs. 30,000/- to Rs. 3,000,000/-):"))
                                                             P=input("Enter your email address:")
                                                             U=input("Enter your address:")
                                                             V=input("Enter your permanent address:")
                                                             E=input("Enter your desired loan repayment period( from 1 to 3 years) :")
                                                             
                                                             
                                                             
                                                             print("Please submit the following documents to any branch of our bank.")
                                                             print("1)Last 6 month's bank statement \n 2)Copy of CNIC / Smart card \n 3)2 recent passport size pictures \n 4)Last two month's salay slip or salary certificate, clearly indicating gross and net salary with details of all deductions \n 5)Complete and duly signed APPLICATION FORM with signature verification from branch.\n 6)Copy of property documents ")
                                                             print("THANK YOU !! HAVE  GOOD DAY !!")
                    
                    else:
                        print("Your account has been logged out.")
                        break
                        
                    
            elif a=="3100123308" and b=="SOBIA YAMEEN" and p=="*****":
                print("You have logged into your account!!")
                while True:
                    
                    self.balance=2000
                    print("What do you want to do??")
                    c=int(input("1)Deposit money \n2)Withdraw money \n3)Transfer money \n4)Check your current balance \n5)Apply for loan \n6)Logout\nEnter your choice:"))
                    if c==1:
                                self.amount=float(input("Enter amount to be Deposit: "))
                                self.balance += self.amount
                                opt=input("Are you sure to want to deposit money??")
                                if opt=="YES":
                                    print("Your amount has been deposited successfully")
                                    print("\n Net Available Balance:Rs",self.balance) 
                                    
                                else:
                                    print("Your request for depositing money has been cancelled!")
                    if c==2:
                                amount = float(input("Enter amount to be Withdrawn: "))
                                if amount>=50000:
                                    print("You cannot withdraw money more than 50,000Rs at a time!!")
                                else:
                                    if self.balance>=amount:
                                        self.balance-=amount
                                        opt=input("Are you sure to want to withdraw money??")
                                        if opt=="YES":
                                            print("Your amount has been withdrawn successfully")
                                            print("\n Net Available Balance:Rs",self.balance)  
                                        else:
                                            print("Your request for money withdrawn has been cancelled!")
                                        
                                    else:
                                        print("\n Insufficient balance  ")
                                print("\n Net Available Balance=",self.balance)
                                
                    if c==3:
                                amount = float(input("Enter amount to be transfer:Rs "))
                                if self.balance>=amount:
                                    int(input("Enter the recievers account number:"))
                                    int(input("Enter the receiver's bank branch code:"))
                                    opt=input("Are you sure to want to transfer money??")
                                    if opt=="YES":
                                        print("Your amount has been transferred successfully!")
                                        self.balance = self.balance - amount
                                        print("\nNet Available Balance= Rs.",self.balance)
                                    else:
                                        print("Your request for transferring money has been cancelled")
                    
                                else:
                                    print("Insufficient balance")
                                   
                                
                    if c==4:
                                print('Your current balance is: Rs.',self.balance)
                    if c==5:
                        print("<<FULFIL YOUR DREAMS WITH OUR LOAN PRODUCTS>>")
                        print(" With our personal finance , you can realize your dreams be it transforming your house into your dream house with all desired luxuries,making wedding a memorable event, gearing up with latest gadgets or enjoying holidays with family and friends at your dream detinations!! \n Just apply to our personal finance and repay in easy monthly installments with peace of mind")
                        print("<<FEATURES AND BENEFITS>>")
                        print("*)Easy loan repayment in equal monthly installment \n *)Flexibility to choose repayment period from 1 to 3 years \n *) Loan amount from Rs. 30,000/- to Rs. 3,000,000/- \n *)Interest of 5% per year \n *)No hidden cost ")
                        print("We offer you the following loans: \n 1) Car loan \n 2)Home loan \n 3)Marriage loan ")
                        ch=int(input("Which type of loan do you want?? \n Enter your choice:"))
                        if (ch==1):
                                print("A flexible and hassle-free financing facility that enables you to own your dream car!!")
                                print("If you want to apply for this loan ,Please fill this eligibility form(IN BLOCK LETTERS) ")
                                print("<<<ELIGIBILITY FORM>>>")
                                nationality=input("what is your nationality??\n")
                                if nationality != "PAKISTANI" :
                                    print("Sorry!! you are not eligible for car loan")
                                else:
                                   age=int(input("what is your age??\n"))
                                   if age<21 :
                                        print("Sorry!! you are not eligible for car loan")
                                   else:
                                        bank=input("Are you our 6 or more than 6 months old customer??\n")
                                        if bank !="YES":
                                            print("Sorry!! you are not eligible for car loan")
                                        else:
                                            salary=int(input("What is your monthly income??\n"))
                                            if salary < 40000:
                                                print("Sorry!! you are not eligible for car loan")
                                            else:
                                                dep=int(input("How many dependants you have??\n"))
                                                if dep>6:
                                                    print("Sorry!! you are not eligible for car loan.")
                                                else: 
                                                    print("Congratulations !! You are eligible for this loan. \n Please fill this application form(IN BLOCK LETTERS) \n")
                                                    print("<<<APPLICATION FORM>>>")
                                                    Q=input("Enter your name: ")
                                                    W=input("Enter your CNIC number :")
                                                    A=input("Enter your profession:")
                                                    if (A!="BUSINESSMAN"):
                                                        R=input("Enter your employee type(govt/private) :")
                                                    Y=int(input("Enter your mobile number:"))               
                                                    U=input("Enter your organization name:")
                                                    I=input("Enter your city:")
                                                    O=int(input("Enter your loan amount(from Rs. 30,000/- to Rs. 3,000,000/-):"))
                                                    P=input("Enter your email address:")
                                                    U=input("Enter your address:")
                                                    V=input("Enter your permanent address:")
                                                    E=input("Enter your desired loan repayment period( from 1 to 3 years) :")
                                                   
                                                    
                                                    
                                                    print("\n Please submit the following documents to any branch of our bank.")
                                                    print("1)Last 6 month's bank statement \n 2)Copy of CNIC / Smart card \n 3)2 recent passport size pictures \n 4)Last two month's salay slip or salary certificate, clerly indicating gross and net salary with details of all deductions \n 5)Complete and duly signed APPLICATION FORM with signature verification from branch. ")
                                                    print("THANK YOU !! HAVE  GOOD DAY !!")
                        if (ch==2):
                                            print("A flexible and hassle-free financing facility that enables you to own your dream house!!")
                                            print("If you want to apply for this loan ,Please fill this eligibility form(IN BLOCK LETTERS) ") 
                                            print("<<<ELIGIBILITY FORM>>>")                               
                                            nationality=input("what is your nationality??\n")
                                            if nationality != "PAKISTANI" :
                                                print("Sorry!! you are not eligible for home loan")
                                            else:
                                               age=int(input("what is your age??\n"))
                                               if age<21 :
                                                    print("Sorry!! you are not eligible for home loan")
                                               else:
                                                    bank=input("Are you our 6 or more than 6 months old customer??\n")
                                                    if bank !="YES":
                                                        print("Sorry!! you are not eligible for home loan")
                                                    else:
                                                        salary=int(input("What is your monthly income??\n"))
                                                        if salary < 40000:
                                                            print("Sorry!! you are not eligible for home loan")
                                                        else:
                                                            dep=int(input("How many do dependants you have??\n"))
                                                            if dep>6:
                                                                print("Sorry!! you are not eligible for home loan")
                                                            else: 
                                                                print("Congratulations !! You are eligible for this loan. \n Please fill this application form(IN BLOCK LETTERS) ")
                                                                print("<<<APPLICATION FORM>>>")
                                                                Q=input("Enter your name: ")
                                                                W=input("Enter your CNIC number :")
                                                                A=input("Enter your profession:")
                                                                if (A!="BUSINESSMAN"):
                                                                    R=input("Enter your employee type(govt/private):")
                                                                Y=int(input("Enter your mobile number:"))               
                                                                U=input("Enter your workplace:")
                                                                I=input("Enter your city:")
                                                                O=int(input("Enter your loan amount(from Rs. 30,000/- to Rs. 3,000,000/-):"))
                                                                P=input("Enter your email address:")
                                                                U=input("Enter your address:")
                                                                V=input("Enter your permanent address:")
                                                                E=input("Enter your desired loan repayment period( from 1 to 3 years) :")
                                                                
                                                                
                                                                
                                                                print("Please submit the following documents to any branch of our bank.")
                                                                print("1)Last 6 month's bank statement \n 2)Copy of CNIC / Smart card \n 3)2 recent passport size pictures \n 4)Last two month's salay slip or salary certificate, clearly indicating gross and net salary with details of all deductions \n 5)Complete and duly signed APPLICATION FORM with signature verification from branch.\n 6)Copy of property documents ")
                                                                print("THANK YOU !! HAVE  GOOD DAY !!")
                                    
                                    
                        if (ch==3):
                                        print("A flexible and hassle-free financing facility that heps you in building your future!!")
                                        print("If you want to apply for this loan ,Please fill this eiligibility form(IN BLOCK LETTERS) ")
                                        print("<<<ELIGIBILITY FORM>>>")
                                        nationality=input("what is your nationality??\n")
                                        if nationality != "PAKISTANI" :
                                            print("Sorry!! you are not eligible for car loan")
                                        else:
                                            age=int(input("what is your age??\n"))
                                            if age<21 :
                                                 print("Sorry!! you are not eligible for home loan")
                                            else:
                                                 bank=input("Are you our 6 or more than 6 months old customer??\n")
                                                 if bank !="YES":
                                                     print("Sorry!! you are not eligible for home loan")
                                                 else:
                                                     salary=int(input("What is your monthly income??\n"))
                                                     if salary < 40000:
                                                         print("Sorry!! you are not eligible for home loan")
                                                     else:
                                                         dep=int(input("How many dependants do you have??\n"))
                                                         if dep>6:
                                                             print("Sorry!! you are not eligible for home loan")
                                                         else: 
                                                             print("Congratulations !! You are eligible for this loan. \n Please fill this application form(IN BLOCK LETTERS) ")
                                                             print("<<<APPLICATION FORM>>>")
                                                             Q=input("Enter your name: ")
                                                             W=input("Enter your CNIC number :")
                                                             A=input("Enter your profession:")
                                                             if (A!="BUSINESSMAN"):
                                                                 R=input("Enter your employee type(govt/private):")
                                                             Y=int(input("Enter your mobile number:"))               
                                                             U=input("Enter your workplace:")
                                                             I=input("Enter your city:")
                                                             O=int(input("Enter your loan amount(from Rs. 30,000/- to Rs. 3,000,000/-):"))
                                                             P=input("Enter your email address:")
                                                             U=input("Enter your address:")
                                                             V=input("Enter your permanent address:")
                                                             E=input("Enter your desired loan repayment period( from 1 to 3 years) :")
                                                             
                                                             
                                                             
                                                             print("Please submit the following documents to any branch of our bank.")
                                                             print("1)Last 6 month's bank statement \n 2)Copy of CNIC / Smart card \n 3)2 recent passport size pictures \n 4)Last two month's salay slip or salary certificate, clearly indicating gross and net salary with details of all deductions \n 5)Complete and duly signed APPLICATION FORM with signature verification from branch.\n 6)Copy of property documents ")
                                                             print("THANK YOU !! HAVE  GOOD DAY !!")
      
                    if c==6:
                        print("Your account has been logged out.")
                        break
                       
                    else:
                        print("Invalid choice")
            
            elif a=="3039704442" and b=="AYESHA NISAR" and p=="*****":
                print("You have logged into your account!!")
                while True:
                    
                    self.balance=3000
                    print("What do you want to do??")
                    c=int(input("1)Deposit money \n2)Withdraw money \n3)Transfer money \n4)Check your current balance \n5)Apply for loan \n6)Logout\nEnter your choice:"))
                    if c==1:
                                self.amount=float(input("Enter amount to be Deposit: "))
                                self.balance += self.amount
                                opt=input("Are you sure to want to deposit money??")
                                if opt=="YES":
                                    print("Your amount has been deposited successfully")
                                    print("\n Net Available Balance:Rs",self.balance) 
                                    
                                else:
                                    print("Your request for depositing money has been cancelled!")
                    if c==2:
                                amount = float(input("Enter amount to be Withdrawn: "))
                                if amount>=50000:
                                    print("You cannot withdraw money more than 50,000Rs at a time!!")
                                else:
                                    if self.balance>=amount:
                                        self.balance-=amount
                                        opt=input("Are you sure to want to withdraw money??")
                                        if opt=="YES":
                                            print("Your amount has been withdrawn successfully")
                                            print("\n Net Available Balance:Rs",self.balance)  
                                        else:
                                            print("Your request for money withdrawn has been cancelled!")
                                        
                                    else:
                                        print("\n Insufficient balance  ")
                                print("\n Net Available Balance=",self.balance)
                                
                    if c==3:
                                amount = float(input("Enter amount to be transfer:Rs "))
                                if self.balance>=amount:
                                    int(input("Enter the recievers account number:"))
                                    int(input("Enter the receiver's bank branch code:"))
                                    opt=input("Are you sure to want to transfer money??")
                                    if opt=="YES":
                                        print("Your amount has been transferred successfully!")
                                        self.balance = self.balance - amount
                                        print("\nNet Available Balance= Rs.",self.balance)
                                    else:
                                        print("Your request for transferring money has been cancelled")
                    
                                else:
                                    print("Insufficient balance")
                                   
                                
                    if c==4:
                                print('Your current balance is: Rs.',self.balance)
                    if c==5:
                        print("<<FULFIL YOUR DREAMS WITH OUR LOAN PRODUCTS>>")
                        print(" With our personal finance , you can realize your dreams be it transforming your house into your dream house with all desired luxuries,making wedding a memorable event, gearing up with latest gadgets or enjoying holidays with family and friends at your dream detinations!! \n Just apply to our personal finance and repay in easy monthly installments with peace of mind")
                        print("<<FEATURES AND BENEFITS>>")
                        print("*)Easy loan repayment in equal monthly installment \n *)Flexibility to choose repayment period from 1 to 3 years \n *) Loan amount from Rs. 30,000/- to Rs. 3,000,000/- \n *)Interest of 5% per year \n *)No hidden cost ")
                        print("We offer you the following loans: \n 1) Car loan \n 2)Home loan \n 3)Marriage loan ")
                        ch=int(input("Which type of loan do you want?? \n Enter your choice:"))
                        if (ch==1):
                                print("A flexible and hassle-free financing facility that enables you to own your dream car!!")
                                print("If you want to apply for this loan ,Please fill this eligibility form(IN BLOCK LETTERS) ")
                                print("<<<ELIGIBILITY FORM>>>")
                                nationality=input("what is your nationality??\n")
                                if nationality != "PAKISTANI" :
                                    print("Sorry!! you are not eligible for car loan")
                                else:
                                   age=int(input("what is your age??\n"))
                                   if age<21 :
                                        print("Sorry!! you are not eligible for car loan")
                                   else:
                                        bank=input("Are you our 6 or more than 6 months old customer??\n")
                                        if bank !="YES":
                                            print("Sorry!! you are not eligible for car loan")
                                        else:
                                            salary=int(input("What is your monthly income??\n"))
                                            if salary < 40000:
                                                print("Sorry!! you are not eligible for car loan")
                                            else:
                                                dep=int(input("How many dependants you have??\n"))
                                                if dep>6:
                                                    print("Sorry!! you are not eligible for car loan.")
                                                else: 
                                                    print("Congratulations !! You are eligible for this loan. \n Please fill this application form(IN BLOCK LETTERS) \n")
                                                    print("<<<APPLICATION FORM>>>")
                                                    Q=input("Enter your name: ")
                                                    W=input("Enter your CNIC number :")
                                                    A=input("Enter your profession:")
                                                    if (A!="BUSINESSMAN"):
                                                        R=input("Enter your employee type(govt/private) :")
                                                    Y=int(input("Enter your mobile number:"))               
                                                    U=input("Enter your organization name:")
                                                    I=input("Enter your city:")
                                                    O=int(input("Enter your loan amount(from Rs. 30,000/- to Rs. 3,000,000/-):"))
                                                    P=input("Enter your email address:")
                                                    U=input("Enter your address:")
                                                    V=input("Enter your permanent address:")
                                                    E=input("Enter your desired loan repayment period( from 1 to 3 years) :")
                                                   
                                                    
                                                    
                                                    print("\n Please submit the following documents to any branch of our bank.")
                                                    print("1)Last 6 month's bank statement \n 2)Copy of CNIC / Smart card \n 3)2 recent passport size pictures \n 4)Last two month's salay slip or salary certificate, clerly indicating gross and net salary with details of all deductions \n 5)Complete and duly signed APPLICATION FORM with signature verification from branch. ")
                                                    print("THANK YOU !! HAVE  GOOD DAY !!")
                        if (ch==2):
                                            print("A flexible and hassle-free financing facility that enables you to own your dream house!!")
                                            print("If you want to apply for this loan ,Please fill this eligibility form(IN BLOCK LETTERS) ") 
                                            print("<<<ELIGIBILITY FORM>>>")                               
                                            nationality=input("what is your nationality??\n")
                                            if nationality != "PAKISTANI" :
                                                print("Sorry!! you are not eligible for home loan")
                                            else:
                                               age=int(input("what is your age??\n"))
                                               if age<21 :
                                                    print("Sorry!! you are not eligible for home loan")
                                               else:
                                                    bank=input("Are you our 6 or more than 6 months old customer??\n")
                                                    if bank !="YES":
                                                        print("Sorry!! you are not eligible for home loan")
                                                    else:
                                                        salary=int(input("What is your monthly income??\n"))
                                                        if salary < 40000:
                                                            print("Sorry!! you are not eligible for home loan")
                                                        else:
                                                            dep=int(input("How many do dependants you have??\n"))
                                                            if dep>6:
                                                                print("Sorry!! you are not eligible for home loan")
                                                            else: 
                                                                print("Congratulations !! You are eligible for this loan. \n Please fill this application form(IN BLOCK LETTERS) ")
                                                                print("<<<APPLICATION FORM>>>")
                                                                Q=input("Enter your name: ")
                                                                W=input("Enter your CNIC number :")
                                                                A=input("Enter your profession:")
                                                                if (A!="BUSINESSMAN"):
                                                                    R=input("Enter your employee type(govt/private):")
                                                                Y=int(input("Enter your mobile number:"))               
                                                                U=input("Enter your workplace:")
                                                                I=input("Enter your city:")
                                                                O=int(input("Enter your loan amount(from Rs. 30,000/- to Rs. 3,000,000/-):"))
                                                                P=input("Enter your email address:")
                                                                U=input("Enter your address:")
                                                                V=input("Enter your permanent address:")
                                                                E=input("Enter your desired loan repayment period( from 1 to 3 years) :")
                                                                
                                                                
                                                                
                                                                print("Please submit the following documents to any branch of our bank.")
                                                                print("1)Last 6 month's bank statement \n 2)Copy of CNIC / Smart card \n 3)2 recent passport size pictures \n 4)Last two month's salay slip or salary certificate, clearly indicating gross and net salary with details of all deductions \n 5)Complete and duly signed APPLICATION FORM with signature verification from branch.\n 6)Copy of property documents ")
                                                                print("THANK YOU !! HAVE  GOOD DAY !!")
                                    
                                    
                        if (ch==3):
                                        print("A flexible and hassle-free financing facility that heps you in building your future!!")
                                        print("If you want to apply for this loan ,Please fill this eiligibility form(IN BLOCK LETTERS) ")
                                        print("<<<ELIGIBILITY FORM>>>")
                                        nationality=input("what is your nationality??\n")
                                        if nationality != "PAKISTANI" :
                                            print("Sorry!! you are not eligible for car loan")
                                        else:
                                            age=int(input("what is your age??\n"))
                                            if age<21 :
                                                 print("Sorry!! you are not eligible for home loan")
                                            else:
                                                 bank=input("Are you our 6 or more than 6 months old customer??\n")
                                                 if bank !="YES":
                                                     print("Sorry!! you are not eligible for home loan")
                                                 else:
                                                     salary=int(input("What is your monthly income??\n"))
                                                     if salary < 40000:
                                                         print("Sorry!! you are not eligible for home loan")
                                                     else:
                                                         dep=int(input("How many dependants do you have??\n"))
                                                         if dep>6:
                                                             print("Sorry!! you are not eligible for home loan")
                                                         else: 
                                                             print("Congratulations !! You are eligible for this loan. \n Please fill this application form(IN BLOCK LETTERS) ")
                                                             print("<<<APPLICATION FORM>>>")
                                                             Q=input("Enter your name: ")
                                                             W=input("Enter your CNIC number :")
                                                             A=input("Enter your profession:")
                                                             if (A!="BUSINESSMAN"):
                                                                 R=input("Enter your employee type(govt/private):")
                                                             Y=int(input("Enter your mobile number:"))               
                                                             U=input("Enter your workplace:")
                                                             I=input("Enter your city:")
                                                             O=int(input("Enter your loan amount(from Rs. 30,000/- to Rs. 3,000,000/-):"))
                                                             P=input("Enter your email address:")
                                                             U=input("Enter your address:")
                                                             V=input("Enter your permanent address:")
                                                             E=input("Enter your desired loan repayment period( from 1 to 3 years) :")
                                                             
                                                             
                                                             
                                                             print("Please submit the following documents to any branch of our bank.")
                                                             print("1)Last 6 month's bank statement \n 2)Copy of CNIC / Smart card \n 3)2 recent passport size pictures \n 4)Last two month's salay slip or salary certificate, clearly indicating gross and net salary with details of all deductions \n 5)Complete and duly signed APPLICATION FORM with signature verification from branch.\n 6)Copy of property documents ")
                                                             print("THANK YOU !! HAVE  GOOD DAY !!")
      
                    if c==6:
                        print("Your account has been logged out.")
                        break
                        
                    else:
                        print("Invalid choice")
            elif a=="3311455592" and b=="ALISHBAH AHMED" and p=="*****":
                print("You have logged into your account!!")
                while True:
                    
                    self.balance=1500
                    print("What do you want to do??")
                    c=int(input("1)Deposit money \n2)Withdraw money \n3)Transfer money \n4)Check your current balance \n5)Apply for loan \n6)Logout\nEnter your choice:"))
                    if c==1:
                                self.amount=float(input("Enter amount to be Deposit: "))
                                self.balance += self.amount
                                opt=input("Are you sure to want to deposit money??")
                                if opt=="YES":
                                    print("Your amount has been deposited successfully")
                                    print("\n Net Available Balance:Rs",self.balance) 
                                    
                                else:
                                    print("Your request for depositing money has been cancelled!")
                    if c==2:
                                amount = float(input("Enter amount to be Withdrawn: "))
                                if amount>=50000:
                                    print("You cannot withdraw money more than 50,000Rs at a time!!")
                                else:
                                    if self.balance>=amount:
                                        self.balance-=amount
                                        opt=input("Are you sure to want to withdraw money??")
                                        if opt=="YES":
                                            print("Your amount has been withdrawn successfully")
                                            print("\n Net Available Balance:Rs",self.balance)  
                                        else:
                                            print("Your request for money withdrawn has been cancelled!")
                                        
                                    else:
                                        print("\n Insufficient balance  ")
                                print("\n Net Available Balance=",self.balance)
                                
                    if c==3:
                                amount = float(input("Enter amount to be transfer:Rs "))
                                if self.balance>=amount:
                                    int(input("Enter the recievers account number:"))
                                    int(input("Enter the receiver's bank branch code:"))
                                    opt=input("Are you sure to want to transfer money??")
                                    if opt=="YES":
                                        print("Your amount has been transferred successfully!")
                                        self.balance = self.balance - amount
                                        print("\nNet Available Balance= Rs.",self.balance)
                                    else:
                                        print("Your request for transferring money has been cancelled")
                    
                                else:
                                    print("Insufficient balance")
                                   
                                
                    if c==4:
                                print('Your current balance is: Rs.',self.balance)
                    if c==5:
                        print("<<FULFIL YOUR DREAMS WITH OUR LOAN PRODUCTS>>")
                        print(" With our personal finance , you can realize your dreams be it transforming your house into your dream house with all desired luxuries,making wedding a memorable event, gearing up with latest gadgets or enjoying holidays with family and friends at your dream detinations!! \n Just apply to our personal finance and repay in easy monthly installments with peace of mind")
                        print("<<FEATURES AND BENEFITS>>")
                        print("*)Easy loan repayment in equal monthly installment \n *)Flexibility to choose repayment period from 1 to 3 years \n *) Loan amount from Rs. 30,000/- to Rs. 3,000,000/- \n *)Interest of 5% per year \n *)No hidden cost ")
                        print("We offer you the following loans: \n 1) Car loan \n 2)Home loan \n 3)Marriage loan ")
                        ch=int(input("Which type of loan do you want?? \n Enter your choice:"))
                        if (ch==1):
                                print("A flexible and hassle-free financing facility that enables you to own your dream car!!")
                                print("If you want to apply for this loan ,Please fill this eligibility form(IN BLOCK LETTERS) ")
                                print("<<<ELIGIBILITY FORM>>>")
                                nationality=input("what is your nationality??\n")
                                if nationality != "PAKISTANI" :
                                    print("Sorry!! you are not eligible for car loan")
                                else:
                                   age=int(input("what is your age??\n"))
                                   if age<21 :
                                        print("Sorry!! you are not eligible for car loan")
                                   else:
                                        bank=input("Are you our 6 or more than 6 months old customer??\n")
                                        if bank !="YES":
                                            print("Sorry!! you are not eligible for car loan")
                                        else:
                                            salary=int(input("What is your monthly income??\n"))
                                            if salary < 40000:
                                                print("Sorry!! you are not eligible for car loan")
                                            else:
                                                dep=int(input("How many dependants you have??\n"))
                                                if dep>6:
                                                    print("Sorry!! you are not eligible for car loan.")
                                                else: 
                                                    print("Congratulations !! You are eligible for this loan. \n Please fill this application form(IN BLOCK LETTERS) \n")
                                                    print("<<<APPLICATION FORM>>>")
                                                    Q=input("Enter your name: ")
                                                    W=input("Enter your CNIC number :")
                                                    A=input("Enter your profession:")
                                                    if (A!="BUSINESSMAN"):
                                                        R=input("Enter your employee type(govt/private) :")
                                                    Y=int(input("Enter your mobile number:"))               
                                                    U=input("Enter your organization name:")
                                                    I=input("Enter your city:")
                                                    O=int(input("Enter your loan amount(from Rs. 30,000/- to Rs. 3,000,000/-):"))
                                                    P=input("Enter your email address:")
                                                    U=input("Enter your address:")
                                                    V=input("Enter your permanent address:")
                                                    E=input("Enter your desired loan repayment period( from 1 to 3 years) :")
                                                   
                                                    
                                                    
                                                    print("\n Please submit the following documents to any branch of our bank.")
                                                    print("1)Last 6 month's bank statement \n 2)Copy of CNIC / Smart card \n 3)2 recent passport size pictures \n 4)Last two month's salay slip or salary certificate, clerly indicating gross and net salary with details of all deductions \n 5)Complete and duly signed APPLICATION FORM with signature verification from branch. ")
                                                    print("THANK YOU !! HAVE  GOOD DAY !!")
                        if (ch==2):
                                            print("A flexible and hassle-free financing facility that enables you to own your dream house!!")
                                            print("If you want to apply for this loan ,Please fill this eligibility form(IN BLOCK LETTERS) ") 
                                            print("<<<ELIGIBILITY FORM>>>")                               
                                            nationality=input("what is your nationality??\n")
                                            if nationality != "PAKISTANI" :
                                                print("Sorry!! you are not eligible for home loan")
                                            else:
                                               age=int(input("what is your age??\n"))
                                               if age<21 :
                                                    print("Sorry!! you are not eligible for home loan")
                                               else:
                                                    bank=input("Are you our 6 or more than 6 months old customer??\n")
                                                    if bank !="YES":
                                                        print("Sorry!! you are not eligible for home loan")
                                                    else:
                                                        salary=int(input("What is your monthly income??\n"))
                                                        if salary < 40000:
                                                            print("Sorry!! you are not eligible for home loan")
                                                        else:
                                                            dep=int(input("How many do dependants you have??\n"))
                                                            if dep>6:
                                                                print("Sorry!! you are not eligible for home loan")
                                                            else: 
                                                                print("Congratulations !! You are eligible for this loan. \n Please fill this application form(IN BLOCK LETTERS) ")
                                                                print("<<<APPLICATION FORM>>>")
                                                                Q=input("Enter your name: ")
                                                                W=input("Enter your CNIC number :")
                                                                A=input("Enter your profession:")
                                                                if (A!="BUSINESSMAN"):
                                                                    R=input("Enter your employee type(govt/private):")
                                                                Y=int(input("Enter your mobile number:"))               
                                                                U=input("Enter your workplace:")
                                                                I=input("Enter your city:")
                                                                O=int(input("Enter your loan amount(from Rs. 30,000/- to Rs. 3,000,000/-):"))
                                                                P=input("Enter your email address:")
                                                                U=input("Enter your address:")
                                                                V=input("Enter your permanent address:")
                                                                E=input("Enter your desired loan repayment period( from 1 to 3 years) :")
                                                                
                                                                
                                                                
                                                                print("Please submit the following documents to any branch of our bank.")
                                                                print("1)Last 6 month's bank statement \n 2)Copy of CNIC / Smart card \n 3)2 recent passport size pictures \n 4)Last two month's salay slip or salary certificate, clearly indicating gross and net salary with details of all deductions \n 5)Complete and duly signed APPLICATION FORM with signature verification from branch.\n 6)Copy of property documents ")
                                                                print("THANK YOU !! HAVE  GOOD DAY !!")
                                    
                                    
                        if (ch==3):
                                        print("A flexible and hassle-free financing facility that heps you in building your future!!")
                                        print("If you want to apply for this loan ,Please fill this eiligibility form(IN BLOCK LETTERS) ")
                                        print("<<<ELIGIBILITY FORM>>>")
                                        nationality=input("what is your nationality??\n")
                                        if nationality != "PAKISTANI" :
                                            print("Sorry!! you are not eligible for car loan")
                                        else:
                                            age=int(input("what is your age??\n"))
                                            if age<21 :
                                                 print("Sorry!! you are not eligible for home loan")
                                            else:
                                                 bank=input("Are you our 6 or more than 6 months old customer??\n")
                                                 if bank !="YES":
                                                     print("Sorry!! you are not eligible for home loan")
                                                 else:
                                                     salary=int(input("What is your monthly income??\n"))
                                                     if salary < 40000:
                                                         print("Sorry!! you are not eligible for home loan")
                                                     else:
                                                         dep=int(input("How many dependants do you have??\n"))
                                                         if dep>6:
                                                             print("Sorry!! you are not eligible for home loan")
                                                         else: 
                                                             print("Congratulations !! You are eligible for this loan. \n Please fill this application form(IN BLOCK LETTERS) ")
                                                             print("<<<APPLICATION FORM>>>")
                                                             Q=input("Enter your name: ")
                                                             W=input("Enter your CNIC number :")
                                                             A=input("Enter your profession:")
                                                             if (A!="BUSINESSMAN"):
                                                                 R=input("Enter your employee type(govt/private):")
                                                             Y=int(input("Enter your mobile number:"))               
                                                             U=input("Enter your workplace:")
                                                             I=input("Enter your city:")
                                                             O=int(input("Enter your loan amount(from Rs. 30,000/- to Rs. 3,000,000/-):"))
                                                             P=input("Enter your email address:")
                                                             U=input("Enter your address:")
                                                             V=input("Enter your permanent address:")
                                                             E=input("Enter your desired loan repayment period( from 1 to 3 years) :")
                                                             
                                                             
                                                             
                                                             print("Please submit the following documents to any branch of our bank.")
                                                             print("1)Last 6 month's bank statement \n 2)Copy of CNIC / Smart card \n 3)2 recent passport size pictures \n 4)Last two month's salay slip or salary certificate, clearly indicating gross and net salary with details of all deductions \n 5)Complete and duly signed APPLICATION FORM with signature verification from branch.\n 6)Copy of property documents ")
                                                             print("THANK YOU !! HAVE  GOOD DAY !!")
      
                    if c==6:
                        break
                        print("Your account has been logged out.")
                    else:
                        print("Invalid choice")
            elif a=="3029222959" and b=="AQSA SHAHID" and p=="*****":
                print("You have logged into your account!!")
                while True:
                    
                    self.balance=3500
                    print("What do you want to do??")
                    c=int(input("1)Deposit money \n2)Withdraw money \n3)Transfer money \n4)Check your current balance \n5)Apply for loan \n6)Logout\nEnter your choice:"))
                    if c==1:
                                self.amount=float(input("Enter amount to be Deposited: "))
                                self.balance += self.amount
                                opt=input("Are you sure to want to deposit money??")
                                if opt=="YES":
                                    print("Your amount has been deposited successfully")
                                    print("\n Net Available Balance:Rs",self.balance) 
                                    
                                else:
                                    print("Your request for depositing money has been cancelled!")
                    if c==2:
                                amount = float(input("Enter amount to be Withdrawn: "))
                                if amount>=50000:
                                    print("You cannot withdraw money more than 50,000Rs at a time!!")
                                else:
                                    if self.balance>=amount:
                                        self.balance-=amount
                                        opt=input("Are you sure to want to withdraw money??")
                                        if opt=="YES":
                                            print("Your amount has been withdrawn successfully")
                                            print("\n Net Available Balance:Rs",self.balance)  
                                        else:
                                            print("Your request for money withdrawn has been cancelled!")
                                        
                                    else:
                                        print("\n Insufficient balance  ")
                                print("\n Net Available Balance=",self.balance)
                                
                    if c==3:
                                amount = float(input("Enter amount to be transfer:Rs "))
                                if self.balance>=amount:
                                    int(input("Enter the recievers account number:"))
                                    int(input("Enter the receiver's bank branch code:"))
                                    opt=input("Are you sure to want to transfer money??")
                                    if opt=="YES":
                                        print("Your amount has been transferred successfully!")
                                        self.balance = self.balance - amount
                                        print("\nNet Available Balance= Rs.",self.balance)
                                    else:
                                        print("Your request for transferring money has been cancelled")
                    
                                else:
                                    print("Insufficient balance")
                                   
                                
                    if c==4:
                                print('Your current balance is: Rs.',self.balance)
                    if c==5:
                        print("<<FULFIL YOUR DREAMS WITH OUR LOAN PRODUCTS>>")
                        print(" With our personal finance , you can realize your dreams be it transforming your house into your dream house with all desired luxuries,making wedding a memorable event, gearing up with latest gadgets or enjoying holidays with family and friends at your dream detinations!! \n Just apply to our personal finance and repay in easy monthly installments with peace of mind")
                        print("<<FEATURES AND BENEFITS>>")
                        print("*)Easy loan repayment in equal monthly installment \n *)Flexibility to choose repayment period from 1 to 3 years \n *) Loan amount from Rs. 30,000/- to Rs. 3,000,000/- \n *)Interest of 5% per year \n *)No hidden cost ")
                        print("We offer you the following loans: \n 1) Car loan \n 2)Home loan \n 3)Marriage loan ")
                        ch=int(input("Which type of loan do you want?? \n Enter your choice:"))
                        if (ch==1):
                                print("A flexible and hassle-free financing facility that enables you to own your dream car!!")
                                print("If you want to apply for this loan ,Please fill this eligibility form(IN BLOCK LETTERS) ")
                                print("<<<ELIGIBILITY FORM>>>")
                                nationality=input("what is your nationality??\n")
                                if nationality != "PAKISTANI" :
                                    print("Sorry!! you are not eligible for car loan")
                                else:
                                   age=int(input("what is your age??\n"))
                                   if age<21 :
                                        print("Sorry!! you are not eligible for car loan")
                                   else:
                                        bank=input("Are you our 6 or more than 6 months old customer??\n")
                                        if bank !="YES":
                                            print("Sorry!! you are not eligible for car loan")
                                        else:
                                            salary=int(input("What is your monthly income??\n"))
                                            if salary < 40000:
                                                print("Sorry!! you are not eligible for car loan")
                                            else:
                                                dep=int(input("How many dependants you have??\n"))
                                                if dep>6:
                                                    print("Sorry!! you are not eligible for car loan.")
                                                else: 
                                                    print("Congratulations !! You are eligible for this loan. \n Please fill this application form(IN BLOCK LETTERS) \n")
                                                    print("<<<APPLICATION FORM>>>")
                                                    Q=input("Enter your name: ")
                                                    W=input("Enter your CNIC number :")
                                                    A=input("Enter your profession:")
                                                    if (A!="BUSINESSMAN"):
                                                        R=input("Enter your employee type(govt/private) :")
                                                    Y=int(input("Enter your mobile number:"))               
                                                    U=input("Enter your organization name:")
                                                    I=input("Enter your city:")
                                                    O=int(input("Enter your loan amount(from Rs. 30,000/- to Rs. 3,000,000/-):"))
                                                    P=input("Enter your email address:")
                                                    U=input("Enter your address:")
                                                    V=input("Enter your permanent address:")
                                                    E=input("Enter your desired loan repayment period( from 1 to 3 years) :")
                                                   
                                                    
                                                    
                                                    print("\n Please submit the following documents to any branch of our bank.")
                                                    print("1)Last 6 month's bank statement \n 2)Copy of CNIC / Smart card \n 3)2 recent passport size pictures \n 4)Last two month's salay slip or salary certificate, clerly indicating gross and net salary with details of all deductions \n 5)Complete and duly signed APPLICATION FORM with signature verification from branch. ")
                                                    print("THANK YOU !! HAVE  GOOD DAY !!")
                        if (ch==2):
                                            print("A flexible and hassle-free financing facility that enables you to own your dream house!!")
                                            print("If you want to apply for this loan ,Please fill this eligibility form(IN BLOCK LETTERS) ") 
                                            print("<<<ELIGIBILITY FORM>>>")                               
                                            nationality=input("what is your nationality??\n")
                                            if nationality != "PAKISTANI" :
                                                print("Sorry!! you are not eligible for home loan")
                                            else:
                                               age=int(input("what is your age??\n"))
                                               if age<21 :
                                                    print("Sorry!! you are not eligible for home loan")
                                               else:
                                                    bank=input("Are you our 6 or more than 6 months old customer??\n")
                                                    if bank !="YES":
                                                        print("Sorry!! you are not eligible for home loan")
                                                    else:
                                                        salary=int(input("What is your monthly income??\n"))
                                                        if salary < 40000:
                                                            print("Sorry!! you are not eligible for home loan")
                                                        else:
                                                            dep=int(input("How many do dependants you have??\n"))
                                                            if dep>6:
                                                                print("Sorry!! you are not eligible for home loan")
                                                            else: 
                                                                print("Congratulations !! You are eligible for this loan. \n Please fill this application form(IN BLOCK LETTERS) ")
                                                                print("<<<APPLICATION FORM>>>")
                                                                Q=input("Enter your name: ")
                                                                W=input("Enter your CNIC number :")
                                                                A=input("Enter your profession:")
                                                                if (A!="BUSINESSMAN"):
                                                                    R=input("Enter your employee type(govt/private):")
                                                                Y=int(input("Enter your mobile number:"))               
                                                                U=input("Enter your workplace:")
                                                                I=input("Enter your city:")
                                                                O=int(input("Enter your loan amount(from Rs. 30,000/- to Rs. 3,000,000/-):"))
                                                                P=input("Enter your email address:")
                                                                U=input("Enter your address:")
                                                                V=input("Enter your permanent address:")
                                                                E=input("Enter your desired loan repayment period( from 1 to 3 years) :")
                                                                
                                                                
                                                                
                                                                print("Please submit the following documents to any branch of our bank.")
                                                                print("1)Last 6 month's bank statement \n 2)Copy of CNIC / Smart card \n 3)2 recent passport size pictures \n 4)Last two month's salay slip or salary certificate, clearly indicating gross and net salary with details of all deductions \n 5)Complete and duly signed APPLICATION FORM with signature verification from branch.\n 6)Copy of property documents ")
                                                                print("THANK YOU !! HAVE  GOOD DAY !!")
                                    
                                    
                        if (ch==3):
                                        print("A flexible and hassle-free financing facility that heps you in building your future!!")
                                        print("If you want to apply for this loan ,Please fill this eiligibility form(IN BLOCK LETTERS) ")
                                        print("<<<ELIGIBILITY FORM>>>")
                                        nationality=input("what is your nationality??\n")
                                        if nationality != "PAKISTANI" :
                                            print("Sorry!! you are not eligible for car loan")
                                        else:
                                            age=int(input("what is your age??\n"))
                                            if age<21 :
                                                 print("Sorry!! you are not eligible for home loan")
                                            else:
                                                 bank=input("Are you our 6 or more than 6 months old customer??\n")
                                                 if bank !="YES":
                                                     print("Sorry!! you are not eligible for home loan")
                                                 else:
                                                     salary=int(input("What is your monthly income??\n"))
                                                     if salary < 40000:
                                                         print("Sorry!! you are not eligible for home loan")
                                                     else:
                                                         dep=int(input("How many dependants do you have??\n"))
                                                         if dep>6:
                                                             print("Sorry!! you are not eligible for home loan")
                                                         else: 
                                                             print("Congratulations !! You are eligible for this loan. \n Please fill this application form(IN BLOCK LETTERS) ")
                                                             print("<<<APPLICATION FORM>>>")
                                                             Q=input("Enter your name: ")
                                                             W=input("Enter your CNIC number :")
                                                             A=input("Enter your profession:")
                                                             if (A!="BUSINESSMAN"):
                                                                 R=input("Enter your employee type(govt/private):")
                                                             Y=int(input("Enter your mobile number:"))               
                                                             U=input("Enter your workplace:")
                                                             I=input("Enter your city:")
                                                             O=int(input("Enter your loan amount(from Rs. 30,000/- to Rs. 3,000,000/-):"))
                                                             P=input("Enter your email address:")
                                                             U=input("Enter your address:")
                                                             V=input("Enter your permanent address:")
                                                             E=input("Enter your desired loan repayment period( from 1 to 3 years) :")
                                                             
                                                             
                                                             
                                                             print("Please submit the following documents to any branch of our bank.")
                                                             print("1)Last 6 month's bank statement \n 2)Copy of CNIC / Smart card \n 3)2 recent passport size pictures \n 4)Last two month's salay slip or salary certificate, clearly indicating gross and net salary with details of all deductions \n 5)Complete and duly signed APPLICATION FORM with signature verification from branch.\n 6)Copy of property documents ")
                                                             print("THANK YOU !! HAVE  GOOD DAY !!")
      
                    else:
                        print("Your account has been logged out.")
                        break
                    
                        
            else:
                    print("The Account number and Title you have entered does not exist")
            
        #Delete account
        if(choice==3):
            
                
                print("Please fill this account closure form in order to close/delete your account")
                print("<<<CLOSURE FORM>>>")
                print("NOTE:PLEASE FILL THIS FORM IN BLOCK LETTERS")
                Date=input("Enter the date:")
                branchcode=int(input("Enter the branch code:"))
                branchname=input("Enter name of branch at which you have open an account:")
                print("\n<ACCOUNT DETAILS FOR CLOSURE>\n")
                ACCOUNTNAME=input("Enter account name:")
                ACCOUNTNUMBER=input("Enter account number:")
                print("\n<REQUEST DETAILS>\n")
                R=input("Reason of closing account:")
                
                w=input("Are you sure to want to delete your account??\n")
                if (w=="YES"):
                    print("\n<ACCOUNT CLOSURE INSTRUCTION>\n")
                    print("As you have requested for closing your account so the amount that you have in your account will be returned to you after account closure.")
                    v=int(input("How do you want your amount??\n 1)Through cash\n2)Through debit card \nEnter your choice:"))
                    if (v==1):    
                        print("Your account has been closed and your balance amount has been given to you as cash")
                    elif (v==2):
                        a=int(input("Enter your Debit card number:"))
                        print("Your request for account closure is being proceed, You will be notified by the mail. ")
                        print("THANK YOU!!")
                    else:
                        print("Invalid choice ")
                elif(w=="NO"):
                    print("You has denied your account closure request")
                    print("THANK YOU !! ")
                else:
                    print("Invalid choice")
        
obj=bankaccount()
obj.account()              
            
               
        
                    
                    

          

  