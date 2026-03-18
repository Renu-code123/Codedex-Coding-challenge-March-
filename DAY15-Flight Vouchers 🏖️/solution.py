###
def pick_voucher(vouchers, delays, max_wait):
    best_index = -1
    best_value = -1  # FIX

    for i in range(len(vouchers)):
        if delays[i] <= max_wait:
            value = vouchers[i] / delays[i]

            if value > best_value:
                best_value = value
                best_index = i

    return best_index
