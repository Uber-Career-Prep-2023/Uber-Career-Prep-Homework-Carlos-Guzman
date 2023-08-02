"""Given a list of coin denominations and a target sum, return the number of possible ways to make change for that sum.

Examples:
Input:
Coins: [2, 5, 10]

Sum: 20
Output: 6 (Options are: 10 2s; 4 5s; 2 10s; 5 2s & 2 5s; 5 2s & 1 10; 2 5s & 1 10)
"""
"""
This is solved using dynamic programming with memoization, calculating all possible ways to give all different changes until we reach the desired change.

1) We define an array dp of size (change we want to give + 1). Each position in this array represents a specific change. Position 0 represents paying with the unit, i.e., paying with the current coin we are trying to form the change. The first position represents a change of one, the second position a change of value 2, and so on. The value stored in each of these positions represents all possible ways to form that change using the available coins in the array of available coins. We will initialize all values of this array to 0 except for the 0th position, which will always be 1 since it represents paying with the current coin we have. We will build the combinations later.
2) We iterate over all available coins that we have to form the change.
3) For each available coin, we iterate from the value of that coin until the end of the dp array, which represents all possible changes that can be given until we reach the desired change. We start from the value of that coin because we cannot generate a change smaller than the value of that coin using that current coin. This means that coin acts as the minimum threshold from which we can start generating different changes. Since it is a coin of fixed value, we start from there, considering that there is one possible way to give that change, which is by using that coin only.
4) We add to the value of the current dp position all the possible ways to generate change once we have that particular coin. In other words, for all the changes that we will give up to that point, considering this coin included, we add all the possible ways to give the remaining change, considering that this coin serves as our pivot, an anchor for giving change. Thus, we need to know how many ways there are to generate the remaining change. We achieve this with the following formula:
dp[i] = dp[i] + dp[i-coin]. This means that we add the possibilities we already have for forming change with previous coins to the possibilities of forming the different changes we can make with the current coin, including the unit. For the first calculation, we have dp[5] = dp[5] + dp[5 - 5], which means that the only possibility at that initial point is to give the unit or the current coin we are using to form the different changes.
5) We continue doing this for all the possibilities of change with all the available coins until we finish with all the coins.
6) We return the last value of the dp array since it represents the sum of all the possibilities of all different ways we can give change using the different coins.
"""

def coin_change(coins, amount):
    # Initialize an array to store the number of ways to make change for all amounts from 0 to amount
    dp = [0] * (amount + 1)
    # Set the first element of the array to 1, since there is 1 way to make change for 0
    dp[0] = 1

    # Iterate over all coins
    for coin in coins:
        # Iterate over all amounts from coin to amount + 1
        for i in range(coin, amount + 1):
            # Add the number of ways to make change for i - coin to the number of ways to make change for i
            dp[i] = dp[i] + dp[i - coin]

    # Return the number of ways to make change for amount
    return dp[-1]

coins = [1, 5, 10]
amount = 15
print(coin_change(coins, amount))  # Output: 6 (Options are: 10 5s; 5 5s & 1 10; 5 1s & 2 5s & 1 10; 10 1s & 1 5s & 1 10; 10 1s & 1 5s & 1 10; 1 5s & 1 10 & 4 1s; 2 5s & 1 10 & 3 1s)


coins = [2, 5, 10]
amount = 3
print(coin_change(coins, amount))  # Output: 0 (There are no ways to make change for 3 using the given coins)

coins = [1]
amount = 5
print(coin_change(coins, amount))  # Output: 1 (Only one way to make change for 5, which is using five 1s)

coins = [1]
amount = 0
print(coin_change(coins, amount))  # Output: 1 (There is one way to make change for 0, which is not giving any change)

coins = []
amount = 10
print(coin_change(coins, amount))  # Output: 0 (No coins available, so there are no ways to make change)
