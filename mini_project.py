import random

# Constantes que definem os limites do jogo
MAX_LINES = 3  # Número máximo de linhas que podem ser apostadas
MAX_BET = 100  # Valor máximo que pode ser apostado
MIN_BET = 1    # Valor mínimo que pode ser apostado

ROWS = 3  # Número de linhas no slot machine
COLS = 3  # Número de colunas no slot machine

# Dicionário que define a quantidade de cada símbolo no slot machine
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# Dicionário que define o valor de cada símbolo
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Função para verificar os ganhos com base nos símbolos alinhados
def check_winnings(columns, lines, bet, values):
    winnings = 0  # Total de ganhos
    winning_lines = []  # Linhas que resultaram em ganhos
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
            
    return winnings, winning_lines    

# Função para simular uma rodada no slot machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns

# Função para exibir o slot machine no console
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" - ")
            else:
                print(column[row], end="")
                
        print()

# Função para solicitar o depósito inicial do jogador
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

# Função para solicitar o número de linhas que o jogador deseja apostar
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

# Função para solicitar o valor da aposta
def get_bet():
    while True:
        amount = input("What would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

# Função principal que executa uma rodada do slot machine
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough money to bet. Your current balance is ${balance}")
        else:
            break
    print(f"You're betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print("You won on lines:", winning_lines)
    return winnings - total_bet
    
# Função principal que gerencia o jogo
def main():
    balance = deposit()
    while True:
        print("Current balance:", balance)
        answer = input("Press enter to spin again. (Or Q to quit)")
        if answer == "Q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

# Inicia o jogo
main()