rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
boxes = [set() for _ in range(9)]

for i in range(9):
    for j in range(9):
        x = board[i][j]

        if x == ".":
            continue

        box_index = 3 * (i // 3) + j // 3

        # 判断 x 是否已经出现在：
        # rows[i]
        # cols[j]
        # boxes[box_index]
        if x in rows[i] or x in cols[j] or x in boxes[box_index]:
            return False
        # 如果重复 → False

        # 否则分别加入三个 set
        rows[i].add(x)
        cols[j].add(x)
        boxes[box_index].add(x)
return True