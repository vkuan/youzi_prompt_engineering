# Victor Kuan
# March 2024
import time
import random
from csv import writer
from openai import OpenAI
client = OpenAI(api_key="FIND IN GITIGNORE FILE")

ASSISTANT_ID = "asst_2gl87dd4oiz1ezI99H1gngOS"


def generate_convo_starter(vibe, detailed_vibe, subvibe, topic, work_safe, difficulty):
    content_string = ("generate a " + detailed_vibe + " convo starter about something related to " + topic)

    # work_safe = 0 represents safe for work
    # work_safe = 1 represents NFSW
    if (work_safe == 1):
        content_string += ". Feel free to bring up crude or adult-themed topics. "

    # difficulty = 0 represents easy 
    # difficulty = 1 represents hard
    if (difficulty == 0):
        content_string += ". Please mostly use Chinese HSK level 1 or HSK level 2 vocabulary and concepts."
    else:
        content_string += ". Please mostly use Chinese HSK level 2 or HSK level 3 vocabulary and concepts."
    print(content_string)
 
    thread = client.beta.threads.create(
        messages=[
            {
                "role": "user",
                "content": content_string,
            }
        ]
    )

    # Submit thread to the assistant.
    run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=ASSISTANT_ID)
    print(f"👉👉👉 Run Created: {run.id}")

    # Wait for run to finish processing.
    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        print(f"🏃 Running Status: {run.status}")
        time.sleep(1)
    else:
        print(f"🏁🏁🏁 Run Completed!")

    message_response = client.beta.threads.messages.list(thread_id=thread.id)
    messages = message_response.data

    # Print latest conversation starter prompt.
    latest_message = messages[0]
    id = random.randint(2, 100000)
    print(f"💬 Response: {latest_message.content[0].text.value}")
    new_convo_starter_row = [id, latest_message.content[0].text.value, vibe, detailed_vibe, subvibe, topic, work_safe, difficulty]
    with open('test_youzi_prompts.csv', 'a') as f_object:
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
    
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(new_convo_starter_row)
    
        # Close the file object
        f_object.close()

list_of_icebreaking_vibes = ["silly icebreaking vibe", "casual icebreaking vibe", "funny and absurd icebreaking vibe", "profound and thoughtful icebreaking vibe"]
list_of_icebreaking_subvibes = ["daily liao tian", "anecdotes and past lives", "fun hypotheticals", "preferences and hot takes"]
list_of_icebreaking_topics_0 = ["something interesting or weird that you encountered today", "something that you're proud of today", "something that you wanted to do today", "something that made you really happy today"]
list_of_icebreaking_topics_1 = ["something that you really regret that happened in the past", "something interesting or weird that happened during high school", "something that you are really proud of from your childhood", "childhood friends", "weird childhood memories", "childhood fun memories", "memories in college", "childhood personality growth periods"]
list_of_icebreaking_topics_2 = ["hypothetically being an animal", "hypothetically being a Chinese dish", "hypothetically living in Taiwan", "hypothethically living in Asia", "hypothetically owning property in China", "hypothetically being a superhero", "hyothetically getting reunited with an ex partner", "hypothetically getting to eat any sort of food in the world", "hypothetically being able to speak perfect Cantonese or some other Chinese dialect", "hypothetically getting any superpower"]
list_of_icebreaking_topics_3 = ["favorite foods", "favorite relatives", "favorite actors", "favorite sorts of places to visit", "favorite travel destinations", "favorite friends", "favorite memories with friends", "favorite social settings", "favorite places to hangout", "favorite types of Chinese foods", "favorite past times or leisure activites", "favorite state in the United States", "favorite way to waste time"]

def generate_icebreaker_convos():
    curr_vibe = "icebreaker vibe"
    for x in list_of_icebreaking_vibes:
        for y in list_of_icebreaking_subvibes:
            if y == "daily liao tian":
                for z in list_of_icebreaking_topics_0:
                    generate_convo_starter(curr_vibe, x, y, z, 0, 0)
                    generate_convo_starter(curr_vibe, x, y, z, 0, 1)
            elif y == "anecdotes and past lives":
                for z in list_of_icebreaking_topics_1:
                    generate_convo_starter(curr_vibe, x, y, z, 0, 0)
                    generate_convo_starter(curr_vibe, x, y, z, 0, 1)
            elif y == "fun hypotheticals":
                for z in list_of_icebreaking_topics_2:
                    generate_convo_starter(curr_vibe, x, y, z, 0, 0)
                    generate_convo_starter(curr_vibe, x, y, z, 0, 1)
            elif y == "preferences and hot takes":
                for z in list_of_icebreaking_topics_3:
                    generate_convo_starter(curr_vibe, x, y, z, 0, 0)
                    generate_convo_starter(curr_vibe, x, y, z, 0, 1)

