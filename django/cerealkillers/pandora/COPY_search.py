import jellyfish
import queue
import json

data_file = 'pandora/COPY_final_completed_index.json'
with open(data_file, 'r') as f:
    data = f.read()
data_dic = json.loads(data)


restaurants = [key for key in data_dic.keys()]

search_item = 'medici'
num_limit = 10

def search(search_item, num_limit=num_limit, restaurants=restaurants):
    q = queue.PriorityQueue(num_limit)
    rv = []
    for restaurant in restaurants:
        score = jellyfish.jaro_winkler(search_item, restaurant)
        if q.full() is False:
            q.put((score, restaurant))
        else:
            lowest = q.get()
            if lowest[0] >= score:
                q.put(lowest)
            else:
                q.put((score, restaurant))
    while q.empty() is False:
        rv.append(q.get()[1])
    return rv 