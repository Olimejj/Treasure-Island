define e = Character("Eileen")
# Defining characters in Ren'Py

# Narrator Jim: An older, more mature version of Jim, perhaps in his late teens or early twenties. 
# Better dressed, reflecting maturity and experience. Confident and reflective.
define narrator_jim = Character("Narrator Jim", color="#006400") # Dark green for distinction

# In-Story Jim: A young boy in his early teens, curious and adventurous. 
# Dressed in simpler, practical attire. Naive and actively engaged in the story.
define jim = Character("Jim", color="#0000CD") # Dark blue for the in-story dialogue

# The Old Seaman/Captain: Tall, strong, heavy, nut-brown man with a tarry pigtail and soiled blue coat. 
# Rugged, intimidating with a sabre cut on his cheek. Gruff, commanding, and mysterious.
define captain = Character("Captain", color="#8B0000") # Deep red for a commanding presence

# Jim's Father: Middle-aged, worn out from work at the inn. Gentle demeanor. 
# Submissive and a bit timid, especially around the captain. Practical and concerned about his business.
define father = Character("Father", color="#A52A2A") # Brown for a more subdued personality

# Dr. Livesey: Neat, bright appearance with powdered wig, reflecting higher social status. 
# Intelligent, authoritative, and unflappable. Not intimidated by the captain.
define livesey = Character("Dr. Livesey", color="#228B22") # Forest green for an educated and authoritative role

# Custom Python functions
python:
    def multi_say(speakers, lines):
        for speaker, line in zip(speakers, lines):
            renpy.say(speaker, line)
# The game starts here.

