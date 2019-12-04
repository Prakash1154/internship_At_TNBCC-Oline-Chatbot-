from pymongo import MongoClient
def getvalue(a):
    client=MongoClient()
    db=client["chatbot"]
    collection=db["botdetails"]
    l={"Hi":"Hello" ,
    "How are you?":"Fine",
    "How do you do?":"Very well",
    "It has been a long time after our last meet":"yes,That's right",
    "It's nice to see after a long time":"yes ofcourse",
    "It's very shocking to see you in this fear":"I came here to accompany my cousin's family since they don't know this place",
    "Why did you come here?":" My family compelled me to join them. So, I am here with them.",
    "Wait. Did you get married?":"No. I am not older to get married.",
    "I am going to have the giant wheel ride. Will you join me?":"No, I'm not interested.",
    "Where are your family? Let me meet them.":"I don't know where they are.",
    "What are you doing?":"I'm currently studying B.Tech of Mechanical Engineering.",
    "Oh! That sounds cool. and you?":"I am studying in BBM.",
    "That's fantastic.":"hmmmm.",
    "ok lets talk about future pla":"sure why not",
    "After B-tech what's your plan":"right now 1st i'm thinking about a good job.",
    "Ooo that nice":"hmmm.",
    "but after job  ":"after job i am thinking about preparation of GRE with job together",
    "That nice":"i know but it not so easy",
    "ok tell me what about your future plaining":"i only searching a good job ",
    "that a good":"yes",
    "My dad is calling.we talk later":"ok",
    "Byee see you soon":"Ok byee"
    }
    #collection.insert(l)
    #res=collection.find({},{"a":1})
    x=l[a]
    return x
