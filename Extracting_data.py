from bs4 import BeautifulSoup
import requests

years = [x for x in range(1930,2019,4) ]

def get_matches(year):
    source = f"https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup"

    response = requests.get(source)
    content = response.text
    content_soup = BeautifulSoup(content, 'lxml')
    # Extract the tables
    matches = content_soup.find_all('div', {'class':'footballbox'})

    home = []
    score = []
    away = []

    for match in matches:
        home.append(match.find('th', {'class':'fhome'}).get_text())
        score.append(match.find('th', {'class':'fscore'}).get_text())
        away.append(match.find('th', {'class':'faway'}).get_text())

    dict_matches ={'Home':home,
                'Score':score,
                'Away':away}

    matches_df = pd.DataFrame(dict_matches)
    matches_df['year'] = str(year)

    return matches_df
historical_data_world_cups = [get_matches(x) for x in years]
historical_data_world_cups_df = pd.concat(historical_data_world_cups, ignore_index=True)
historical_data_world_cups_df.to_csv('D:\\Proyectos\\Soccer_World_Championship\\data\\historical_data_world_cups.csv',index=False)

#fixture and the results from 2022
df_fixture = get_matches('2022')
df_fixture.to_csv('D:\\Proyectos\\Soccer_World_Championship\\data\\fixture.csv') 