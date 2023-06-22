define t = Character("Thomas")
define n = Character("Nigel")
define nu = Character("???")
define es = Character("Soldier")
define du = Character("Nigel's mom")
define d = Character("Delia")
define tr = Character("Training robot")
define sk = Character("Shopkeeper")
define lg = Character("Lagouga")
define sfu = Character("???")
define sf = Character("Serfopo")
define zgu = Character("???")
define zg = Character("Zagingagin")
define eow = Character("Eye Of Warns")
define vx = Character("Vyxi")

define audio.musplaceholder = "audio/music/placeholder_music.mp3"
define audio.musambience = "audio/music/a_very_unfamiliar_place.mp3"
define audio.musbattle = "audio/music/fighting_a_common_enemy.mp3"
define audio.musgameover = "audio/music/theres_still_hope.mp3"
define audio.sndplaceholder = "audio/sounds/placeholder_sound.mp3"


label start:

    scene bg door

    play music musambience

    "You woke up in a strange place and have no idea where you are."

    "You see a door next to you, and you feel like entering it."

    "You enter..."

    scene bg weird place
    with fade

    "You ended up in a really strange place, the door behind you disappeared"

    show thomas confused

    t "Ugh, where am i?"

    t "What the hell is this place?"

    t "I don't think i should've entered that door..."

    hide thomas confused

    "You hear the footsteps"

    play sound sndplaceholder

    show thomas scared

    menu:

        t "Oh god, what should i do?"

        "Look around":

            jump lookaround

        "Run away":

            jump runaway


label runaway:

    hide thomas scared

    "You ran away."

    "But then, you realize that you have nowhere to run."

    menu:

        "..."

        "Look around":

            jump lookaround


label lookaround:

    hide thomas scared

    show thomas confused arms

    t "Who are you?"

    hide thomas confused arms

    "As the figure gets closer, it reveals itself"

    stop music

    show nigel smug
    with dissolve

    nu "Hey, are you from the Super Outer World?"

    hide nigel smug

    show thomas neutral

    t "What do you mean Super Outer World?"

    hide thomas neutral

    show nigel smug

    nu "There are some realms existing - From Super Inner to Super Outer Worlds. You're most likely from the Super Outer World."

    nu "One of the ways to get to the Inner World is by entering the door in the Realms Corridor."

    hide nigel smug

    show thomas neutral arms

    t "That's what exactly i did. By the way, what's your name?"

    hide thomas neutral arms

    show nigel happy arms

    n "The name's Nigel, what about you?"

    t "Th.. Thomas."

    hide nigel happy arms

    show nigel happy talking

    n "Nice to meet you, Thomas, and welcome to the Inner World!"

    hide nigel happy talking

    show thomas happy talking

    t "Thanks. Where should we go?"

    hide thomas happy talking

    show soldier

    play music musbattle

    es "Nowhere!!"

    hide soldier

    show thomas surprised

    t "Who are you and why are you here?"

    hide thomas surprised

    show soldier

    "They prefer not to talk about it"

    n "It's a soldier from the Inner World Abyssal Kingdom. They're the most common in the military, as they don't show a big genuine threat."

    t "But i don't have any weapons!"

    menu:
    
        t "Now, what do i need to do..."

        "Trick the soldier":

            jump soldierbattletrick

        "Attack the soldier immediately":

            jump soldierbattleinstattack


label soldierbattletrick:

    hide soldier

    show thomas happy talking

    t "Hey, there are your friends' airship in the sky!"

    hide thomas happy talking

    show soldier

    es "Where?"

    menu:

        "The soldier is trick. What should Thomas do?"

        "Attack":

            jump soldierbattleattack

        "Sneak behind and then attack":

            jump soldierbattleinstattack


label soldierbattleattack:

    es "Haha, i saw it!"

    "Soldier punches Thomas so hard that he fainted."

    stop music

    play music musgameover

    "GAME OVER"

    return


label soldierbattleinstattack:

    hide soldier

    show thomas angry

    t "Now take this!"

    hide thomas angry

    "The soldier dodged"

    show soldier

    es "Hah, you missed!"

    "The soldier attacks Thomas back"

    menu:
    
        "Do the action"

        "Attack again":

            jump soldierbattleanotherattack

        "Dodge":

            jump soldierbattledodge


label soldierbattleanotherattack:

    es "Hah, you're weak!"

    "The soldier punched Thomas, and he fainted."

    stop music

    play music musgameover

    "GAME OVER"

    return


