# Whos the Boss

def FindBoss(n, names):
    # Write your code here
    # Lists for managers and employers
    managers = []
    employers = []
    # Append items
    for manager, employer in names:
        managers.append(manager)
        employers.append(employer)
    # Find manager not in employers list
    for i in managers:
        if i not in employers:
            print(i)
        

        
        
                
n = 10
names = [['Merill', 'Town'], ['Ardine', 'Elvis'], ['Jania', 'Othelia'], ['Town', 'Ardine'], ['Victor', 'Thaddius'], ['Merill', 'Victor'], ['Victor', 'Jania'], ['Ardine', 'Gwen'], ['Victor', 'Adolfo'], ['Victor', 'Menard']]
FindBoss(n,names)