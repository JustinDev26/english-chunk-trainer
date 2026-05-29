# 1.  COMMMENCE SYNONYMS MAP
synonyms_map = {
    "solve": ["resolve", "fix", "settle"],
    "check": ["verify", "look into", "double-check"],
    "want": ["aim to", "strive to", "am eager to"],
    "improve": ["optimize", "boost", "upgrade"],
    "problem": ["technical issue", "glitch", "setback"]
}

# 2. LETS CREEATE MAIN LOOP CONTROL
program_running = True

while program_running:
    print("\n ENGLISH CHUNK & SYNONYM TRAINER")
    print("[1] Practice: 'thrive under pressure'")
    print("[2] Practice: 'i want to grow'")
    print("[3] Find BPO Synonyms (Notebook)")
    print("[4] Exit")

    option = input("Choose an option (1-4): ").strip()
#
    if option == "1":
        playing = True
        correct_phrase = "thrive under pressure"
        while playing:
            print("\nRecruiter asks: How do you handle stress?")
            my_answer = input("Type the phrase: ").strip().lower()
            if my_answer == correct_phrase:
                print("Yeah, you got it! 👌")
                playing = False
            else:
                print("You were so close! 🎯 Look at your notes.")

    elif option == "2":
        english_phrase = "i want to grow in this company"
        print("\nTranslate to English: Quiero crecer en esta empresa")
        my_answer = input("Your answer: ").strip().lower()
        if my_answer == english_phrase:
            print("Excellent bro 🔥! The chunk is perfect.")
        else:
            print("Close but no cigar 🚬")

    elif option == "3":
        print("\n--- BPO synonym finder ---")
        word = input("Enter a basic word (solve/check/want/improve/problem): ").strip().lower()
        if word in synonyms_map:
            print(f"\n✨ Professional options for '{word}':")
            for syn in synonyms_map[word]:
                print(f"🍺 {syn}")
        else:
            print("\n🔒 Word not found in your BPO bank yet.")

    elif option == "4":
        print("\n..😉 Thank you for practicing, Justin! Keep improving. Goodbye!")
        program_running = False

    else:
        print("\n❌ Invalid option! Please choose between 1 and 4.")
