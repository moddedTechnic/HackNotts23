
def play(n: int) -> None:
    """Play a tone representing the number `n`, a value from 0x0-0xF"""

    base_time = 1
    high_time = (base_time/16) * n
    low_time = base_time - high_time

    #print(high_time)
    #print(low_time)