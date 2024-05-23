from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    wis = ['wisdom','Wisdom','Tell','tell','pour','Pour','some','Some','more']
    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'hello' in lowered:
        return '"Mmmmm MONKE"'
    elif 'how are you' in lowered:
        return '"Good, Good is how i am"'
    elif 'bye' in lowered:
        return '"Farewell"'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    elif 'real' in lowered:
        return '"yesterday is history, tomorrow is a mistery, but today is a gift. Thats why its called The Present."'
    elif any(word in lowered for word in wis):
        return choice([
            '"if you are on a tower and a plane is what you see, you better start to flee"',
            '“If she sleeps with another, there is always her mother.”',
            '“If shes ugly but thick, moving to the back will do the trick.”',
            '"If she sleeps with another mister, there is always her sister"',
            '"If she is not in the mode, you shall show her mother your chode"',
            '"If she doesnt send nudes, you shall get together with dudes"',
            '"If you have no bitches, then trap all of them in ditches."',
            '"Jesus can turn water into wine, but I can turn your mama into mine."',
            '"If nautical nonsense be something you wish, then drop on the deck and flop like a fish"',
            '"If she leaves you for another man, you shall do to her mother what America did to Japan"',
            '"If her booty does not bounce, the end of the relationship you shall announce."',
            '"if her mother is already in the grave?, Well then my student...... You have to be brave"',
            '"If she is flat and has no cake, her mother you shall take"',
            '"If there is a hole....there is always a goal"',
            '"My students, do not be tempted by these virtual women. They will not bring happiness my students only sadness."',
            '"If she leaves you for another, You shall pursue her mother."',
        ])
    else:
        return choice([
            'I do not understand',
            'Mmmmmm MONKE',
            'Speak again child'
        ])