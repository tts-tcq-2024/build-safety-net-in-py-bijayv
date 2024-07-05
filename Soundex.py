def get_soundex_code(c,prev_code):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    ch =  mapping.get(c, '0')  # Default to '0' for non-mapped characters
    if (prev_code == 7):
        return ch
        break
    elif ch != '0' and ch != prev_code:
        return ch
    else:
        return ""
    
def abc(name,prev_code):
    soundex = ""
    for char in name[1:]:
        code = get_soundex_code(char,prev_code)
        if(code != ""):
            soundex += code
            prev_code = code
    return soundex

def generate_soundex(name):
    if not name:
        return ""
    else:
        s = name[0].upper()
        prev_code = get_soundex_code(s,7)
        soundex = s + abc(name,prev_code)
        if len(soundex) > 4:
            soundex = soundex[:4]

    # Start with the first letter (capitalized)

    # Pad with zeros if necessary
    soundex = soundex.ljust(4, '0')

    return soundex
