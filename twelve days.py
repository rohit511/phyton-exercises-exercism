def recite(start_verse, end_verse):
    days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
            'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    gift = ['a Partridge in a Pear Tree.', 'two Turtle Doves, and',
            'three French Hens,', 'four Calling Birds,', 'five Gold Rings,',
            'six Geese-a-Laying,', 'seven Swans-a-Swimming,', 'eight Maids-a-Milking,',
            'nine Ladies Dancing,',  'ten Lords-a-Leaping,',  'eleven Pipers Piping,',
            'twelve Drummers Drumming,']
    return [f'On the {days[i]} day of Christmas my true love gave to me: {" ".join(gift[i::-1])}' for i in range(start_verse-1, end_verse) ]