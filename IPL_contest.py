def myfunc(mid):
    import requests
    import time
    import random
    import twitter
    import os

    proxyDict = {
        "http": os.environ.get('IPB_HTTP', ''),
        "https": os.environ.get('IPB_HTTPS', '')
    }

    print(proxyDict)

    class Cricbuzz():
        def __init__(self):
            pass

        def crawl_url(self, url):
            try:
                # r = requests.get(url).json()
                print("From try block")
                r = requests.get(url).json()
                return r
            except Exception:
                print("From except")
                r = requests.get(url, proxies=proxyDict).json()
                return r

        def players_mapping(self, mid):
            url = "http://mapps.cricbuzz.com/cbzios/match/" + mid
            match = self.crawl_url(url)
            players = match.get('players')
            d = {}
            for p in players:
                d[int(p['id'])] = p['name']
            t = {}
            t[int(match.get('team1').get('id'))] = match.get('team1').get('name')
            t[int(match.get('team2').get('id'))] = match.get('team2').get('name')
            return d, t

        def matchinfo(self, mid):
            d = {}
            d['id'] = mid
            url = "http://mapps.cricbuzz.com/cbzios/match/" + mid
            match = self.crawl_url(url)

            d['srs'] = match.get('series_name')
            d['mnum'] = match.get('header', ).get('match_desc')
            d['type'] = match.get('header').get('type')
            d['mchstate'] = match.get('header').get('state')
            d['status'] = match.get('header').get('status')
            d['venue_name'] = match.get('venue').get('name')
            d['venue_location'] = match.get('venue').get('location')
            d['toss'] = match.get('header').get('toss')
            d['official'] = match.get('official')
            d['start_time'] = time.strftime('%Y-%m-%d %H:%M:%S',
                                            time.localtime(int(match.get('header').get('start_time'))))

            # squads
            p_map, _ = self.players_mapping(mid)
            team1 = {}
            team1['name'] = match.get('team1').get('name')
            t1_s = match.get('team1').get('squad')
            if t1_s is None:
                t1_s = []
            team1['squad'] = [p_map[id] for id in t1_s]
            t1_s_b = match.get('team1').get('squad_bench')
            if t1_s_b is None:
                t1_s_b = []
            team1['squad_bench'] = [p_map[id] for id in t1_s_b]
            team2 = {}
            team2['name'] = match.get('team2').get('name')
            t2_s = match.get('team2').get('squad')
            if t2_s is None:
                t2_s = []
            team2['squad'] = [p_map[id] for id in t2_s]
            t2_s_b = match.get('team2').get('squad_bench')
            if t2_s_b is None:
                t2_s_b = []
            team2['squad_bench'] = [p_map[id] for id in t2_s_b]
            d['team1'] = team1
            d['team2'] = team2
            return d

        def matches(self):
            url = "http://mapps.cricbuzz.com/cbzios/match/livematches"
            crawled_content = self.crawl_url(url)
            matches = crawled_content['matches']
            info = []

            for match in matches:
                info.append(self.matchinfo(match['match_id']))
            return info

        def find_match(self, id):
            url = "http://mapps.cricbuzz.com/cbzios/match/livematches"
            crawled_content = self.crawl_url(url)
            matches = crawled_content['matches']

            for match in matches:
                if match['match_id'] == id:
                    return match
            return None

        def livescore(self, mid):
            data = {}
            try:
                comm = self.find_match(mid)
                if comm is None:
                    return data
                batting = comm.get('bat_team')
                if batting is None:
                    return data
                bowling = comm.get('bow_team')
                batsman = comm.get('batsman')
                bowler = comm.get('bowler')

                team_map = {}
                team_map[comm["team1"]["id"]] = comm["team1"]["name"]
                team_map[comm["team2"]["id"]] = comm["team2"]["name"]

                if batsman is None:
                    batsman = []
                if bowler is None:
                    bowler = []
                d = {}
                d['team'] = team_map[batting.get('id')]
                d['score'] = []
                d['batsman'] = []
                for player in batsman:
                    d['batsman'].append(
                        {'name': player['name'], 'runs': player['r'], 'balls': player['b'], 'fours': player['4s'],
                         'six': player['6s']})
                binngs = batting.get('innings')
                if binngs is None:
                    binngs = []
                for inng in binngs:
                    d['score'].append({'inning_num': inng['id'], 'runs': inng['score'], 'wickets': inng['wkts'],
                                       'overs': inng['overs'], 'declare': inng.get('decl')})
                data['batting'] = d
                d = {}
                d['team'] = team_map[bowling.get('id')]
                d['score'] = []
                d['bowler'] = []
                for player in bowler:
                    d['bowler'].append(
                        {'name': player['name'], 'overs': player['o'], 'maidens': player['m'], 'runs': player['r'],
                         'wickets': player['w']})
                bwinngs = bowling.get('innings')
                if bwinngs is None:
                    bwinngs = []
                for inng in bwinngs:
                    d['score'].append({'inning_num': inng['id'], 'runs': inng['score'], 'wickets': inng['wkts'],
                                       'overs': inng['overs'], 'declare': inng.get('decl')})
                data['bowling'] = d
                return data
            except Exception:
                raise

        def commentary(self, mid):
            data = {}
            try:
                url = "http://mapps.cricbuzz.com/cbzios/match/" + mid + "/commentary"
                comm = self.crawl_url(url).get('comm_lines')
                d = []
                for c in comm:
                    if "comm" in c:
                        d.append({"comm": c.get("comm"), "over": c.get("o_no")})
                data['commentary'] = d
                return data
            except Exception:
                raise

        def scorecard(self, mid):
            try:
                url = "http://mapps.cricbuzz.com/cbzios/match/" + mid + "/scorecard.json"
                scard = self.crawl_url(url)
                p_map, t_map = self.players_mapping(mid)

                innings = scard.get('Innings')
                data = {}
                d = []
                card = {}
                for inng in innings:
                    card['batteam'] = inng.get('bat_team_name')
                    card['runs'] = inng.get('score')
                    card['wickets'] = inng.get('wkts')
                    card['overs'] = inng.get('ovr')
                    card['inng_num'] = inng.get('innings_id')
                    extras = inng.get("extras")
                    card["extras"] = {"total": extras.get("t"), "byes": extras.get("b"), "lbyes": extras.get("lb"),
                                      "wides": extras.get("wd"), "nballs": extras.get("nb"), "penalty": extras.get("p")}
                    batplayers = inng.get('batsmen')
                    if batplayers is None:
                        batplayers = []
                    batsman = []
                    bowlers = []
                    fow = []
                    for player in batplayers:
                        status = player.get('out_desc')
                        p_name = p_map[int(player.get('id'))]
                        batsman.append(
                            {'name': p_name, 'runs': player['r'], 'balls': player['b'], 'fours': player['4s'],
                             'six': player['6s'], 'dismissal': status})
                    card['batcard'] = batsman
                    card['bowlteam'] = t_map[int(inng.get("bowl_team_id"))]
                    bowlplayers = inng.get('bowlers')
                    if bowlplayers is None:
                        bowlplayers = []
                    for player in bowlplayers:
                        p_name = p_map[int(player.get('id'))]
                        bowlers.append(
                            {'name': p_name, 'overs': player['o'], 'maidens': player['m'], 'runs': player['r'],
                             'wickets': player['w'], 'wides': player['wd'], 'nballs': player['n']})
                    card['bowlcard'] = bowlers
                    fall_wickets = inng.get("fow")
                    if fall_wickets is None:
                        fall_wickets = []
                    for p in fall_wickets:
                        p_name = p_map[int(p.get('id'))]
                        fow.append({"name": p_name, "wkt_num": p.get("wkt_nbr"), "score": p.get("score"),
                                    "overs": p.get("over")})
                    card["fall_wickets"] = fow
                    d.append(card.copy())
                data['scorecard'] = d
                return data
            except Exception:
                raise

        def fullcommentary(self, mid):
            data = {}
            try:
                url = "https://www.cricbuzz.com/match-api/" + mid + "/commentary-full.json"
                comm = self.crawl_url(url).get('comm_lines')
                d = []
                for c in comm:
                    if "comm" in c:
                        d.append({"comm": c.get("comm"), "over": c.get("o_no")})
                data['fullcommentary'] = d
                return data
            except Exception:
                raise

        def players(self, mid):
            data = {}
            try:
                url = "https://www.cricbuzz.com/match-api/" + mid + "/commentary.json"
                players = self.crawl_url(url).get('players')
                d = []
                for c in players:
                    if "player" in c:
                        d.append({"id": c.get("id"), "f_name": c.get("f_name"), "name": c.get("name"),
                                  "bat_style": c.get("bat_style"), "bowl_style": c.get("bowl_style")})
                data['players'] = d
                return data
            except Exception:
                raise

    extra_words = ['Wow!!', 'amazing!', 'Good stuff!', 'Greatttt one', 'Superb!', '', 'Evergreen shot!', 'Niceeee',
                   'Woahhh', 'Stunner', 'Perfect', 'Unreal!!', "\U0001F618", "\U0001F607", "\U0001F49D", "\U0001F49A",
                   "\U0001F4AB"]
    smileys = ["\U0001F973", "\U0001F60E", "\U0001F917", "\U0001F60D", "\U0001F970", "\U0001F929", "\U0001F618",
               "\U0001F607", "\U0001F49D", "\U0001F49A", "\U0001F4AB", "\U0001F44C", "\U0001F91F", "\U0001F44F",
               "\U0001F483", "\U0001F57A"]

    c = Cricbuzz()

    count = 0

    while count < 360:

        with open('dummy.txt', 'r') as f:
            content = f.read()

        xxx, yyy = content.split(' ')
        total_fours = int(xxx)
        total_sixes = int(yyy)
        scard = c.scorecard(mid)

        x = scard['scorecard']
        print(x)
        #print(total_fours, total_sixes)

        for i in x:

            fours = 0
            sixes = 0

            if float(i['overs']) <= 6.0:
                print("Over is less than 6.0 - " + str(i['overs']))
                for j in i['batcard']:
                    fours = fours + int(j['fours'])
                    sixes = sixes + int(j['six'])

                four_diff = fours - total_fours
                six_diff = sixes - total_sixes

                if four_diff > 0 or six_diff > 0:

                    if four_diff > 0:
                        
                        api = []

                    if six_diff > 0:
                    
                        api = []

                    total_fours = fours
                    total_sixes = sixes

                    content_to_write = str(total_fours) + " " + str(total_sixes)

                    with open('dummy.txt', 'w') as w:
                        w.write(content_to_write)

        time.sleep(30)
        count = count + 1
        print("Iteration count: " + str(count))

        if count == 150 or count == 355:

            content_to_write = "0 0"

            with open('dummy.txt', 'w') as w:
                w.write(content_to_write)
            print("File reset done")