label soldierbattledodge:

    hide soldier

    "You dodge and snuck behind to kick him"

    show thomas happy

    t "Take this!"

    hide thomas happy

    "As Thomas kicked Soldier, he fell down the hill and damaged his armor."

    show nigel happy talking

    n "Great job Thomas!"

    hide nigel happy talking

    show thomas happy talking

    t "Thanks!"

    hide thomas happy talking

    stop music

    "YOU WON!"

    scene bg hills n characters
    with dissolve

    "For hours, our heroes Thomas and Nigel were getting to Begler Village without eating and sleeping."

    "Every step on the ground was making them feel anxious."

    t "Damn it, i'm feeling so tired!"

    n "Be patient, Thomas, we're almost close."

    t "But i haven't ate my Oreos yet!"

    n "Oreos? What are these?"

    t "Well, it's some sort of dark tasty cookies with a milk-flavored thingy in it."

    t "Someone even invented a weird way to taste it, like opening it, licking the ''milk'' thing and then dip it into the milk bottle."

    t "I eat it in a normal way."

    n "Wow, these are pretty interesting. You see, Inner World differs from the Super Outer World in many aspects, including food."

    n "We have cookies too, but they're quite different."

    t "Nice."

    "And then, they finally reached it.."

    scene bg nigels house
    with fade

    n "This is where i live."

    t "That's a pretty nice looking house. Is this fine if i enter and sleep in there for a while?"

    n "As long as my family won't mind it."

    n "Hey mom, is this okay if this person spends his night in our house?"

    du "He looks like a person from the Super Outer World. Is he nice?"

    n "Yes, i just met him, and i'm helping him to find the way back. You know it's hard to escape the Inner World."

    du "Well, in that case, he may."

    t "Yay, thank you miss!"

    n "Let's go Thomas, i'll show you where is where in this house."

    "And then, they went home."

    scene bg black
    with dissolve

    "Nigel's mom revealed her name, and it's Delia."

    "She has given chicken strips to Thomas and trained him to be stronger."

    "Soon, everyone went to sleep."

    d "Goodnight Thomas, goodnight Nigel!"

    n "Goodnight mom.."

    t "Goodnight Mrs. Xaqqa."

    "Everyone slept well, except Thomas..."

    scene bg thomas waking up
    with fade

    "Some strange sounds that sound like tinkering kept Thomas up for 15 minutes straight..."

    scene bg thomas sleeping

    "...until he fell asleep again..."

    scene bg black

    "Next morning, a few hours later until it's afternoon. Thomas needs to continue his training"

    scene bg nigels house day
    with dissolve

    show nigel happy talking
    
    n "Are you ready Thomas?"

    hide nigel happy talking

    show thomas happy talking

    t "As always!"

    hide thomas happy talking

    show delia worried

    d "Be careful!"

    hide delia worried

    show thomas happy arms

    t "Don't worry, i will!"

    hide thomas happy arms

    show delias training robot

    tr "Greetings, user. Please say your name."

    t "Thomas Throndsen..."

    tr "Great. Now, Thomas Throndsen, allow me to introduce myself!"

    tr "I'm a training robot created by Delia Xaqqa for the obvious purposes - to train everyone that need it."

    menu:
    
        tr "Are you prepared? (Don't forget to save before leaving.)"

        "Yes":

            jump trainingstart

        "No":

            jump trainingrefusing


label trainingrefusing:

    tr "It's fine if you don't want to."

    tr "Come back when you're ready!"

    return


label trainingstart:

    tr "Great! Now let's get to training!"

    tr "Step 1: When you feel that the enemy will attack you, just simply dodge!"

    tr "Now get ready. 3."

    tr "2."

    menu:

        tr "1!"

        "Dodge":

            jump trainingdodge

        "Don't dodge":

            jump trainingdontdodge


label trainingdontdodge:

    "The robot punches you."

    menu:

        "Try again?"

        "Yes":

            jump trainingstart

        "No":

            jump gameover


label gameover:

    "GAME OVER"

    return


label trainingdodge:

    "The robot punches you."

    "But you dodge."

    tr "Great job, Thomas, you have good reactions!"

    tr "Step 2: Attack at the perfect timing."

    tr "Since you're ready to attack..."

    menu:

        tr "Do it!"

        "Attack":

            jump trainingattack

        "Don't attack":

            jump trainingdontattack


