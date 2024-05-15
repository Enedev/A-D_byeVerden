#Dar las vueltas utilizando el menor número de monedas.
# Supongamos que usted es un programador para un fabricante de máquinas expendedoras. 
#Su empresa desea agilizar el esfuerzo dando la menor cantidad posible de monedas para las vueltas de cada transacción.

def min_coins(coins, amount, cache={}):

  if amount == 0:
    return 0, []  

  if amount < 0:
    return float('inf'), None  #no negativos

  if amount in cache:
    return cache[amount]  

  min_count = float('inf')
  min_coins_used = None

  for coin in coins:
    if coin > amount:
      continue  
    count, coins_used_for_coin = min_coins(coins, amount - coin, cache)
    if count + 1 < min_count:
      min_count = count + 1
      min_coins_used = [coin] + coins_used_for_coin

  cache[amount] = (min_count, min_coins_used)
  return min_count, min_coins_used

coins = [1, 5, 10, 25]
amount = 30

min_count, coins_used = min_coins(coins, amount)

print("Cantidad mínima de monedas necesarias:", min_count)
if coins_used:
  print("Monedas utilizadas:", coins_used)
else:
  print("No combination of coins found for the given amount.")