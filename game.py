import random

MAX_LINES = 3
MAX_BET = 10000
MIN_BET = 100 

R = 3
CL = 3

symbol_dict = {
    "A": 1,
    "B": 2,
    "C": 2,
    "D": 4
}

symbol_V = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_w(columns, lines, bet , values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            
            symbol_check = column[line]
            if symbol != symbol_check: 
                break
            
            else:
                winnings += values[symbol] * bet
               
                winning_lines.append(lines + 1)

    return winnings, winning_lines

def machine_spin(r,c,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []   
    for _ in range(c):
        column = []
        current_symbols = all_symbols[:]
        for _ in range (r):   
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
                if i != len(columns) -1:
                    print(column[row], end=" | ")
                else:
                    print( column[row], end="")
        print()

def deposit():
    while True:
        amount = input("How much would you like to deposit? £")
        if amount.isdigit():
            amount = int(amount) 
            if amount >=100: 
               
                break
            else:
                print("To play you must at least deposit £100")
        else:
            print("Please enter a number.")
    return amount

def line_numbers ():
    while True:
        line = input("Enter the number of line to bet on (1-" + str(MAX_LINES) + ")? ") 
        if line.isdigit():
            line = int(line)
            if 1 <= line <= MAX_LINES:
                break
            else:
                print('Enter a valid number of line to bet on.')     
        else:
            print('Please enter a number.')
    return line

def bet_():
    while True:
        bet = input("How much would you like to bet ? £") 
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            elif MIN_BET > bet:
                print('You have to bet at least £100 to take part.')
            elif bet > MAX_BET:
                print("You can't bet more than £10000.")
        else:
            print('Please enter a number.')
    return bet


def game(balance):
    line = line_numbers()
    while True:
        bet = bet_()
        total_bet= bet * int(line) 

        if total_bet > balance:
            print(f"Your total bet is £{total_bet}, you don't have that amount of money. Your current deposit is £{balance}. Please lower the amount of money to bet on.")

        else:
            break
    print(f"You're betting £{bet} on {line} lines. Total bet is equal to: £{total_bet}")
    print(f'Deposited amount: £{balance} | Line/s bet on: {line} | Total bet: £{total_bet}')

    slots = machine_spin(R,CL,symbol_dict)
    print_machine(slots)
    winnings, winning_lines = check_w(slots, line, bet, symbol_V)
    print(f"You won £{winnings}!")
    print(f"You won on lines:", *winning_lines) 
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is £ {balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += game(balance)
    print(f"You're left with £{balance}")

main()