label trainingdontattack:


    tr "Please attack."

    menu:

        "..."

        "Attack":

            jump trainingattack

        "Don't attack":

            jump trainingdontattack


label trainingattack:


    "You punch a robot."

    tr "What a nice punch! Don't worry, i don't get injured even from the strong attacks."

    tr "Step 3: During the battle, thing about preferences."

    tr "When you think it's a perfect time to be done, you can settle the peace, or choose violence instead."

    hide delias training robot

    show thomas scared

    t "I don't think i will have to choose violence. I don't need to fight everyone, except the soldier that i already defeated yesterday."

    t "My only purpose is just to get to my world as soon as possible."

    t "So i will choose peace only.."

    hide thomas scared

    show delias training robot

    tr "That's a wise choice, Thomas. But remember."

    tr "Being too kind all the time doesn't help you either, so in the tough situations, stay neutral."

    t "I understand. Thank you for the advice."

    hide delias training robot
    with fade

    scene bg black
    with fade

    "YOU WON!"

    scene bg nigels house day
    with dissolve

    show delias training robot
    with dissolve

    tr "Fantastic job Thomas! I see that you're ready for the new adventures awaiting!"

    hide delias training robot

    "Delia turned off the robot"

    show delia happy talking

    d "Very nice, Thomas!"

    d "Looks like you're ready!"

    hide delia happy talking

    show thomas happy

    t "Thank you Mrs. Xaqqa. But is there any way to get home very fast? Like, can you invent a machine?"

    hide thomas happy

    show delia neutral talking

    d "Unfortunately, i can't, it's too impossible for me. The only known way possible is by placing a Dimensional Pearl on the Dark Matter Table."

    hide delia neutral talking

    show thomas confused

    t "Thank you for the advice, but where can i find both of these?"

    hide thomas confused

    show delia neutral

    d "Well, you can find the pearl in Zorgin's cave in the Outer World, and you can find the Dark Matter Table in Super Inner World's kingdom castle."

    hide delia neutral

    show delia worried

    d "But be careful, both of these places are dangerous, and i don't want any of you to be hurt!"

    hide delia worried

    show nigel happy talking

    n "Don't worry, mom, i'll make sure me and Thomas will stay safe!"

    hide nigel happy talking

    show nigel neutral arms

    n "If i could only ask Serfopo if he joined us."

    hide nigel neutral arms

    show delia very happy

    d "Great! And when you come back home, Nigel, i will make a lettuce pie for us all!"

    hide delia very happy
    
    show delia worried

    d "Except you, Thomas, sorry, since you're going back to your world."

    hide delia worried

    show thomas happy

    t "Don't worry, Mrs Xaqqa, i'm not really into lettuce. But i still accept your kindness."

    t "Well, i'm heading. Bye Mrs Xaqqa!"

    hide thomas happy

    show delia happy

    d "Bye Thomas, bye Nigel!"

    n "Bye mom!"

    hide delia happy

    scene bg black
    with dissolve

    "And then, Thomas and Nigel went to the shop first."

    scene bg shop

    show shopkeeper smug

    sk "Heya kiddos, what do you want to buy?"

    n "I want to buy at least something for my new acquaintance Thomas."

    sk "Oh, how about a dagger?"

    t "I'd better have boxing gloves."

    sk "Oh, you prefer it a sporty way? It worths 149 Raiguls"

    n "Sure!"

    hide shopkeeper smug

    "Nigels buys a pair of boxing gloves for Thomas."

    show shopkeeper confident

    "That was a nice deal! Come back when you have any time!"

    scene bg shop n forest

    hide shopkeeper confident

    n "Well, i wonder when you will try them out."

    t "I guess now.."

    show lagouga

    "The fierce Lagouga has appeared!"

    menu:

        "Thomas' turn."

        "Punch":

            jump lagougathomaspunch

        "Kick":

            jump lagougakick


label lagougakick:

    "Thomas kicked Lagouga's body."

    "lagouga's turn."

    "Lagouga reflected Thomas' kick."

    "Thomas fainted."

    menu:
    
        "Nigel's turn."

        "Punch":

            jump lagouganigelpunch

        "Stab":

            jump lagougastab


label lagouganigelpunch:

    "Nigel punched Lagouga in the face."

    "Lagouga's turn."

    "Since Nigel didn't have the gloves like Thomas does, Lagouga ignored his attacks and reflected them."

    "Nigel fainted."

    "GAME OVER"

    return


