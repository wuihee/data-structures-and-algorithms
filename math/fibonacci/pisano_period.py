def pisano(mod_val):
    fib_prev = 0
    fib_curr = 1
    mod_seq = [fib_prev % mod_val, fib_curr % mod_val]
    period_len = len(mod_seq) // 2

    while mod_seq[:period_len] != mod_seq[period_len:]:
        fib_prev, fib_curr = fib_curr, fib_prev + fib_curr
        mod_seq.append(fib_curr % mod_val)
        period_len = len(mod_seq) // 2

    return mod_seq[:period_len]
