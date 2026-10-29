try:
    # python -m calculator 로 실행할 때
    from . import add, minus, multiplication, division
except ImportError:
    # 폴더 안에서 python __main__.py 로 직접 실행할 때
    from add import add
    from minus import minus
    from multiplication import multiplication
    from division import division


def main():
    a, b = 10, 5
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {minus(a, b)}")
    print(f"{a} * {b} = {multiplication(a, b)}")
    print(f"{a} / {b} = {division(a, b)}")


if __name__ == "__main__":
    main()