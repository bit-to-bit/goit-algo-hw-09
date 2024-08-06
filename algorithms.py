""" Calculations"""

from constants import COINS


def get_max_coin(balance):
    """Max coin from coins set <= balance"""
    res = None
    available_coins = [x for x in COINS if x <= balance]
    if available_coins:
        res = max(available_coins)
    return res


def find_coins_greedy(change):
    """Calculate coins set for change"""
    coins = {}
    while change > 0:
        coin = get_max_coin(change)
        if coin:
            change -= coin
            item = coins.get(coin)
            coins[coin] = item + 1 if item else 1
        else:
            change = 0
            coins = None
    return coins if coins else None


def find_min_coins(change):
    """Calculate coins set for change"""
    if change == 0:
        return None
    coin = get_max_coin(change)
    if change - coin == 0:
        return {coin: 1}
    memo = find_min_coins(change - coin)
    item = memo.get(coin)
    memo[coin] = item + 1 if item else 1
    return memo