label lagougastab:

    "Nigel stabbed lagouga in the chest."

    hide lagouga

    "Lagouga perished."

    "YOU WON!"

    scene bg black

    "Gladly, Nigel has some medicine to heal Thomas' hurt places."

    scene bg shop n forest

    show nigel worried

    n "Are you feeling better now, Thomas?"

    t "Yeah, i am, thank you pal."

    t "Without you, i would just be laid down on the ground screaming in pain."

    hide nigel worried

    show nigel happy

    n "You're welcome, buddy!"

    hide nigel happy

    jump storycontinuation


label lagougathomaspunch:

    "Thomas punched Lagouga in the face."

    hide lagouga

    "The power of boxing gloves pushed Lagouga to the tree nearby."

    "YOU WON!"

    show thomas happy talking

    t "Whoa, the gloves really work!"

    show nigel happy

    n "Yes! I think you need to keep it as your main weapon!"

    hide nigel happy

    jump storycontinuation


label storycontinuation:

    show nigel happy talking

    n "Anyways, since Serfopo lives too far from here, we'll have to spend much time on reaching his house."

    n "The shortest way is by crossing the forest."

    hide nigel happy talking

    show thomas happy talking

    t "Interesting. If there can be more enemies like these, i'll deal with them using my new boxing gloves!"

    hide thomas happy talking

    scene bg forest
    with fade

    "Thomas and Nigel entered the forest."

    "The sounds of trees leaves dissipating in the wind and sparrows chirping give them a relaxing feeling."

    "However, it's quite too, since they're the only people in the entrance."

    "Until in one moment, they encounter..."

    show soldier

    "...another soldier!"

    menu:
    
        "Thomas' turn"

        "Punch":

            jump soldiertwopunch

        "Kick":

            jump soldierkick


label soldierkick:

    "Thomas kicks the soldier."

    "But it dodges."

    "Soldier's turn."

    menu:

        "Soldier punches Thomas."

        "Dodge":

            jump soldiertwododge

        "Punch":

            jump soldiertwopunch


label soldiertwododge:

    "Thomas dodges the soldier's punch."

    menu:

        "Nigel's turn."

        "Punch":

            jump soldiertwopunchnigel

        "Stab":

            jump soldierstab


label soldiertwopunchnigel:

    "Nigel punches tgh soldier."

    hide soldier

    "The soldier faints!"

    jump soldiervictory


label soldierstab:

    "Nigel stabs the soldier."

    hide soldier

    "The soldier perishes!"

    jump soldiervictory


label soldiertwopunch:

    "Thomas punches the soldier."

    hide soldier

    "The soldier faints!"

    jump soldiervictory


label soldiervictory:

    "YOU WON!"

    show nigel happy arms

    n "That was pretty interesting!"

    hide nigel happy arms

    show thomas happy arms

    t "Yeah, i agree! Fighting these soldiers is way easy with these gloves!"

    hide thomas happy arms

    scene bg black
    with fade

    "As Thomas and Nigel were going as far as possible in the forest, they started thinking that they got lost."
    scene bg forest
    with fade

    show thomas scared

    t "Oh god, we're lost! Do you have a map?"

    hide thomas scared

    show nigel worried

    n "Unfortunately, i don't have it."

    hide nigel worried

    show thomas angry

    t "Why didn't you get it?"

    hide thomas angry

    show nigel worried

    n "Because there aren't any, sadly.."

    hide nigel worried

    show thomas confused

    t "Damn it, we need to find the way to Serfopo's house!"

    hide thomas confused

    show nigel happy

    n "Calm down Thomas, i think it should be right th-"

    hide nigel happy

    "As Nigel was going through, he tripped on a tree root and fell down the hole that has been dug since a while ago."

    show thomas talking

    t "Nigel? Where are-"

    hide thomas talking

    show thomas scared

    t "He fell in the hole!"

    t "I gotta get there to save him!"

    hide thomas
    with dissolve

    "However, the hole disappears, and Thomas, panicking, runs all over the forest to find Nigel."

    "Sometimes, Thomas would feel tired, so he had to drink water before continuing."

    "Encountering many Lagougas in his way, Thomas found a particular one..."

    show lagouga

    lg "Wohoho!! You're trying to find your friend? Well, you won't!"

    hide lagouga

    show thomas angry

    t "Where is Nigel?! Tell me now!!"

    hide thomas angry

    show lagouga

    lg "I refuse to give information!"

    hide lagouga

    show thomas mad

    t "Ughh, i'll show you!"

    "Thomas punches Lagouga."

    "But it's not getting kicked."

    hide thomas mad

    show thomas confused arms

    t "Wait, how are you not getting hit?"

    hide thomas confused arms

    show lagouga

    lg "I'm covered in Zingo Oil that ignores any attacks, so i guess i'm safe now, hah!"

    menu:

        "There's only one choice..."

        "Kick":

            jump lagougakickx


