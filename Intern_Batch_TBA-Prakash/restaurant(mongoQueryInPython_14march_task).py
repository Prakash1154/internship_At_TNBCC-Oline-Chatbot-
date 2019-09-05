from pymongo import MongoClient
client=MongoClient()
db=client["hotel1"]
collection=db["restaurants"]
l1={"address": {"building": "1007", "coord": [-73.856077, 40.848447], "street": "Morris Park Ave", "zipcode": "10462"}, "borough": "Bronx", "cuisine": "Bakery",
    "grades": [{"date": {"date": 1393804800000}, "grade": "A", "score": 2}, {"date": {"date": 1378857600000}, "grade": "A", "score": 6},
               {"date": {"date": 1358985600000}, "grade": "A", "score": 10}, {"date": {"date": 1322006400000}, "grade": "A", "score": 9},
               {"date": {"date": 1299715200000}, "grade": "B", "score": 14}], "name": "Morris Park Bake Shop", "restaurant_id": "30075445"
,"address1": {"building": "469", "coord": [-73.961704, 40.662942], "street": "Flatbush Avenue", "zipcode": "11225"}, "borough": "Brooklyn", "cuisine": "Hamburgers",
    "grades": [{"date": {"date": 1419897600000}, "grade": "A", "score": 8}, {"date": {"date": 1404172800000}, "grade": "B", "score": 23},
               {"date": {"date": 1367280000000}, "grade": "A", "score": 12}, {"date": {"date": 1336435200000}, "grade": "A", "score": 12}],
    "name": "Wendy'S", "restaurant_id": "30112340"
,"address2": {"building": "351", "coord": [-73.98513559999999, 40.7676919], "street": "West   57 Street", "zipcode": "10019"}, "borough": "Manhattan", "cuisine": "Irish", "grades": [{"date": {"date": 1409961600000}, "grade": "A", "score": 2}, {"date": {"date": 1374451200000}, "grade": "A", "score": 11}, {"date": {"date": 1343692800000}, "grade": "A", "score": 12}, {"date": {"date": 1325116800000}, "grade": "A", "score": 12}], "name": "Dj Reynolds Pub And Restaurant", "restaurant_id": "30191841"
,"address3": {"building": "2780", "coord": [-73.98241999999999, 40.579505], "street": "Stillwell Avenue", "zipcode": "11224"}, "borough": "Brooklyn", "cuisine": "American ", "grades": [{"date": {"date": 1402358400000}, "grade": "A", "score": 5}, {"date": {"date": 1370390400000}, "grade": "A", "score": 7}, {"date": {"date": 1334275200000}, "grade": "A", "score": 12}, {"date": {"date": 1318377600000}, "grade": "A", "score": 12}], "name": "Riviera Caterer", "restaurant_id": "40356018"
,"address4": {"building": "97-22", "coord": [-73.8601152, 40.7311739], "street": "63 Road", "zipcode": "11374"}, "borough": "Queens", "cuisine": "Jewish/Kosher", "grades": [{"date": {"date": 1416787200000}, "grade": "Z", "score": 20}, {"date": {"date": 1358380800000}, "grade": "A", "score": 13}, {"date": {"date": 1343865600000}, "grade": "A", "score": 13}, {"date": {"date": 1323907200000}, "grade": "B", "score": 25}], "name": "Tov Kosher Kitchen", "restaurant_id": "40356068"
,"address5": {"building": "8825", "coord": [-73.8803827, 40.7643124], "street": "Astoria Boulevard", "zipcode": "11369"}, "borough": "Queens", "cuisine": "American ", "grades": [{"date": {"date": 1416009600000}, "grade": "Z", "score": 38}, {"date": {"date": 1398988800000}, "grade": "A", "score": 10}, {"date": {"date": 1362182400000}, "grade": "A", "score": 7}, {"date": {"date": 1328832000000}, "grade": "A", "score": 13}], "name": "Brunos On The Boulevard", "restaurant_id": "40356151"
}
collection.insert(l1)
#qn(1)Query to display all the documents in the collection restaurants.
for x in collection.find():
    print(x)
    print("")
#qn(2)Query to display the fields restaurant_id, name, borough and cuisine for all the documents in the collection restaurant.
for i in collection.find({},{restaurant_id:1,"name":1,"borough":1,"cuisine":1}):
    print(i)
    print("")
#qn(3)Query to display the fields restaurant_id, name, borough and cuisine,but exclude the field _id for all the documents in the collection restaurant.
for i in collection.find({},{"restaurant_id":1,_id:0,"name":1,"borough":1,"cuisine":1}):
    print(i)
    print("")
#qn(4)Query to display the fields restaurant_id, name, borough and zip code,but exclude the field _id for all the documents in the collection restaurant.
for i in collection.find({},{address.zipcode:1,"restaurant_id":1,_id:0,"name":1,"borough":1}):
    print(i)
    print("")
#qn(5) Query to display all the restaurant which is in the borough Bronx.
for i in collection.find({"borough": "Bronx"}):
    print(i)
    print("")
#qn(6)  Query to find the restaurants who achieved a score more than 90
for i in collection.find({grade:{"Score":{gt:90}}}):
    print(i)
    print("")
#qn(7)Query to find the restaurants that achieved a score, more than 80 but less than 100.
for i in collection.find({grade:{"score":{gt:80,lt:100}}}):
    print(i)
    print("")
'''
#qn(8)Write a MongoDB query to find the restaurants which do not prepare any cuisine of 'American ' and achieved a grade point 'A' not belongs to the borough Brooklyn. The document must be displayed according to the cuisine in descending order.
for i in restaurants.find( { and :[  {    "cuisine" : {ne : "American "},"grades.grade" :"A","borough": {$ne : "Brooklyn"}}]}).sort({"cuisine":-1}):
    print(i)
    print("")
    
#qn(9)  Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which contain 'Reg' as three letters somewhere in its name.
for i in restaurants.find({},{"restaurant_id" : 1,"name":1,"borough":1,"cuisine" :1,{"name": /.Reg./}}):
    print(i)
    print("")
'''    
#qn(10)    Write a MongoDB query to find the restaurant Id, name, address and geographical location for those restaurants where 2nd element of coord array contains a value which is more than 42 and upto 52.
for i in restaurants.find({"address.coord.1": {gt : 42, lte : 52}},{"restaurant_id" : 1,"name":1,"address":1,"coord":1}):
    print(i)
    print("")
    
 
NOTE:-sir qn no. 8.9 syntax are not working it gives syntax error.
