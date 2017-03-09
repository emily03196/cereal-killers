import final_indexer
import jellyfish
import queue

restaurants = [key for key in final_indexer.main_index.keys()]

search_item = 'medici'
num_limit = 10

def search(search_item, num_limit=num_limit, restaurants=restaurants):
    q = queue.PriorityQueue(num_limit)
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
        print (q.get()[1])