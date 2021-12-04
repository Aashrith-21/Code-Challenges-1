row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to hide the treasure?\n")
column_no = int(position[0])
map_row_no = int(position[1])

map[map_row_no -1][column_no -1] = "X"

print(f"{row1}\n{row2}\n{row3}")

