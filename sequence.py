import sys


def loop():
    try:
        marked = []
        index = 0
        max_len = int(input("What is the max len? "))
        number = input("What is the sum sequence? ")
        if number == "":
            return
        sequence = number.split(" ")
        for position, n in enumerate(sequence):
            sequence[position] = int(n)
        sequence_index = 0
        while True:
            number = sequence[sequence_index]
            index = (index + int(number)) % max_len
            if index == 0:
                index = max_len
            while index in marked:
                index = (index + 1) % max_len
            marked.append(index)
            print(len(marked), '-> (', index, ')')
            if len(marked) == max_len:
                break
            sequence_index = (sequence_index + 1) % len(sequence)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    loop()
    sys.exit()
