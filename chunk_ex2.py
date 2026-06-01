#go to apply the learned,lets endeavor something with random chunks 😉
#in this part we generated various functions:
#"opens bpo_notes.txt"  read mode "r"
#"with" statement this Ensures the file closes after wxecution
#"file.read" this extracts the content and display it
import random


# 1. SYNONYMS MAP updated
synonyms_map = {
"solve": ["resolve", "fix", "settle"],
"check": ["verify", "look into", "double-check"],
"want": ["aim to", "strive to", "am eager to"],
"improve": ["optimize", "boost", "upgrade"],
"problem": ["technical issue", "glitch", "setback" ]
}

chunks_store= [                 #NEW list 
"let me walk you through the process",
"i'd like to pivot to another point",
"as a matter of fact",
"to the best of my knowledge"
    ]

# 2. MAIN LOOP CONTROL
program_running = True

while program_running:
    print("\n ESTUDIO INTELIGENTE v1.0")
    print("[1] Practice: 'thrive under pressure'") 
    print("[2] Practice: 'i want to grow'")
    print("[3] Find BPO Synonyms (Notebook)")
    print("[4] Save new professional note (.txt)") #the function(.txt) 
    print("[5] view saved notes📖")# new
    print("[6]Exit")
    option = input("Choose an option (1-6): ").strip()

    if option == "1":
        correct_phrase = random.choice(chunks_store )  # i modifyied the text
        print("\nRecruiter asks: How do you handle stress?")
        my_answer = input("Type the phrase: ").strip().lower()
        if my_answer == correct_phrase:
                print("Yeah, you got it! 👌")
        else:
                print(f"You were so close! 🎯 the correct was: {correct_phrase}")

    elif option == "2":
        english_phrase = "i want to grow in this company"
        print("\nTranslate to English: Quiero crecer en esta empresa")
        my_answer = input("Your answer: ").strip().lower()
        if my_answer == english_phrase:
            print("Excellent bro 🔥! The chunk is perfect.")
        else:
            print("Close but no cigar 🚬")

    elif option == "3":
        print("\n--- BPO SYNONYM FINDER ---")
        word = input("Enter a basic word (solve/check/want/improve/problem): ").strip().lower()
        if word in synonyms_map:
            print(f"\n✨ Professional options for '{word}':")
            for syn in synonyms_map[word]:
                print(f"👉 {syn}")
        else:
            print("\n❌ Word not found in your BPO bank yet.")

    elif option == "4":
        print("\n--- QUICK NOTE SAVER ---")
        new_chunk = input("Type the new chunk or phrase: ").strip()
        meaning = input("Type the professional synonym or meaning: ").strip()
        with open("bpo_notes.txt", "a") as file:                #
            file.write(f"Chunk: {new_chunk} -> Meaning: {meaning}")
        print("\n🎯 Saved successfully to 'bpo_notes.txt'!")
    elif option == "5":
        print("\n--MY SAVED BPO NOTES📖--")
        with open("bpo_notes.txt","r")as file:               
            print(file.read())                          
    elif option == "6":
        print("\n👋 Thank you for practicing! Keep improving. Goodbye!")
        program_running = False

    else:
        print("\n❌ Invalid option! Please choose between 1 and 6.")
        