teens = ['eleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen']
singleDigits = ['onetwothreefourfivesixseveneightnine']
doubleDigits = ['tentwentythirtyfortyfiftysixtyseventyeightyninety']
tripleDigits = ['onehundredtwohundredthreehundredfourhundredfivehundredsixhundredsevenhundredeighthundredninehundred']
thousand = ['onethousand']
ands = ['and']

print len(teens) * 10 + len(singleDigits) * 9 * 10 + len(doubleDigits) * 10 + len(tripleDigits) * 100 + len(ands) * 99 * 9 + len(thousand)
