import pandas as pd
import numpy as np

draws = pd.read_csv("2021/4/data.csv", header=None, nrows = 1)
draws = [x for x in draws.iloc[0]]

cards = pd.read_csv("2021/4/data.csv", header=None, skiprows = 1)
cards.columns = ["cards"]
cards = [row.replace("  ", " ").strip().split(' ', 5) for row in cards['cards']]
cards_transpose = [[card[i] for card in cards] for i in range(0, 5)]
cards = pd.concat([pd.Series(x) for x in cards_transpose], axis=1)
##
idxs = list(np.arange(0, cards.shape[0], 5)) + [cards.shape[0]]
cards = [cards[idxs[i]:idxs[i+1]].reset_index(drop=True) for i in range(0, len(idxs)-1)]
for i in range(0, len(cards)):
    cards[i].columns = ["c" + str(cc) for cc in cards[i].columns]
    cards[i] = cards[i].astype(int)

# ---- part 1 ----

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
    if any(card.sum() == -5) or any(card.sum(axis = 1) == -5):        
        return (draw, card.sum().sum() + len(np.where(np.array(card) == -1)[0]))
    else:
        return card

bingos = []
for draw in draws:    
    for i in range(0, len(cards)):        
        try:
            cards[i] = bingo(draw, cards[i])
        except:
            bingos.append(cards[i])

bingos[0][0] * bingos[0][1]
