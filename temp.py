def minimaxPolicy(game, state, player):

    def recurse(state, player):

        # start with the base case
        if game.isEnd(state) == True:

            return (game.utility(state, player), None)
        if cache.has_key((state, player)):
            return cache[(state, player)]


        choices = [(recurse(game.successor(state, action), -1*player)[0], action) for action in game.actions(state)]


        if player == +1:
            val = max(choices)
        else:
            val = min(choices)
        cache[(state, player)] = val
        return val


    value, action = recurse(state, player)
    return (value, action)
