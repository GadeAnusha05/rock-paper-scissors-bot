import random

def get_computer_choice(player_choice):
    # 70% random, 30% tries to beat the player
    if random.random() < 0.3:
        if player_choice == 'r':
            return 'p'  # paper beats rock
        elif player_choice == 'p':
            return 's'  # scissors beat paper
        elif player_choice == 's':
            return 'r'  # rock beats scissors
    return random.choice(['r', 'p', 's'])

def determine_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == 'r' and computer == 's') or \
         (player == 'p' and computer == 'r') or \
         (player == 's' and computer == 'p'):
        return "player"
    else:
        return "computer"

def play_game():
    rounds = int(input("Number of rounds: "))
    player_score, computer_score = 0, 0
    options = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

    for _ in range(rounds):
        player = input("rock(r), paper(p), scissors(s): ").lower()
        if player not in options:
            print("❌ Invalid choice, try again!")
            continue

        computer = get_computer_choice(player)
        print(f"{options[player]} vs {options[computer]}")

        winner = determine_winner(player, computer)
        if winner == "player":
            print("✅ You win this round!")
            player_score += 1
        elif winner == "computer":
            print("🤖 Computer wins this round!")
            computer_score += 1
        else:
            print("⚖️ It's a draw!")

        print(f"Score → You: {player_score} | Computer: {computer_score}\n")

    print("===== Final Result =====")
    if player_score > computer_score:
        print("🎉 Congrats, you WON the game!")
    elif player_score < computer_score:
        print("😢 You lost to the computer...")
    else:
        print("⚖️ It's an overall DRAW!")

if __name__ == "__main__":
    play_game()
