
def repl_str(input: str) -> str:
    out = input
    DIGITS = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    for i, d in enumerate(DIGITS):
        repl = f'{d[0]}{i + 1}{d[-1]}'
        out = out.replace(d, repl)

    return out


if __name__ == '__main__':
    with open('content/day_1.txt', 'r') as f:
        content = repl_str(f.read())
    with open('content/day_1_transform.txt', 'w') as f:
        f.write(content)
