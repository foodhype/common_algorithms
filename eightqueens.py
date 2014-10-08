def is_safe(board, row, col):
    for i in xrange(col - 1, -1, -1):
        if board[row][i]:
            return False
    for i, j in zip(xrange(row - 1, -1, -1), xrange(col - 1, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(xrange(row + 1, 8), xrange(col - 1, -1, -1)):
        if board[i][j]:
            return False
    return True


def eightqueens(board=None, col=0):
    """Determine if eight queens can be placed on a board where no queen can
    attack another queen."""
    if board is None:
        board = [[False for _ in xrange(8)] for _ in xrange(8)]
    if col >= 8:
        return True
    for row in xrange(8):
        if is_safe(board, row, col):
            board[row][col] = True
            if eightqueens(board, col + 1):
                return True
            board[row][col] = False

    return False


def main():
    print eightqueens()


if __name__ == "__main__":
    main()