label lagougakickx:

    "Thomas kicks Lagouga"

    hide lagouga

    "It reflects Thomas' quick and pushes him off"

    "Thomas gets heavily injured."

    "Does that mean he should give up?.."

    show thomas injured

    t "Maybe you are strong, but i'm sure Nigel will come back and defeat you..."

    hide thomas injuted

    show lagouga

    lg "There's no way to get hit when you're covered in Zi-"

    hide lagouga

    "A burning rock hits Lagouga's back of his head."

    "Lagouga gets burned to ashes."

    "YOU WON!! Except it wasn't you..."

    show thomas injured

    t "W-wait.. Nigel, is t-that you?.."

    hide thomas injured

    sfu "No, i'm not Nigel, but rather his good old friend! Here, take this!"

    "A mysterious stranger gives Thomas a healing potion."

    "Thomas drinks it."

    show thomas happy

    t "Thank you!"

    hide thomas happy

    show thomas confused

    t "But who are you?"

    hide thomas confused

    sfu "You're welcome! And i'm none other than..."

    show serfopo smug

    sf "...Serfopo!"

    hide serfopo smug

    show thomas happy talking

    t "Wow! So you're that guy that Nigel looks for!"

    hide thomas happy talking

    show serfopo happy

    sf "Yeah, that's me! But where's Nigel?"

    hide serfopo happy

    show thomas neutral arms

    t "I don't know, but he tripped and fell somewhere, and i can't find him!"

    hide thomas neutral arms

    show serfopo neutral

    sf "I know where is it!"

    hide serfopo neutral

    show serfopo happy talking

    sf "Follow me!"

    hide serfopo happy talking
    
    "Meanwhile, a few minutes later..."

    scene bg lair room
    with fade

    "Nigel has his problems too..."

    show lagouga
    
    lg "You should eat it."

    hide lagouga

    show nigel scared

    n "No, i hate bilgeging, it tastes worse than an expired potato!"

    hide nigel scared

    show lagouga

    lg "I cannot accept your refusing. It's time to-"

    hide lagouga

    "Another lagouga gets hit by a burning rock."

    show serfopo smug

    sf "I'm finally here!"

    hide serfopo smug

    show nigel happy talking

    n "Serfopo, you finally found me! But how?"

    hide nigel happy talking

    show serfopo smug

    sf "Me and Thomas entered the Lagouga Lair and then looked for your room until we found you shouting."

    hide serfopo smug

    show thomas happy arms

    t "Come on, let's get out of here!"

    hide thomas happy arms

    scene bg forest
    with dissolve

    "Our heroes left Lagouga's Lair, with killing a few Lagougas in the way."

    show serfopo happy

    sf "Let's go to my house and rest there for a while!"

    sf "My family knows where my great grandma lives."

    sf "She lives next to the portal to the Outer World, which can lead to Zorgin's cave!"

    hide serfopo happy

    show serfopo neutral

    sf "But it's too far away from here."

    hide serfopo neutral

    show thomas happy
    
    t "No matter what, we will still get here!"

    hide thomas happy

    scene bg black
    with dissolve

    "3 hours later"

    "After a long walking, the traveler Thomas, alongst with his new acquaintances Nigel and Serfopo reached the Swamp of Kruzcenkk."

    scene bg swamp
    with fade

    show thomas disgusted

    t "Eugh, this place smells!"

    hide thomas disgusted

    show serfopo derp

    sf "a"

    hide serfopo derp

    show nigel neutral

    n "Concentrate, guys! If we won't reach Qza Wolqekc, we're gonna get doomed!"

    hide nigel neutral

    show thomas disgusted

    t "I'm trying, but i can't!"

    hide thomas disgusted

    show serfopo derp

    sf "I'm a Barbie Girl, in the Barbie world life in plastic, it's fantastic!"

    hide serfopo derp

    show nigel neutral arms

    n "Come on, be serious!"

    hide nigel neutral arms
    
    show serfopo derp

    sf "Fine, i'll try..."

    hide serfopo derp

    show soldier

    es "Give up!"

    hide soldier

    show lagouga

    lg "Yes, give up."

    hide lagouga

    show serfopo angry

    sf "Oh come on, like more soldiers and lagouga weren't enough!"

    hide serfopo angry

    show thomas neutral arms

    t "I've seen only 3 soldiers so far."

    hide thomas neutral arms

    show soldier

    "Target: Soldier"

    menu:

        "Thomas' turn."

        "Punch":

            jump soldierthreepunch

        "kick":

            jump soldierthreekick


