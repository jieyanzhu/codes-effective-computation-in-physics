def decay(index, database):
    lambdas = database.decay_constants()
    try:
        lambda_i = lambdas[index]   # gets decay constant at index in the list
    except LookupError:
        raise Exception("value not found in the decay constants object!")
    return lambda_i

