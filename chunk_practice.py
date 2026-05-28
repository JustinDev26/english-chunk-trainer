#STEP 1:DeFINE THE TARGET  PHRASE FROM THE NOTEBOOK
correct_phrase="thrive under pressure"
#STEP 2:SET UP A BOOLEAN FLAG TO COMMAND THE LOOP STATUS
playing= True

#STEP 3:RUN THE INTERACTIVE LOOP WHILE  THE FLAG REMAINS True 
while playing:
    print("Recruiter asks: how do handlle stress? ->")
    my_answer=input("type the phrase: ").strip()
#STEP 4: VERIFY IF THE USER INPUT MATCHES THE CORRECT ANSWER
    if my_answer == correct_phrase:
        print("yeah,you got it👌")
        playing= False              #FINAL STEP:WE ARE GONNA COME UP WITH FEEDBACK FOR  INCORRECT ANSWER
    else:
        print("you were so close! 🎯look at your notebook")