list_of_haixiu_vibes = ["silly gossipy vibe", "gossipy vibe", "fun gossipy vibe"]
list_of_haixiu_subvibes = ["spill the tea", "romance", "divulge some juicy secrets", "rant club"]
list_of_haixiu_topics_0 = ["something dramatic that happened to you recently", "something that pissed you off recently", "some drama or gossip happening in your friend group", "some weird drama happening in your life", "some drama happening at your workplace right now", "some bullshit that you're dealing with"]
list_of_haixiu_topics_1 = ["college romance", "college romance regrets", "college dating weird stories", "spicy things that happened during college dating", "funny and absurd college dating stories", "recent dating stories", "recent dating blunders", "missed romance opportunities", "first date stories", "absurd first date stories", "love at first sight", "favorite weird date ideas"]
list_of_haixiu_topics_2 = ["weird secrets you've been holding onto", "funny lighthearted secrets you have", "profound secret", "secret about your friend group", "secret about your lifestyle", "If you were a spy, what would your code name be and why?", "being a liar", "weird lies you've told", "ridiculous secrets you've kept"]
list_of_haixiu_topics_3 = ["something bothering you recently that you want to rant about", "bullshit that you want to rant about", "something pissing you off lately", "something that irrationally irks you", "What's the most ridiculous 'first world problem' you could passionately rant about for hours", "types of people that piss you off", "places that make you weirdly pissed"]

def generate_haixiu_convos():
    curr_vibe = "hai xiu / spicy talk"
    for x in list_of_haixiu_vibes:
        for y in list_of_haixiu_subvibes:
            if y == "spill the tea":
                for z in list_of_haixiu_topics_0:
                    generate_convo_starter(curr_vibe, x, y, z, 0, 0)
                    generate_convo_starter(curr_vibe, x, y, z, 0, 1)
            elif y == "romance":
                for z in list_of_haixiu_topics_1:
                    generate_convo_starter(curr_vibe, x, y, z, 0, 0)
                    generate_convo_starter(curr_vibe, x, y, z, 0, 1)
            elif y == "divulge some juicy secrets":
                for z in list_of_haixiu_topics_2:
                    generate_convo_starter(curr_vibe, x, y, z, 0, 0)
                    generate_convo_starter(curr_vibe, x, y, z, 0, 1)
            elif y == "rant club":
                for z in list_of_haixiu_topics_3:
                    generate_convo_starter(curr_vibe, x, y, z, 0, 0)
                    generate_convo_starter(curr_vibe, x, y, z, 0, 1)

# generate_icebreaker_convos()
# generate_haixiu_convos()

list_of_trauma_vibes = ["profound trauma bonding vibe", "thoughtful trauma bonding vibe", "relaxing trauma bonding vibe"]
list_of_trauma_subvibes = ["ABC childhood trauma bonding", "career trauma bonding", "academics trauma", "romance struggles"]
list_of_trauma_topics_0 = ["something weird that happened during your childhood", "something absurd that happened during your childhood", "something weird that happened with your parents", "weird childhood conflicts", "battles with your siblings", "weird academic pressures that your parents put on you", "weird academic childhood stories", "going to Chinese school in America"]
list_of_trauma_topics_1 = ["something terrible that happened to you at work", "something from work that you want to rant about", "weird stories about your boss at work", "weird coworker flirting stories", "tragic stories from work", "getting rejected from your dream job", "horror stories from your job", "assholes from your office or work"]
list_of_trauma_topics_3 = ["something traumatic that happened with a romantic partner", "something weird that your partner does", "something weird that your partner used to do", "a weird pet peeve you have when dating", "weird trauma from using dating apps", "weird dating app stories", "worst dates you've ever gone on", "weird date stories"]
list_of_trauma_topics_2 = ["something traumatic that happened at school", "weird college trauma", "weird college drama trauma", "weird academic trauma", "weird exam trauma", "SAT bullshit", "parents imposing academic stress", "funny studying trauma", "applying to collge weird stories"]

def generate_trauma_convos():
    curr_vibe = "trauma bonding"
    for x in list_of_trauma_vibes:
        for y in list_of_trauma_subvibes:
            if y == "ABC childhood trauma bonding":
                for z in list_of_trauma_topics_0:
                    generate_convo_starter(curr_vibe, x, y, z, 0, 0)
                    generate_convo_starter(curr_vibe, x, y, z, 0, 1)
            elif y == "career trauma bonding":
                for z in list_of_trauma_topics_1:
                    generate_convo_starter(curr_vibe, x, y, z, 0, 0)
                    generate_convo_starter(curr_vibe, x, y, z, 0, 1)
            elif y == "academics trauma":
                for z in list_of_trauma_topics_2:
                    generate_convo_starter(curr_vibe, x, y, z, 0, 0)
                    generate_convo_starter(curr_vibe, x, y, z, 0, 1)
            elif y == "romance struggles":
                for z in list_of_trauma_topics_3:
                    generate_convo_starter(curr_vibe, x, y, z, 0, 0)
                    generate_convo_starter(curr_vibe, x, y, z, 0, 1)