import datetime
from time import gmtime, strftime

now = datetime.datetime.now()
daay = now.strftime("%A")

curtime = strftime("%H:%M", gmtime())

midd = str(now.strftime("%d%B%p"))
print(midd)


today_val = {

    '13OctoberPM' : '30440',
    '14OctoberPM' : '30445',
    '15OctoberPM' : '30449',
    '16OctoberPM' : '30450',
    '17OctoberAM' : '30454',
    '17OctoberPM' : '30459',
    '18OctoberAM' : '30460',
    '18OctoberPM' : '30464',
    '19OctoberPM' : '30465',
    '20OctoberPM' : '30469',
    '21OctoberPM' : '30474',
    '22OctoberPM' : '30475',
    '23OctoberPM' : '30479',
    '24OctoberPM' : '30484',
    '25OctoberAM' : '30494',
    '25OctoberPM' : '30495',
    '26OctoberPM' : '30500',
    '27OctoberPM' : '30504',
    '28OctoberPM' : '30505',
    '29OctoberPM' : '30510',
    '30OctoberPM' : '30515',
    '31OctoberAM' : '30519',
    '31OctoberPM' : '30520',
    '01NovemberAM' : '30524',
    '01NovemberPM' : '30529',
    '02NovemberPM' : '30534',
    '03NovemberPM' : '30539',
    }


mid = '30409'

myfunc(mid)
