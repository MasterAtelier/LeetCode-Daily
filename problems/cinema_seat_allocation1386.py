class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        valid_set = [
            {2, 3, 4, 5},
            {4, 5, 6, 7},
            {6, 7, 8, 9}
        ]
        occupied_seats = {}
        for row, seat in reservedSeats:
            if row not in occupied_seats:
                occupied_seats[row] = []
            occupied_seats[row].append(seat)
        placed_count = (n - len(occupied_seats)) * 2
        for row, seats in occupied_seats.items():
            is_valid_first_set = True
            is_valid_second_set = True
            is_valid_third_set = True
            for j in range(len(seats)):
                if seats[j] in valid_set[0]:
                    is_valid_first_set = False
                if seats[j] in valid_set[1]:
                    is_valid_second_set = False
                if seats[j] in valid_set[2]:
                    is_valid_third_set = False
            if is_valid_first_set:
                placed_count += 1
                is_valid_second_set = False
            if is_valid_second_set:
                placed_count += 1
                is_valid_third_set = False
            if is_valid_third_set:
                placed_count += 1                
        return placed_count
