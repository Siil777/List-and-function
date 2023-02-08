from module1 import*

#palgad=read_file('Palgad_file.txt')
#print(palgad)

#inimised=read_file('inimised_file.txt')
#print(inimised)


while True:
    print(f'-----------------------------------------------------------------------------------------------')
    print(f'\n0 read from file\n1 input workers and birthday,\n2 save to file.\n3 youngest workers,\n4 average year of birth,\n5 year worker\n6 show pensioners,\n7 show younger or older then certain year\n8 delete\n9 exit')
    v=input('>>:')
    if v=='0':
        workers=[]
        birthday=[]
        # empty lists
        workers=read_file('workers_file.txt')
        birthday=read_file('birthday_file.txt')
        

        zipped=list(zip(workers,birthday))
        
        print(workers)
        print(birthday)
        
  

    elif v=='1':
        workers,birthday=write_workers_to_file(workers,birthday)
        print(birthday)
        print(workers)

    elif v=='2':
        save_to_file(workers,'workers_file.txt')
        save_to_file(birthday,'birthday_file.txt')
        

    elif v=='3': 
        youngest_workers(zipped)
    elif v=='4': 
        average_age(workers, birthday)
    elif v=='5': 
        year_worker(birthday,workers)
    elif v=='6':
        pensioner(zipped)
    elif v=='7':
        choice=input("would you like to know who older to whom? (1 younger 2 older)")
        amount=input("input year for comparing: ")
        lower_or_bigger(choice,amount,zipped)
    elif v=='8': 
        birthday,workers=delete_worker(input('name:'),birthday,workers)  
        print(workers) 
        print(birthday) 

    elif v=='9':
        break
