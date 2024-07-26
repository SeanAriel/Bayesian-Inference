from math import comb
import matplotlib.pyplot as plt

SUITS = 4
PRIOR = 1/SUITS
CARDS = 40
HAND = 10
COMMON = 12
UNCOMMON = 10

OBSERVATIONS = range(0, 11)

PLOT1 = False
PLOT2 = False

results = {}
for observation in OBSERVATIONS:

    REMAINING_CARDS = CARDS - COMMON
    THEORETICAL_REMAINING_CARDS = CARDS - UNCOMMON
    REMAINING_HAND = HAND - observation

    # Total possible hands
    total_hands = comb(CARDS, HAND)

    # Ways to get [obs] spades if spades is the common suit
    ways_obs_spades_common = comb(COMMON, observation) * comb(REMAINING_CARDS, REMAINING_HAND)

    # Ways to get [obs] spades if spades has 10 cards
    ways_obs_spades_10 = comb(HAND, observation) * comb(THEORETICAL_REMAINING_CARDS, REMAINING_HAND)

    # Probability calculations
    P_obs_spades_common = ways_obs_spades_common / total_hands
    P_obs_spades_not_common = ways_obs_spades_10 / total_hands
    P_obs_spades = (P_obs_spades_common * PRIOR) + (P_obs_spades_not_common * (1-PRIOR))

    # Bayes' Theorem
    P_spades_common_given_obs_spades = (P_obs_spades_common * PRIOR) / P_obs_spades
    results[observation] = round(P_spades_common_given_obs_spades, 2)

print(results)
if PLOT1:
    x = list(results.keys())
    y = list(results.values())
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o')
    plt.title('Probability Distribution')
    plt.xlabel('Number')
    plt.ylabel('Probability')
    plt.grid(True)
    plt.show()

OBSERVATION = 4
OTHER_SUIT = range(0, HAND - OBSERVATION + 1)

results = {}
for other_suit in OTHER_SUIT:
    remaining_suit = HAND - OBSERVATION - other_suit

    # Total number of ways to choose 10 cards out of 40
    total_hands = comb(40, 10)

    # Number of ways to get [obs] spades and 5 hearts if spades is the common suit (12 spades)
    ways_obs_spades_5_hearts_common = comb(12, OBSERVATION) * comb(10, other_suit) * comb(18, remaining_suit)

    # Number of ways to get [obs] spades and [obs] hearts if spades has 10 cards
    ways_obs_spades_5_hearts_10 = comb(10, OBSERVATION) * comb(10, other_suit) * comb(20, remaining_suit)

    # Since it's impossible to get [obs] spades out of 8 spades, we don't consider it
    # Probability calculations
    P_obs_spades_5_hearts_common = ways_obs_spades_5_hearts_common / total_hands
    P_obs_spades_5_hearts_not_common = ways_obs_spades_5_hearts_10 / total_hands
    P_obs_spades_5_hearts = (P_obs_spades_5_hearts_common * PRIOR) + (P_obs_spades_5_hearts_not_common * (1-PRIOR))

    # Bayes' Theorem
    P_spades_common_given_5_spades_5_hearts = (P_obs_spades_5_hearts_common * PRIOR) / P_obs_spades_5_hearts
    results[other_suit] = round(P_spades_common_given_5_spades_5_hearts, 2)

print(results)
if PLOT2:
    x = list(results.keys())
    y = list(results.values())
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o')
    plt.title('Probability Distribution')
    plt.xlabel('Number')
    plt.ylabel('Probability')
    plt.grid(True)
    plt.show()