# generate_trauma_convos()

list_of_media_vibes = ["interesting Chinese media vibe", "interesting Taiwanese and Hong Kong media vibe", "fun Chinese and Taiwanese media vibe"]
list_of_media_subvibes = ["Songs", "TV Shows & Movies", "News and Current Events", "News and Current Events"]
list_of_media_topics_0 = ["favorite Chinese singers", "favorite Taiwanese singers", "parents' favorite singers", "music that makes you dance", "music that you study to", "weird music", "favorite genres of music", "Jay Chou", "listening to Chinese music", "understanding Chinese music", "recent popular must-listen Chinese music"]
list_of_media_topics_1 = ["favorite Chinese TV shows", "favorite Chinese movies", "Wong Kar Wai", "favorite Chinese movie of all time", "favorite Chinese movie star of all time", "favorite Taiwanese movie star ever", "Chinese historical dramas", "weirdest Chinese movie or show you've seen", "Chinese movies or TV shows that have taught you something", "funniest Chinese productions", "what sort of movie would you like to star in", "Chinese comedy works"]
list_of_media_topics_2 = ["do your parents keep up with Chinese or Taiwanese politics", "current Chinese politics", "travelling to Taiwan recently", "travelling to China recently", "Are you familiar with any major infrastructure projects currently underway in Taiwan", "new Chinese infrastruture news", "news about Huawei, Xiaomi, and other Chinese tech", "Chinese companies vs. Apple and Google", "Chinese employment news", "what are your views on Taiwan", "what are your views on Hong Kong", "Hong Kong news", "new EV cars in China", "cool new Chinese inventions"]
list_of_media_topics_3 = ["favorite Chinese celeb", "weirdest Chinese celebs", "favorite Taiwanese or Hong Kong celebs", "which Chinese celeb would you like to hypothetically see in a Hollywood production", "do you have a crush on any Chinese celebrity", "have you ever seen a Chinese celeb in person (like at a concert or something)", "following Chinese celebs on Instagram or TikTok", "hottest Taiwanese celebs", "funniest Chinese celebs", "hottest Chinese celebs"]

def generate_media_convos():
    curr_vibe = "Chinese media"
    for x in list_of_media_vibes:
        for y in list_of_media_subvibes:
            # if y == "Songs":
            #     for z in list_of_media_topics_0:
            #         generate_convo_starter(curr_vibe, x, y, z, 0, 0)
            #         generate_convo_starter(curr_vibe, x, y, z, 0, 1)
            # elif y == "TV Shows & Movies":
            #     for z in list_of_media_topics_1:
            #         generate_convo_starter(curr_vibe, x, y, z, 0, 0)
            #         generate_convo_starter(curr_vibe, x, y, z, 0, 1)
            # if y == "News and Current Events":
            #     for z in list_of_media_topics_2:
            #         generate_convo_starter(curr_vibe, x, y, z, 0, 0)
            #         generate_convo_starter(curr_vibe, x, y, z, 0, 1)
            if y == "News and Current Events":
                for z in list_of_media_topics_3:
                    generate_convo_starter(curr_vibe, x, y, z, 0, 0)
                    generate_convo_starter(curr_vibe, x, y, z, 0, 1)



generate_media_convos()
generate_icebreaker_convos()
generate_haixiu_convos()
generate_trauma_convos()

# for x in range(1, 10): 
#     generate_convo_starter("profound", "interesting childhood memories")

# for x in range(1, 10): 
#     generate_convo_starter("spicy", "your deepest darkest secrets")


# example tester of generate_convo_starter
for x in range(1, 3): 
    generate_convo_starter("silly and funny", "test", "hypothetically what you would do if you met the most attractive person of all time", 1, 1)


# Vibes brainstorming / reference
# Icebreaking / Liao Tian:
# “Daily chat” (can’t be too vanilla, don’t need the app to do that)
# ie did you do anything interesting today
# “Tell me about your past”
# ie immigration story similar to parents are human
# Hypothetical talk (fun talk)
# -  ie if you were a Chinese dish, what would you be?
# Preference 
# - ie your favourite food
# 		Fun facts (about me)
# - ie whos the most memorable stranger you’ve met
# etc 

# Hai xiu / Spicy:
# “School gossip” 
# ie did you have any friendship dramas during college
# “Crush gossip”
# ie what’s the weirdest thing you’ve ever done to convey love to your crush
# “Ranting”
# ie whats your complaints 
# “Lighthearted secret”
# Ie what your 
# etc

# Trauma bonding:
# Childhood
# Career 
# School
# Romance
# - ie toxic ex
# etc

# Media:
# Songs 
# TV shows/Movies
# News/Current events
# Celebrities
# etc
