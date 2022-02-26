from local_scanner import localscan
from scout_runner import scoutrun

choice=input('''Select the environment you want to scan:    1> local(write 1) 
                                            2> cloud(write 2)  ''')

if choice == '1':
    localscan()
elif choice == '2':
    scoutrun()   
else:
    print('please enter valid choice')     
