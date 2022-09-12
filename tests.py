import pytest

from game import Board
from utils import create_players, create_report


@pytest.fixture
def players():
    return create_players()


@pytest.fixture
def profiles():
    return {
        1: 'impulsivo',
        2: 'exigente',
        3: 'cauteloso',
        4: 'aleatorio'
    }


@pytest.fixture
def board():
    board = Board()
    return board


@pytest.fixture
def game_finish(board, players):
    board.players = players
    board.champion = board.players[0]
    board.rotation = 300
    return board


def test_add_players_in_board(board, players):
    board.players = players
    assert len(board.players) == len(players)


def test_player_max_money(board, players):
    board.players = players
    board.players[0].money += 200
    assert board.player_max_money() == board.players[0]


def test_remove_player(board, players):
    board.players = players
    player_remove = board.players[0]
    board.remove_player(player_remove)
    assert not player_remove in board.players


def test_player_walk(board, players):
    board.players = players
    player_walk = board.players[0]
    property = board.propeties[1]
    property.owner = player_walk.id
    board.walk_player(player_walk)
    assert player_walk.position > 0


def test_player_pay_rent(board, players):
    board.players = players
    player_paying = board.players[0]
    player_owner = board.players[1]
    property = board.propeties[1]
    property.owner = player_owner.id
    player_paying.pay_rent(property, board)
    assert player_paying.money < 300
    assert player_owner.money > 300


def test_player_buy_propety_profile_impulsivo(board, players):
    board.players = players
    player_paying = board.players[0]
    property = board.propeties[1]
    player_paying.buy_property(property, board)
    assert player_paying.money < 300
    assert board.propeties[1].owner == player_paying.id


def test_player_buy_propety_profile_cauteloso(board, players):
    board.players = players
    player_paying = board.players[2]
    property = board.propeties[1]
    player_paying.buy_property(property, board)
    assert player_paying.money < 300
    assert board.propeties[1].owner == player_paying.id


def test_player_buy_propety_profile_exigente(board, players):
    board.players = players
    player_paying = board.players[1]
    property = board.propeties[2]
    property.rent = 60
    player_paying.buy_property(property, board)
    assert player_paying.money < 300
    assert board.propeties[2].owner == player_paying.id


def test_player_buy_propety_profile_aleatorio(board, players):
    board.players = players
    player_paying = board.players[3]
    property = board.propeties[1]
    player_paying.buy_property(property, board, injected_value=1)
    assert player_paying.money < 300
    assert board.propeties[1].owner == player_paying.id


def test_board_run(board, players):
    board.players = players
    player_running = board.players[0]
    board.run(player_running)
    assert player_running.money < 300
    assert player_running.position > 0


def test_board_run_player_remove(board, players):
    board.players = players
    player_running = board.players[0]
    player_running.money = -1
    board.run(player_running)
    assert not player_running in board.players


def test_create_report(game_finish, profiles):
    report = create_report([game_finish])
    assert report[1] == profiles[game_finish.champion.id]
