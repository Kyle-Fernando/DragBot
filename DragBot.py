def mood():
  import random;
  tea_type = input("how's the tea, sis? (hot, cold, mild):")
  tea = {
    'hot': ['werk, sister!', 'slay, bae', 'chantay you STAY', 'Kween', 'yas, hunty!!', 'SNATCHED', 'my wig just flew off!', 'SHOOK like a CROOK', 's h a k i n g in my boots'],
    'cold': ['sashay AWAY','i am GAGGED', 'gooped', '*tongue pop* okuuurt', 'ooo no henny', 'thank u, next', 'stream 1999 by Charli XCX', "thinking you're a bit 2000 and LATE",'need some READING lessons'],
    'mild': ['brunch?', 'do we stan?', 'wanna listen to Beyoncé?', 'skrrt, skrrt', 'Listen to "Almost Love" by Sabrina Carpenter', 'we stan Kacey Musgraves: Gay Icon', 'Ever hear of Ms. Ariana Grande?']
    }
  for shade in tea:
    if(tea_type == 'hot'):
      print(random.choice(tea['hot']))
    elif(tea_type == 'cold'):
      print(random.choice(tea['cold']))
    elif(tea_type == 'mild'):
      print(random.choice(tea['mild']))
    elif(tea_type == ''):
      print('you there, sis??')
    else:
      print('is your wig on too tight, hunty?')
  age = input('how old are you, girl?')
  age = int(age)
  bars = ["Micky's", "The Abbey", "Fiesta Cantina", "Flaming Saddles", "Beaches", "Mother Lode", "The Bayou", "Tops Bar", "Trunks", "Revolver" ]
  if age < 18:
    print('i think you need some more booty shaking practice baby..')
    for shade in tea:
      print(random.choice(tea['cold']))
  elif age < 21:
    print("better stick to Rage with the rest of the twinks, girl...")
    for shade in tea:
      print(random.choice(tea['mild']))
  elif age >= 21:
    print("W I G, let's go to " + random.choice(bars) + " tonight and catch some trade, honey! ;)")
    for shade in tea:
      print(random.choice(tea['hot']))
  reading_lesson = input('is reading FUNDAMENTAL? (yes, no)')
  if reading_lesson == 'yes':
    print('the library is open, darling... and you can read me for FILTH')
    for shade in tea:
      print(random.choice(tea['hot']))
  elif reading_lesson == 'no':
    print('the library is closed.')
    for shade in tea:
      print(random.choice(tea['cold']))
mood()