label start:

    #Chapter 1 -----------------------------------------------------------------------------------------
    # Narration by Narrator Jim
    narrator_jim "Squire Trelawney, Dr. Livesey, and the rest of these gentlemen having asked me \
    to write down the whole particulars about Treasure Island, from the beginning to the end, \
    keeping nothing back but the bearings of the island, and that only because there is still \
    treasure not yet lifted, I take up my pen in the year of grace 17__ and go back to the time \
    when my father kept the Admiral Benbow inn and the brown old seaman with the sabre cut first \
    took up his lodging under our roof."

    # Continuing the narration
    narrator_jim "I remember him as if it were yesterday, as he came plodding to the inn door, \
    his sea-chest following behind him in a hand-barrow—a tall, strong, heavy, nut-brown man, \
    his tarry pigtail falling over the shoulder of his soiled blue coat, his hands ragged and scarred, \
    with black, broken nails, and the sabre cut across one cheek, a dirty, livid white. I remember \
    him looking round the cove and whistling to himself as he did so, and then breaking out in that \
    old sea-song that he sang so often afterwards."

    # The Captain's song
    captain "Fifteen men on the dead man's chest— Yo-ho-ho, and a bottle of rum!"

    # Narrator Jim adds more details
    narrator_jim "He sang in the high, old tottering voice that seemed to have been tuned and broken \
    at the capstan bars. Then he rapped on the door with a bit of stick like a handspike that he carried, \
    and when my father appeared, called roughly for a glass of rum."

    # Father and Captain's dialogue
    father "This way, sir."
    captain "This is a handy cove, and a pleasant sittyated grog-shop. Much company, mate?"
    father "No, very little company, the more's the pity."

    # The Captain makes his decision 
    captain "Well, then, this is the berth for me. Here you, matey, he cried to the man who trundled \
    the barrow; bring up alongside and help up my chest. I’ll stay here a bit. I'm a plain man; rum \
    and bacon and eggs is what I want, and that head up there for to watch ships off. What you mought \
    call me? You mought call me captain."

    # Narrator Jim describes the Captain's action
    narrator_jim "As he spoke, he threw down three or four gold pieces on the threshold. 'You can tell \
    me when I’ve worked through that,' he said, looking as fierce as a commander. And indeed bad as his \
    clothes were and coarsely as he spoke, he had none of the appearance of a man who sailed before the \
    mast, but seemed like a mate or skipper accustomed to be obeyed or to strike."

    # Narrator Jim offers more insight into the Captain's character
    narrator_jim "The man who came with the barrow told us the mail had set him down the morning before \
    at the Royal George, that he had inquired what inns there were along the coast, and hearing ours well \
    spoken of, I suppose, and described as lonely, had chosen it from the others for his place of residence. \
    And that was all we could learn of our guest."

    #` Narrator Jim reflects on the Captain's habits
    narrator_jim "He was a very silent man by custom. All day he hung round the cove or upon the cliffs \
    with a brass telescope; all evening he sat in a corner of the parlour next the fire and drank rum \
    and water very strong. Mostly he would not speak when spoken to, only look up sudden and fierce and \
    blow through his nose like a fog-horn; and we and the people who came about our house soon learned to let him be."

    # Jim talks about the Captain's inquiries
    narrator_jim "Every day when he came back from his stroll he would ask if any seafaring men had gone by along the road. \
    At first we thought it was the want of company of his own kind that made him ask this question, but at last, \
    we began to see he was desirous to avoid them."

    # Jim's personal experience with the Captain
    narrator_jim "When a seaman did put up at the Admiral Benbow, as now and then some did, making by the coast road for Bristol, \
    he would look in at him through the curtained door before he entered the parlour; and he was always sure to be as silent as a mouse \
    when any such was present. For me, at least, there was no secret about the matter, for I was, in a way, a sharer in his alarms."

    # Narrator Jim describes a frightening figure in his dreams
    narrator_jim "How that personage haunted my dreams, I need scarcely tell you. On stormy nights, \
    when the wind shook the four corners of the house and the surf roared along the cove and up the cliffs, \
    I would see him in a thousand forms, and with a thousand diabolical expressions."

    # Jim's fear grows with each sighting
    narrator_jim "Now the leg would be cut off at the knee, now at the hip; now he was a monstrous kind \
    of a creature who had never had but the one leg, and that in the middle of his body. To see him leap \
    and run and pursue me over hedge and ditch was the worst of nightmares."

    # The toll it takes on Jim
    narrator_jim "And altogether I paid pretty dear for my monthly fourpenny piece, in the shape of these \
    abominable fancies. But though I was so terrified by the idea of the seafaring man with one leg, \
    I was far less afraid of the captain himself than anybody else who knew him."

    # Narrator Jim reflects on the impact of the Captain's presence
    narrator_jim "There were nights when he took a deal more rum and water than his head would carry; \
    and then he would sometimes sit and sing his wicked, old, wild sea-songs, minding nobody; but sometimes \
    he would call for glasses round and force all the trembling company to listen to his stories or bear a chorus to his singing."

    # Jim describes the fear the Captain instilled
    narrator_jim "Often I have heard the house shaking with 'Yo-ho-ho, and a bottle of rum,' all the neighbours \
    joining in for dear life, with the fear of death upon them, and each singing louder than the other to avoid remark."

    # The Captain's dominance during his fits
    narrator_jim "For in these fits he was the most overriding companion ever known; he would slap his hand on the table for \
    silence all round; he would fly up in a passion of anger at a question, or sometimes because none was put, and so he judged \
    the company was not following his story."

    # Narrator Jim on the Captain's Terrifying Tales
    narrator_jim "His stories were what frightened people worst of all. Dreadful stories they were—about hanging, \
    and walking the plank, and storms at sea, and the Dry Tortugas, and wild deeds and places on the Spanish Main. \
    By his own account, he must have lived his life among some of the wickedest men that God ever allowed upon the sea."

    # The Effect on the Inn and Jim's Father
    narrator_jim "My father was always saying the inn would be ruined, for people would soon cease coming there \
    to be tyrannized over and put down, and sent shivering to their beds; but I really believe his presence did us good."

    # Jim Observes the Captain's Influence on the Younger Men
    narrator_jim "People were frightened at the time, but on looking back they rather liked it; it was a fine excitement \
    in a quiet country life, and there was even a party of the younger men who pretended to admire him, calling him a \
    'true sea-dog' and a 'real old salt' and such like names, and saying there was the sort of man that made England terrible at sea."


    return
