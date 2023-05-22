import ipdb

katz_deli = []

def line(katz_deli): 
    if len(katz_deli) == 0:
        print('The line is currently empty.')
    else: 
        line = []
        for i in range(len(katz_deli)):
            line.append(f'{i+1}. {katz_deli[i]}')
        print('The line is currently: ' + ' '.join(line))
    
def take_a_number(katz_deli, person):
    katz_deli.append(person)
    print(f'Welcome, {katz_deli[-1]}. You are number {len(katz_deli)} in line.')

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print('There is nobody waiting to be served!')
    else:
        print(f'Currently serving {katz_deli[0]}.')
        katz_deli.pop(0)