label soldierthreekick:

    "Thomas kicks the soldier."

    "He gets pushed far."

    jump lagougatarget


label soldierthreepunch:

    "Thomas puches the soldier."

    "He gets a serious injury."

    hide soldier

    "The soldier faints and escapes."

    jump lagougatarget


label lagougatarget:

    hide soldier

    show lagouga

    "Target: Lagouga"

    menu:

        "Nigel's turn"

        "Punch":

            jump lagougatwopunch

        "Kick":

            jump lagougatwokick

        "Stab":

            jump lagougatwostab

        "Let Serfopo have a turn":

            jump lagougatwoserfopo


label lagougatwopunch:

    "Nigel punches a lagouga."

    "It reflects his attack."

    "Nigel faints."

    jump lagougatwoserfopo


label lagougatwokick:

    "Nigel punches a lagouga."

    "It reflects his attack."

    "Nigel faints."

    jump lagougatwoserfopo


label lagougatwostab:

    "Nigel stabs a lagouga."

    "Lagouga perishes."

    "YOU WON!"

    jump lagougavictory


label lagougatwoserfopo:

    menu:

        "Serfopo's turn."

        "Punch":

            jump lagougatwopunchserfopo

        "Shoot":

            jump lagougatwoshoot


label lagougatwopunchserfopo:

    "Serfopo punches a lagouga."

    "It reflects Serfopo's attack."

    "Serfopo faints."

    "GAME OVER"

    return


label lagougatwoshoot:

    "Serfopo shoots a lagouga in the chest using a firerock gun."

    hide lagouga

    "Lagouga perishes."

    "YOU WON!"

    jump lagougavictory


label lagougavictory:

    hide lagouga

    show thomas happy talking

    t "Nice!"

    hide thomas happy talking

    show thomas talking

    t "Wait a minute!!"

    hide thomas talking

    show nigel neutral

    n "?"

    hide nigel neutral

    show serfopo neutral

    sf "?"

    hide serfopo neutral

    show thomas surprised

    t "First, we need to go to the Abyssal Kingdom to put an end to it, and then we should go to Serfopo's great grandma's house to get into Outer World!"

    hide thomas surprised

    show nigel happy talking

    n "Nice idea Thomas!"

    hide nigel happy talking

    zgu "Greetings, adventurers. I feel that you're tired!"

    show thomas confused

    t "Who is that?"

    hide thomas confused

    show zagingagin
    with dissolve

    zgu "It's me!"

    hide zagingagin

    show thomas confused
    
    t "Who-"

    hide thomas confused

    show zagingagin

    zgu "Allow me to introduce myself!"

    zg "My name is Zagingagin, and i live in this swamp."

    zg "You guys seem to be tired from this adventure. Do you want to come to my house and rest?"

    hide zagingagin

    show serfopo happy

    sf "Sure, i'm very tired!"

    hide serfopo happy

    show thomas confused

    t "Didn't you say ''I feel that you're tired?''"


    t "Besides that, we need to go to Qza Wolqekc in time, so sorry, we have no time!"

    hide thomas confused

    show zagingagin

    zg "Well, how about i give you all Poptarts?"

    hide zagingagin

    "Everyone agreed"

    show zagingagin

    zg "Very well..."

    hide zagingagin

    show thomas confused

    t "Thinking: ''Something is totally off... But i'll enter anyway...''"

    hide thomas confused

    show zagingagin

    zg "Good, now let's go."

    hide zagingagin

    scene bg black
    with dissolve

    "Everyone came in. It looked like an average house. The furniture is very comfortable."

    "Zagingagin did give our heroes the promised Poptarts and leaded them to two bedrooms, with one of them having two beds while the first one has one bed."

    "As if he planned something... or did he? Or didn't? Who knows?"

    "Eventually, everyone have fallen asleep."

    "Nigel is dreaming about visiting an amusement park."

    "Serfopo is dreaming about cats and singing meme songs."

    "And Thomas..."

    scene bg dreamrays
    with fade

    "He ended up in a strange place."

    show thomas confused rayd

    t "Where am i?"

    hide thomas confused rayd

    show eye of warns
    with dissolve

    eow "I am Eye Of Warns, and i'm here you to warn about what will happen next morning."

    eow "You need to defeat the King of Swamp Hermits in time."

    hide eye of warns

    show thomas confused rayd

    t "Does it have to do with all this stuff happened recently?"

    hide thomas confused rayd

    show eye of warns

    eow "Yes. Otherwise, your will lose your team."

    eow "I also heard you saying something about Abyssal Kingdom and Qza Wolqekc, but you can't make sure where to go first."

    hide eye of warns

    show thomas confused rayd

    t "I guess Qza Wolqekc."

    hide thomas confused rayd

    show eye of warns

    eow "I'm glad you understood what is supposed to happen."

    eow "Since King of Swamp Hermits is quite strong, you need to train."

    menu:
    
        eow "Show me what you got!"

        "Punch":

            jump eyeofwarnspunch

        "Kick":

            jump eyeofwarnskick


