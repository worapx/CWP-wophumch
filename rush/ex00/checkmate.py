def checkmate(board: str) -> None:
    lines = [line for line in board.splitlines() if line]
    if not lines:
        return

    size = len(lines)
    for line in lines:
        if len(line) != size:
            return

    king_pos = None
    enemies = []

    for r in range(size):
        for c in range(size):
            char = lines[r][c]
            if char == 'K':
                king_pos = (r, c)
            elif char in ('P', 'B', 'R', 'Q'):
                enemies.append((char, r, c))

    if not king_pos:
        return

    kr, kc = king_pos

    def has_clear_path(er, ec, dr, dc) -> bool:
        curr_r, curr_c = er + dr, ec + dc
        while 0 <= curr_r < size and 0 <= curr_c < size:
            if curr_r == kr and curr_c == kc:
                return True
            if lines[curr_r][curr_c] != '.':
                return False
            curr_r += dr
            curr_c += dc
        return False

    for piece, er, ec in enemies:
        # --- PAWN (P) ---
        if piece == 'P':
            if er - 1 == kr and (ec - 1 == kc or ec + 1 == kc):
                print("Success")
                return

        # --- ROOK (R) ---
        elif piece == 'R':
            if er == kr or ec == kc:
                dr = 0 if er == kr else (1 if kr > er else -1)
                dc = 0 if ec == kc else (1 if kc > ec else -1)
                if has_clear_path(er, ec, dr, dc):
                    print("Success")
                    return

        # --- BISHOP (B) ---
        elif piece == 'B':
            if abs(er - kr) == abs(ec - kc):
                dr = 1 if kr > er else -1
                dc = 1 if kc > ec else -1
                if has_clear_path(er, ec, dr, dc):
                    print("Success")
                    return

        # --- QUEEN (Q) ---
        elif piece == 'Q':
            if er == kr or ec == kc or abs(er - kr) == abs(ec - kc):
                dr = 0 if er == kr else (1 if kr > er else -1)
                dc = 0 if ec == kc else (1 if kc > ec else -1)
                if has_clear_path(er, ec, dr, dc):
                    print("Success")
                    return

    print("Fail")
