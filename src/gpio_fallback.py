from typing import Literal

BOARD = 'BOARD'
BCM = 'BCM'

OUT = 'OUT'
IN = 'IN'

HIGH = True
LOW = False


def setmode(mode: Literal['BOARD', 'BCM']) -> None:
    print(f'Setting mode to {mode}')


def setup(pin: int, mode: Literal['OUT', 'IN']) -> None:
    print(f'Setting pin {pin} to {mode}')


def output(pin: int, value: bool) -> None:
    print(f'Outputting {value} on {pin}')


def cleanup() -> None:
    print('Done')

