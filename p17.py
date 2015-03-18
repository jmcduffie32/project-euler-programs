digitsList = [
    {
        '0' : '',
        '1' : 'one',
        '2' : 'two',
        '3' : 'three',
        '4' : 'four',
        '5' : 'five',
        '6' : 'six',
        '7' : 'seven',
        '8' : 'eight',
        '9' : 'nine'
        },

    {
        '0' : '',
        '1' : '',
        '2' : 'twenty',
        '3' : 'thirty',
        '4' : 'forty',
        '5' : 'fifty',
        '6' : 'sixty',
        '7' : 'seventy',
        '8' : 'eightty',
        '9' : 'ninety'
        },

    {
        '0' : '',
        '1' : 'onehundred',
        '2' : 'twohundred',
        '3' : 'threehundred',
        '4' : 'fourhundred',
        '5' : 'fivehundred',
        '6' : 'sixhundred',
        '7' : 'sevenhundred',
        '8' : 'eighthundred',
        '9' : 'ninehundred'
        }
    ]

characters = ''

for num in range(1000):
    num = str(num)
    if len(num) == 1:
        characters += digitsList[0]
    
