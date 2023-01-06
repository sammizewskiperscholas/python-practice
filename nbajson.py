import requests
import json

response = requests.get("http://data.nba.net/prod/v2/2018/teams.json")
data=json.loads(response.text)
data = response.json()
print(type(data))
# print(data)
print(data.keys())
print(data['league'].keys())
print(type(data['league']['standard']))
print(len(data['league']['standard']))

#to include only teams that are NBA franchises. we can create new list nba_teams
nba_teams=[team for team in data['league']['standard'] if team['isNBAFranchise']]

with open('nba_teams.json',"w") as f:
    json.dump(nba_teams,f,indent=4,sort_keys=True)

with open('nba_teams.json',"r") as f:
    data = json.load(f)

#group teams into divisions(Atlantic, Central, Southwest, Northwest, Pacific and Southwest)
def group_teams_by_division(team):
    return(team['fullName'], team['divName'])

with open('nba_teams.json') as f:
    data=json.load(f, object_hook=group_teams_by_division)

#create dictnoary where key will be division name and corresponding value will be a list of all teams in that division
teams_by_division={}
for i in range(len(data)):
    team, division = data[i]
    if division not in teams_by_division.keys():
        teams_by_division[division] = []
    teams_by_division[division].append(team)

# print(teams_by_division)
with open('teams_by_division.json',"w") as f:
    json.dump(teams_by_division, f, indent=4, sort_keys=True)



