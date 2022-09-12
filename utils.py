from game import Board
from player import Player


def create_players():
    players = []
    for i in range(1, 5):
        players.append(Player(i))

    return players


def create_report(boards: Board):
    profiles = dict(impulsivo=0, exigente=0, cauteloso=0, aleatorio=0)
    total_timeout = sum([1 for i in boards if i.rotation >= 1000])
    media_rotation = sum([result.rotation for result in boards])
    for i in boards:
        profiles[i.champion.profile] += 1

    champion_profile = max(profiles, key=profiles.get)
    percentages = list(map(lambda x: ((int(x) * 100) / len(boards)), profiles.values()))

    return percentages, champion_profile, media_rotation, total_timeout, profiles


def show_report(boards, percentages, champion_profile, media_rotation, total_timeout, profiles):
    print(f'''
    Total timeout: {total_timeout} 
    Rodadas médias: {media_rotation / len(boards):.2f}    
    Percentual por profile: 
       {list(profiles.keys())[0].title()}: {percentages[0]:.2f} %
       {list(profiles.keys())[1].title()}: {percentages[1]:.2f} %
       {list(profiles.keys())[2].title()}: {percentages[2]:.2f} %
       {list(profiles.keys())[3].title()}: {percentages[3]:.2f} %
    Perfil Campeão: {champion_profile.title()} 
    ''')
