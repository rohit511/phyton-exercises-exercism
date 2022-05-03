def tally(rows):
    def tally_this(board, tally_ticks):
        for team, outcome in tally_ticks:
            board[team][outcome] += 1
    tally_board = {}
    for row in rows:
        home, away, outcome = row.split(";")
        for new_entry in (home, away):
            if new_entry not in tally_board.keys():
                tally_board[new_entry] = {"W": 0, "D": 0, "L": 0}
        if outcome == "draw":
            tally_this(tally_board, [(home, "D"), (away, "D")])
        else:  # do the 'win' behaviour, note the 'loss' behaviour happens here too as reversed 'win'
            if outcome == "loss":
                home, away = away, home
            tally_this(tally_board, [(home, "W"), (away, "L")])
    # complete the board
    tally_board = sorted(
        tally_board.items(), key=lambda index: index[0]
    )  # sort by name
    tally_table = []
    for team, l in tally_board:
        tally_table.append(
            [team, sum(l.values()), l["W"], l["D"], l["L"], 3 * l["W"] + l["D"]]
        )
    tbl = sorted(tally_table, key=lambda x: -x[5])  # now have 'score', sort the board,
    tbl.insert(0, ["Team", "MP", "W", "D", "L", "P"])  # insert the header
    # use the format function write it as a list of strings
    line = "{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}"
    return [line.format(*i) for i in tbl]
