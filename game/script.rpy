init python:
    class Items(object):
        def __init__(self, name):
            self.idle = name + "_idle.png"
            self.hover = name + "_hover.png"
            self.LabelToCall = name + "Dialog"
            self.item = name


# Hier beginnt das Spiel.
label start:
   
    call variables

    scene bg titel with dissolve

    pause


    scene bg erstescene01 with dissolve

    
    Dave "Mom?"
    Mutter "Ja,Dave?"
    Dave "Woran ist er gestorben?"
    Mutter "Ich weiß es nicht Dave. Niemand wusste es. Nichtmal mir konnte jemand etwas erzählen und keiner konnte ihm helfen."
    Mutter "(Verdammt Micky. Was ist nur passiert?)"
    Dave "(Dad...)"


    scene bg grabstein with dissolve

    pause

    scene bg timeskip01 with dissolve


    pause 4.0


    scene bg timeskipbackground 
    
    pause

    show Dave timeskip at left with dissolve

    Dave "Oh Hallo.Ich hab dich ja garnicht bemerkt."
    Dave "Wo kommst du den her?"
    Dave "Du kannst mich doch sehen oder? Wieso antwortest du mir den nicht?"
    Dave "..."
    Dave "Oh...Ich entschuldige mich für mein Verhalten."
    Dave "Ich hab ja noch garnicht nach deinen Namen gefragt haha. Wie unhöflich von mir. Wie heißt du den?"

    python:
        Playername  = renpy.input("Komm sag mir bitte deinen Namen?", length = 32)

        if not Playername:
            Playername = renpy.input("Ich möchte doch nur deinen Namen erfahren")
        if not Playername:
            Playername = renpy.input("Bist wohl nicht der gesprächigste was?")
        
        if not Playername:
            Playername = "Scott"
            Dave("Wirklich kein Grund schüchtern zu sein. Naja gut. Hey wie wärs wenn ich dir ein Namen ausdenke. Ab heute lautet dein Name [Playername]")





    Dave "Herzlich Willkommen in meiner Welt [Playername]. Mein Name ist Dave. Ich bin 19 Jahre alt und studiere zurzeit Medizin."
    Dave "Ich verfolge ein Ziel,weißt du. Ich muss einfach herauszufinden an was mein Dad verstorben ist und dafür muss ich einer der besten werden."
    Dave "Aber reden wir nicht so lange über mich. Du möchtest bestimmt das Spiel sehen."
    Dave "Dann fangen wir an. Folge mir auf meiner Reise."  

    scene bg strasse with dissolve

    pause

    scene bg strassen02 with dissolve

    pause

    show Dave strasse with dissolve
    Dave "Wie es aussieht bist du erfolgreich hier angekommen [Playername]."
    Dave "Und dies ist mein Zuhause. Die Schule hat mich hungrig gemacht. Lass uns doch reingehen"

    scene bg vordertür with dissolve 

    pause

    scene bg just_room with dissolve

    pause

    show Dave drinne with dissolve

    pause

    show Mutter drinne with dissolve

    pause
 


    Mutter "Oh Hallo Dave. Du bist ja heute schon früh Zuhause. *hust*"
    Dave "Hey. Ja, die Vorlesungen in der Schule gingen heute nicht so lange. Wie geht es dir zurzeit?"
    Mutter "Ja es ist schon besser geworden. *Hust* *Hust* Aber mach dir keine Gedanken drüber. Das wird schon wieder Dave."
    Dave "Ach Mom du solltest mal etwas Pause machen und dir etwas Urlaub gönnen. Du siehst wirklich nicht mehr gut aus!"
    Mutter "*Hust* Es ist nur eine kleine Erkältung. In paar Tagen bin ich wieder Topfit."
    Dave "..."
    Mutter "Oh... Aber ich muss jetzt wieder schleunigst zur Arbeit gehen. Essen habe ich dir in dein Zimmer gestellt. Bye"
    Dave "(Ich muss schleunigst was tun. So geht das nicht mehr weiter. Sie sieht echt schlimm aus.)"
    Dave "Vielleicht sollten wir vorher noch in mein Zimmer vorbeischauen."


    $ added_items = set()



    python:
        def addItemsToSet(itemName):
            global itemsAreAdded
            if len(added_items) != 3:
                added_items.add(itemName)
            if len(added_items) == 3:
                itemsAreAdded = True

        def checkAddedItems():
            global amountOfTimesFailed
            global added_items
            global itemsAreAdded
            if "rot" in added_items and "gelb" in added_items and "pink" in added_items:
                renpy.jump("drogenScene")
            else:
                if len(added_items) == 3:
                    added_items = set()
                    itemsAreAdded = False
                    amountOfTimesFailed += 1
                    if amountOfTimesFailed == 3:
                        renpy.jump("todesSzene")


    menu:
        "Ins Zimmer gehen":
            jump Zimmer
        "Ins Labor gehen":
            jump Labor

    label Zimmer:
        scene bg Zimmer
        call screen zimmerItem



    screen zimmerItem():

        for q in zimmerImageButtons:
            imagebutton:
                idle q.idle
                hover q.hover
                focus_mask True
                action Jump(q.LabelToCall)

    label Labor:
        scene bg Labor
        

        pause

        show Dave timeskip at left with dissolve

        Dave "Willkommen in meinem Labor. Es wird höchste Zeit das Mittel fertigzustellen. Ich hoffe du bist bereit dafür. Kleiner Tipp das zweite Buch ist unten rechts"

        scene bg Labor

        pause

        scene bg labormix
        call screen LaborItems
  
        "Ich hoffe du weißt was zu tun ist. Kleine Hilfe am Rande. Die dritte Farbe ist pink."



    screen LaborItems(): 
        imagebutton auto "gelb_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "gelbe Flasche")           
            unhovered SetVariable("screen_tooltip", "")
            action Function(addItemsToSet, "gelb")

        imagebutton:
            idle "grün_idle.png"
            hover "grün_hover.png"
            focus_mask True
            hovered SetVariable("screen_tooltip", "Grüne Flasche")            
            unhovered SetVariable("screen_tooltip", "")
            action Function(addItemsToSet, "grün")

        imagebutton:
            idle "lila_idle.png"
            hover "lila_hover.png"
            focus_mask True
            hovered SetVariable("screen_tooltip", "Lila Flasche")            
            unhovered SetVariable("screen_tooltip", "")
            action Function(addItemsToSet, "lila")

        imagebutton:
            idle "rot_idle.png"
            hover "rot_hover.png"
            focus_mask True
            hovered SetVariable("screen_tooltip", "Rote Flasche")            
            unhovered SetVariable("screen_tooltip", "")
            action Function(addItemsToSet, "rot")

        imagebutton:
            idle "pink_idle.png"
            hover "pink_hover.png"
            focus_mask True
            hovered SetVariable("screen_tooltip", "pinke Flasche")            
            unhovered SetVariable("screen_tooltip", "")
            action Function(addItemsToSet, "pink")

        imagebutton:
            idle "funktion01_idle.png"
            hover "funktion01_idle.png"
            focus_mask True
            hovered SetVariable("screen_tooltip", "funktion")
            unhovered SetVariable("screen_tooltip", "")
            action Function(checkAddedItems)



        imagebutton:
            idle "Itemglas"
            hover "Itemglas"
            focus_mask True
            hovered SetVariable("screen_tooltip", "glas")
            unhovered SetVariable("screen_tooltip", "")
            action Function(checkAddedItems)

        



    label drogenScene:

        scene bg droge with dissolve

        pause 

    label drogenNehmen:
        menu:
            "Take":
                "ne geht nicht, wir muessen mom noch helfen"
                jump weis
            "Don't take":
                "Nimm die Droge oder das Spiel geht nicht weiter :)"
                call drogenNehmen


      

    
    label weis:
        scene bg weis

    pause 

    "Was ist passiert?"
    "Wieso ist alles weiß.Ist das die Wirkung der Pille?."
    "Oh ich glaube ich höre etwas."

    scene bg wiesegeschlosseneaugen with dissolve

    pause

    scene bg wieseclose with dissolve

    pause

    Dave "Hmm? Was ist bloß passiert?"
    Dave "Wo befinde ich mich hier nur?"
    Dave "Ich sollte mich mal umschauen"

    label todesSzene:

        return

    return

