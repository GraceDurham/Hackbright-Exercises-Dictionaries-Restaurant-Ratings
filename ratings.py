"""Restaurant rating lister."""

def process_scores():
    """Reads scores file and return dictionary of {restaurant_name: score}. """

    restaurant_data = open("scores.txt") 
    
    scores = {}

    for line in restaurant_data:
        line = line.rstrip()
        restaurant, score = line.split(":")
        scores[restaurant] = int(score)   
        # print restaurant_name, rating 

    return scores 


def user_add_restaurant(scores):
    """User adds a restaurant and rating"""

  
    restaurant_name = raw_input("Please input a restaurant name")
    rating = int(raw_input("Please give that restaurant a rating"))

    scores[restaurant_name] = rating



def sort_print_restaurants(scores):
    """Print restaurants and ratings, sorted"""

    for restaurant, rating in sorted(scores.items()):
        print "%s is rated at %s" % (restaurant, rating)


# read existing scores in from file
scores = process_scores()

#allow user to add a restaurant/rating pair
user_add_restaurant(scores)

#print an alphabetical list of all rated restaurants and their ratings
sort_print_restaurants(scores)


# graces_dictionary = {"hair" :"brown", "eyes":"brown", "height":"short", "weight":"none of your business"}

# grace_sort = graces_dictionary.values()
# grace_sort.sort()
# for value in grace_sort:
#     print value

# #grabs the keys in the dictionary sorts them with the sorted funtion 
# for key in sorted(graces_dictionary):
#     print key





