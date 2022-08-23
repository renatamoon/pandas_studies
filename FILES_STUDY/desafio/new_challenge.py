class HigherNumber:

    @classmethod
    def check_int_validity(
            cls, number
    ) -> bool:

        if type(number) != int:
            raise ValueError
        return True

    @classmethod
    def next_higher_numbers(cls, number: int):
        cls.check_int_validity(number=number)

        list_numbers = list(map(int, str(number)))

        for number in reversed(range(len(list_numbers))):
            if number == 0:
                return list_numbers
            if list_numbers[number] > list_numbers[number - 1]:
                break
        left_number, right_number = list_numbers[:number], list_numbers[number:]

        for number in reversed(range(len(right_number))):
            if right_number[number] > left_number[-1]:
                right_number[number], left_number[-1] = left_number[-1], right_number[number]
                break
        higher_number = int("".join(map(str, (left_number + sorted(right_number)))))
        return higher_number


if __name__ == '__main__':
    response = HigherNumber.next_higher_numbers(
        number=5047
    )
    print(response)
