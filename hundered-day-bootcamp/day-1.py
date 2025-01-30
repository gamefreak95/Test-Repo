import random

def generate_matchups(players, num_games):
    """
    Generate matchups for games such that no player faces more than one power-up from an opponent
    and no player plays against the same opponent in multiple games.

    Args:
        players (list): List of player names.
        num_games (int): Number of games to be played.

    Returns:
        list: A list of matches for each game.
    """
    if len(players) % 2 != 0:
        raise ValueError("Number of players must be even for pairings.")

    matches = []
    power_up_users = []
    used_pairs = set()

    for game in range(1, num_games + 1):
        # Select two unique players to use power-ups for this game
        available_for_power_ups = [p for p in players if p not in power_up_users]
        if len(available_for_power_ups) < 2:
            power_up_users = []  # Reset if all players have used power-ups
            available_for_power_ups = players

        power_up_pair = random.sample(available_for_power_ups, 2)
        power_up_users.extend(power_up_pair)

        # Shuffle players to create matchups
        remaining_players = [p for p in players if p not in power_up_pair]
        random.shuffle(remaining_players)

        # Pair players for the game, avoiding repeats
        pairs = []
        while len(pairs) < 5:
            for i in range(0, len(remaining_players), 2):
                pair = (remaining_players[i], remaining_players[i + 1])
                if pair not in used_pairs and pair[::-1] not in used_pairs:
                    pairs.append(pair)
                    used_pairs.add(pair)
                    if len(pairs) == 5:
                        break

        # Ensure power-up users are matched correctly
        if len(pairs) < 5:
            for power_up_user in power_up_pair:
                for opponent in remaining_players:
                    pair = (power_up_user, opponent)
                    if pair not in used_pairs and pair[::-1] not in used_pairs:
                        pairs.append(pair)
                        used_pairs.add(pair)
                        remaining_players.remove(opponent)
                        break

        matches.append({
            "game": game,
            "power_ups": power_up_pair,
            "pairs": pairs
        })

    return matches

# Players
players = ["Yohvan", "Baseer", "Zakia", "Ashwini", "Ramli", "Sara", "Aisha", "Zorran", "Yousaf", "Jay"]
num_games = 5

# Generate matchups
matchups = generate_matchups(players, num_games)

# Display results
for game in matchups:
    print(f"Game {game['game']}:")
    print(f"  Power-Up Users: {', '.join(game['power_ups'])}")
    print("  Matches:")
    for pair in game['pairs']:
        print(f"    {pair[0]} vs {pair[1]}")
    print()
