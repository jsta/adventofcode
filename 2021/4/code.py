import pandas as pd
import numpy as np

draws = pd.read_csv("2021/4/data.csv", header=None, nrows=1)
draws = [x for x in draws.iloc[0]]

cards = pd.read_csv("2021/4/data.csv", header=None, skiprows=1)
cards.columns = ["cards"]
cards = [row.replace("  ", " ").strip().split(" ", 5) for row in cards["cards"]]
cards_transpose = [[card[i] for card in cards] for i in range(0, 5)]
cards = pd.concat([pd.Series(x) for x in cards_transpose], axis=1)
##
idxs = list(np.arange(0, cards.shape[0], 5)) + [cards.shape[0]]
cards = [
    cards[idxs[i] : idxs[i + 1]].reset_index(drop=True) for i in range(0, len(idxs) - 1)
]
for i in range(0, len(cards)):
    cards[i].columns = ["c" + str(cc) for cc in cards[i].columns]
    cards[i] = cards[i].astype(int)


def mark_matches(draw, card):
    matches = np.where(np.array(card) == draw)
    if len(matches[0]) == 0:
        return card
    else:
        card.iloc[[int(matches[0])], [int(matches[1])]] = -1
        return card


def bingo(draw, card):
    if card.shape[0] == 2:
        raise Exception
    card = mark_matches(draw, card)
    if any(card.sum() == -5) or any(card.sum(axis=1) == -5):
        return (draw, card.sum().sum() + len(np.where(np.array(card) == -1)[0]))
    else:
        return card


# ---- part 1 ----

cards_pt1 = cards.copy()
bingos = []
for draw in draws:
    for i in range(0, len(cards_pt1)):
        try:
            cards_pt1[i] = bingo(draw, cards_pt1[i])
        except:
            bingos.append(cards_pt1[i])

bingos[0][0] * bingos[0][1]


# ---- part 2 ----
cards_pt2 = cards.copy()
bingos = []
for draw in draws:
    for i in range(0, len(cards_pt2)):
        try:
            cards_pt2[i] = bingo(draw, cards_pt2[i])
        except:
            bingos.append((i, cards_pt2[i]))

card_index = [x for x in range(0, len(cards_pt2))]
card_bingo = [i for (i, (draw, card_sum)) in bingos]
card_sum = [card_sum for (i, (draw, card_sum)) in bingos]
card_draws = [draw for (i, (draw, card_sum)) in bingos]


def last_bingo(bingo, card_index):
    # bingo = card_bingo[0]
    if len(card_index) == 1:
        raise Exception
    if bingo in card_index:
        card_index.pop(int(np.where(np.array(bingo) == card_index)[0]))
    return card_index


for bingo in card_bingo:
    try:
        card_index = last_bingo(bingo, card_index)
    except:
        break

# first instance where last card is solved
last_card_solved_i = np.where(np.array(card_bingo) == card_index[0])[0].tolist()[0]
card_sum[last_card_solved_i] * card_draws[last_card_solved_i]
