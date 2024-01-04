import random

# Колода карт
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Очки для карт
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
               '7': 7, '8': 8, '9': 9, '10': 10,
               'J': 10, 'Q': 10, 'K': 10, 'A': 1}

# Очки игрока и дилера
player_points = 0
dealer_points = 0

# Карты игрока и дилера
player_cards = []
dealer_cards = []

# Функция для суммирования очков
def count_points(cards):
    points = 0
    ace = False
    for card in cards:
        points += card_values[card]
        if card == 'A':
            ace = True
    if ace and points <= 11:
        points += 10
    return points

# Функция для начала игры
def start_game():
    global player_points, dealer_points, player_cards, dealer_cards
    print('Добро пожаловать в игру блэкджек!')
    # Раздача карт игроку и дилеру
    player_cards = [cards[random.randint(0, len(cards)-1)],
                    cards[random.randint(0, len(cards)-1)]]
    dealer_cards = [cards[random.randint(0, len(cards)-1)],
                    cards[random.randint(0, len(cards)-1)]]
    # Считаем очки игрока и дилера
    player_points = count_points(player_cards)
    dealer_points = count_points(dealer_cards)
    # Выводим карты игрока и одну карту дилера
    print('Ваши карты:', player_cards)
    print('Карта дилера:', dealer_cards[0])
    # Проверяем на наличие блэкджека у игрока
    if player_points == 21:
        print('У вас блэкджек! Вы победили.')
        return
    # Проверяем на наличие блэкджека у дилера
    if dealer_points == 21:
        print('У дилера блэкджек! Вы проиграли.')
        return
    # Запускаем игру
    game()

# Функция для игры
def game():
    global player_points, dealer_points, player_cards, dealer_cards
    # Ход игрока
    while player_points < 21:
        choice = input('Хотите взять ещё карту? (Y/N): ')
        if choice == 'Y':
            player_cards.append(cards[random.randint(0, len(cards)-1)])
            player_points = count_points(player_cards)
            print('Ваши карты:', player_cards)
            print('Количество очков:', player_points)
        else:
            break
    if player_points > 21:
        print('Перебор! Вы проиграли.')
        return
    # Ход дилера
    while dealer_points < 17:
        dealer_cards.append(cards[random.randint(0, len(cards)-1)])
        dealer_points = count_points(dealer_cards)
    print('Карты дилера:', dealer_cards)
    print('Количество очков дилера:', dealer_points)
    # Определение победителя
    if dealer_points > 21:
        print('Дилер перебрал! Вы победили.')
        return
    elif dealer_points > player_points:
        print('Вы проиграли.')
        return
    elif dealer_points < player_points:
        print('Вы победили.')
        return
    else:
        print('Ничья.')
        return
start_game()