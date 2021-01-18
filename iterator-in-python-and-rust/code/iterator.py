class GenerateNumbers:
    def __init__(self, start, end):
        self.current = start
        self.high = end

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


class AlphaList:
    def __init__(self, elements: list) -> None:
        self.alpha_list = elements

    def __iter__(self):
        return AlphaListIterator(self.alpha_list)


class AlphaListIterator:
    def __init__(self, elements: list) -> None:
        self.alpha_list = elements
        self.index = 0

    def __next__(self):
        try:
            result = self.alpha_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

    def __iter__(self):
        return self


if __name__ == "__main__":
    g = GenerateNumbers(0, 10)
    for i in g:
        print(i)

    alpha_list = AlphaList([1, 2, 3])
    print(alpha_list)
    for e in alpha_list:
        print(e)

    for e in alpha_list:
        print(e)

    it1 = AlphaListIterator([1, 2, 3, 4, 5])
    for e in it1:
        print(e)

    for e in it1:
        print("again...")
        print(e)
