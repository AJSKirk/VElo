import sys, getopt, itertools

class Player(object):
    def __init__(self, name):
        self.__name = name
        self.score = 1200 # Arbitary but lines well w/ FIDE
    def get_name():
        return self.name
    def get_score():
        return self.score
    def expected_score(opponent):
        return 1.0 / (1 + 10 ** ((opponent.get_score() - self.score) / 400.0))
    def play(opponent, result, k=40.0): # k=40 for rapid learning
        self.score += k * (result - expected_score(opponent))

def play_round(player1, player2):
    print("-------------------------------")
    print("[1] {} ({})".format(player1.get_name(), player1.get_score()))
    print("[2] {} ({})".format(player2.get_name(), player2.get_score()))
    win_id = raw_input("Who won? ")
    while win_id not in (1, 2, 'q'):
        win_id = raw_input("Please enter either a 1 or a 2, or a q to quit: ")
    if win_id == 'q':
        return 0
    if win_id == 1:
        winner = player1
        loser = player2
    else:
        winner = player2
        loser = player1
    winner.play(loser, 1)
    loser.play(winner, 0)
    print("New Scores:")
    print("[1] {} ({})".format(player1.get_name(), player1.get_score()))
    print("[2] {} ({})".format(player2.get_name(), player2.get_score()))
    return 1

def main(argv):
    infile = ''
    outfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print("elo.py -i <infile> -o <outfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == 'h':
            print("elo.py -i <infile> -o <outfile>")
            sys.exit()
        elif opt in ('-i', '--ifile'):
            infile = arg
        elif opt in ('-o', '--ofile'):
            ofile = arg
    players = []
    with open(ifile, 'r') as f:
        for name in f:
            players.append(Player(name))

    for (player1, player2) in itertools.permutations(players, 2):
        if play_round(player1, player2) == 0:
            break

    with open(ofile, 'w') as f:
        for player in players:
            f.write(player.get_name() + ',' + player.get_score())
    return


if __name__ == "__main__":
    main(sys.argv[1:]) # Call on default Visiting Enki setup