label variables:
    python:
        zimmerImageButtons = []
        zimmerImageButtons.append(Items("zulabor"))
        zimmerImageButtons.append(Items("pc"))
        zimmerImageButtons.append(Items("ball"))
        zimmerImageButtons.append(Items("zettel"))
        zimmerImageButtons.append(Items("uhr"))
        zimmerImageButtons.append(Items("tv"))
        zimmerImageButtons.append(Items("papier"))
        zimmerImageButtons.append(Items("rahmen"))
        zimmerImageButtons.append(Items("notizen"))
        zimmerImageButtons.append(Items("lampe"))
        zimmerImageButtons.append(Items("bücher"))
        zimmerImageButtons.append(Items("buch"))
        zimmerImageButtons.append(Items("gitarre"))

    define Dave = Character("Dave")
    define Mutter = Character("Mutter")
    default itemsAreAdded = False
    default amountOfTimesFailed = 0
    image Dave timeskip = "Dave_timeskip.png"
    image Dave drinne = "Dave_inside.png"
    image Dave strasse = "Davestrasse.png"
    image Mutter drinne = "Mutter_inside.png"
    image black = "#000000"
    image white = "#ffffff"
    image bg Zimmer ="bg Zimmer.jpg"
    image bg Labor = "bg Labor.jpg"
    image bg wiese = "bg wiese.jpg"
    image bg weis = "bg weis.jpg"
    image bg labormix = "bg labormix.jpg"
    image Itemglas = ConditionSwitch(
        "itemsAreAdded == True", "glasleuchten.png",
        "True", "glas_idle.png")

    transform my_Left: 
        xalign 0.1 yalign 1.0

    transform my_Right:
        xalign 0.9 yalign 1.0



