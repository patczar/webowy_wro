def oblicz(operacja:str, arg1:int, arg2:int) -> int:
    if operacja == '+': return arg1 + arg2
    if operacja == '-': return arg1 - arg2
    if operacja == '*': return arg1 * arg2
    if operacja == '/': return arg1 // arg2
    if operacja == '^': return arg1 ** arg2
    raise ValueError(f'Nieznana operacja {operacja}')
