MORSE = {
 ".-": "a", "-...": "b", "-.-.": "c",
 "-..": "d", ".": "e", "..-.": "f",
 "--.": "g", "....": "h", "..": "i",
 ".---": "j", "-.-": "k", ".-..": "l",
 "--": "m", "-.": "n", "---": "o",
 ".--.": "p", "--.-": "q", ".-.": "r",
 "...": "s", "-": "t", "..-": "u",
 "...-": "v", ".--": "w", "-..-": "x",
 "-.--": "y", "--..": "z"
}
with open('input.txt','r') as file:
    moz=file.read()
    lst=moz.split('  ')

    gap=""
    for i in range(len(lst)):
        q=lst[i].split(' ')
        for j in range(len(q)):
            try:
                gap +=MORSE[q[j]]
            except:
                continue
        gap+=" "

    with open('output.txt','w') as file:
        file.write(gap)