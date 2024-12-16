import random
MAX_LINE  = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbol_value = {
    "A":5,
    "B":4,
    "C":2,
    "D":2
}
def check_winning(columns, lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings +=values[symbol]*bet
            winning_lines.append(line+1)
    return winnings , winning_lines

def get_slot_machine_spin(rows, cols , symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        Current_symbol = all_symbols[:]
        for row in range(rows):
            value = random.choice(Current_symbol )
            Current_symbol.remove(value)
            column.append(value)
        
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        
        print()

def deposit():
    while True:
        amount = input("What do you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater then 0.")
        else:
            print("Please enter a number.")
    return amount
def get_number_of_line():
    while True:
        line = input("Enter the number of line to bet on (1-"+ str(MAX_LINE)+")? ")
        if line.isdigit():
            line = int(line)
            if 1<= line <= MAX_LINE:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return line

def get_bet():
    while True:
        amount = input("What would do you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<= amount <= MAX_BET:
                break
            else:
                amount = input(f"What would you like to bet on each line? (${MIN_BET} - ${MAX_BET}): $")
        else:
            print("Please enter a number.")
    return amount

def spin(balance):
    lines = get_number_of_line()
    while True:      
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is ${balance}.")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}")
    
    # Get the spin result
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    
    # Check winnings
    winnings, winning_lines = check_winning(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ", *winning_lines)
    
    # Return net winnings (positive or negative)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press Enter to play (q to quit): ")
        if answer.lower() == "q":
            break
        balance += spin(balance)
    
    print(f"You left with ${balance}")

main()