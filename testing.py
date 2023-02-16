from fuzzywuzzy import fuzz
from fuzzywuzzy import process


print(fuzz.ratio("Alberto Hernandez Martin", "Alberto Hernandez"))
print(fuzz.ratio("Jeff Goldstein", "Jeff Bloomberg"))
print(fuzz.ratio("Martin Luther King, Jr.", "King Jr., Martin Luther"))



list1 = "John Smith", "Garnish Lemon", "Johny Boy", "Martin Luther King, Jr.", "Jeff Bloomberg"
list2 = "John Smith Jr.", "Garnish The Lemon", "Johny Good Boy", "King Jr., Martin Luther", "Jeff Goldstein"
dicReturn = {}
poorMatches = []

for i in list1:
    highest = 0;
    best_match_list2 = ""
    for j in list2:
        if(fuzz.ratio(i,j) > highest):
            print("changed to " + i +" matched with" + j)
            highest = fuzz.ratio(i,j)
            best_match_list2 = j
    dicReturn[i] = best_match_list2
    if(highest <=70):
        poorMatches.append(i + " has a poor match with " + best_match_list2)

print(dicReturn)
print(poorMatches)

#%%
