hackathon_1 = ["Team Kenzie", "Team Ateliware", "Team VHSYS", "Team Mirum"]
hackathon_2 = ["Team Ateliware", "Team Kenzie", "Team VHSYS", "Team Mirum"]
hackathon_3 = ["Team Mirum", "Team Ateliware", "Team VHSYS", "Team Kenzie"]

def get_score(team_name, team):
    index = team.index(team_name)
    
    return f"A {team[index]} ficou classificada em {index + 1}"

print(get_score("Team Ateliware", hackathon_1))

print(get_score("Team Kenzie", hackathon_1))

print(get_score("Team Mirum", hackathon_3))