label eyeofwarnskick:

    "Thomas kicks Eye Of Warns."

    "It didn't affect Eye Of Warns that much."

    jump eyeofwarnsfirstattack


label eyeofwarnspunch:

    "Thomas punched Eye Of Warns."

    "It affected Eye Of Warns that much."

    jump eyeofwarnsfirstattack


label eyeofwarnsfirstattack:

    "Very well, Thomas."

    "Now dodge red rectangles. Get through the green ones though."

    menu:

        "The road turns into a conveyer. Eye Of Warns throws rectangles at you. Choose the direction to go."

        "Go Left":

            jump eyeofwarnsleft

        "Go right":

            jump eyeofwarnsright


label eyeofwarnsleft:

    "Thomas goes left."

    "He gets hit by a red rectangle, then falls down."

    "GAME OVER"

    return


label eyeofwarnsright:

    "Thomas goes right."

    "He goes through a green rectangle."

    menu:

        "Another wave of rectangles."

        "Stay still at the right side":

            jump eyeofwarnsrighttwo

        "Go Left":

            jump eyeofwarnslefttwo


label eyeofwarnsrighttwo:

    "Thomas stays still"

    "He gets hit by a red rectangle, then falls down."

    "GAME OVER"

    return


label eyeofwarnslefttwo:

    "Thomas goes left."

    "He goes through a green rectangle."

    eow "Great job Thomas!"

    eow "Remember one last thing!"

    "before Eye of Warns vanishes, he says his important words."

    eow "Once you get asked to stay, refuse!"

    eow "And when you end up in the endless hall, try to disgust King of Swamp Hermits with what Serfopo prefers."

    hide eye of warns

    show thomas confused rayd

    t "But i don't know what does Serfopo like!"

    hide thomas confused rayd

    show eye of warns

    eow "Try to ask him."

    eow "Now i really need to go. Goodbye Thomas..."

    hide eye of warns
    with fade

    "Eye of Warns disappeared."

    scene bg black
    with dissolve

    "Thomas wakes up."

    "..."

    vx "Hello guys, Vyxi here."

    vx "This game has suffered development hell for a whole year."

    vx "I never had any motivation to continue it."

    vx "I was always busy with college stuff and my other projects."

    vx "It's the best to cancel the game and no longer worry about it."

    vx "The artstyle sucks, but i can't draw any better."

    vx "I couldn't implement the actual RPG system due to zero knowledge of how to do it."

    vx "Maybe in the far future, i can hire a lot of people to work for the game's revival."

    vx "It won't be a visual novel though."

    vx "Currently, i'm working for the comic series called ''Rocker and Charlie''."

    vx "The artstyle will be the same as here, which means it will still be bad."

    vx "But hopefully, i will learn to draw properly."

    vx "But from now on, let's just quit the game. Turned out to be quite crappy."

    vx "Enemies only being soldiers and Lagouga, and the lore is unfinished."

    vx "I shouldn't have made lore that complicated for a first project."

    vx "Welp, that was Vyxi, goodbye!"

    return