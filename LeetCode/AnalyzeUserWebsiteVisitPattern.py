from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        def prepare_timestamps(username, timestamp, website):
            track = {}

            for i in range(len(username)):
                if username[i] not in track:
                    track[username[i]] = []
                    track[username[i]].append((timestamp[i], website[i]))
                else:
                    track[username[i]].append((timestamp[i], website[i]))
            return track
        
        def make_combinations(users):
            for user in users.keys():
                web = [track[1] for track in users[user]]
                web = list(combinations(web, 3))
                websites = []
                for i in web:
                    if i not in websites:
                        websites.append(i)
                users[user] = websites
            return users
       

        users = prepare_timestamps(username, timestamp, website)
        for user in users.keys():
            users[user].sort(key = lambda x:x[0])
        
        websites = make_combinations(users)
        
        
        count_combinations = {}
        for names in websites.keys():
            for combination in websites[names]:
                if combination not in count_combinations:
                    count_combinations[combination] = 1
                else:
                    count_combinations[combination] += 1
        print(count_combinations)
        
        max_ = 0
        pattern = ""
        for combination_ in count_combinations.keys():
            if count_combinations[combination_] > max_:
                max_ = count_combinations[combination_]
                pattern = combination_
            elif count_combinations[combination_] == max_:
                if pattern > combination_:
                    pattern = combination_
        return pattern
                
            
        
        
        
