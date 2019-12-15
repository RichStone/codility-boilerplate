def solution(N, S):
    if S == '':
        return 2 * N

    possible_family_reservations = 0
    reserved_seats = S.split(' ')

    # initialize empty seats
    row_length = 10
    seat_plan = [[False for col in range(row_length)] for row in range(N)]

    # map reservations to 2D array
    for seat in reserved_seats:
        reserved_col = int(ord(seat[-1].lower())) - 96
        reserved_row = int(seat[:-1])
        seat_plan[reserved_row - 1][reserved_col - 1] = True

    # get family numbers
    family_size = 4
    family_possible = 0
    for row in seat_plan:
        unreserved_sequence = 0

        for i in range(1, 5):
            seat_reserved = row[i]

            if seat_reserved:
                break

            unreserved_sequence += 1
            if unreserved_sequence == family_size:
                family_possible += 1
                # reserve seats
                row[1:4] = [True, True, True, True]

        unreserved_sequence = 0
        for i in range(3, 7):
            seat_reserved = row[i]

            if seat_reserved:
                break

            unreserved_sequence += 1
            if unreserved_sequence == family_size:
                family_possible += 1
                # reserve seats
                row[3:6] = [True, True, True, True]

        unreserved_sequence = 0
        for i in range(5, 9):
            seat_reserved = row[i]

            if seat_reserved:
                break

            unreserved_sequence += 1
            if unreserved_sequence == family_size:
                family_possible += 1
                # reserve seats
                row[5:8] = [True, True, True, True]

    return family_possible


if __name__ == '__main__':
    N = 2
    S = '1A 2F 1C'
    print(solution(N, S))
