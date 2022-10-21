def cipher():
    t = '200820 BLACKPLINK Jennie is regarded to have great effect on KT Mystic Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20(LG U+ Mystic Pink 30%, SKT Mystic Blue not disclosed)'
    t = t.replace('SKT',  '*')
    t = t.replace('KT', '*')
    t = t.replace('Samsung', '*')
    t = t.replace('LG','*')
    print(t)

cipher()