from game import Board
from utils import create_players, create_report, show_report


def main():
    result = []
    for index in range(300):
        board = Board()
        players = create_players()
        board.players = players
        while board.champion is None:
            for player in board.players:
                if len(board.players) == 1:
                    board.champion = player
                    break

                elif board.rotation >= 1000:
                    board.champion = board.player_max_money()
                    break

                board.run(player)
            board.rotation += 1

        result.append(board)
    report = create_report(result)
    show_report(result, *report)


if __name__ == '__main__':
    main()
