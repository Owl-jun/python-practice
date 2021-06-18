# 모스 부호 해독



data = '.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'

def solveMos(data):
    solve = {
    '.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E', '..-.':'F', '--.':'G', '....':'H', '..':'I', '.---':'J', '-.-':'K','.-..':'L','--':'M',
    '-.':'N', '---':'O', '.--.':'P', '--.-':'Q', '.-.':'R', '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W', '-..-':'X', '-.--':'Y', '--..':'Z'
    }
    result = ''
    list = data.split(' ')
    for i in list:
        if i == '':
            result += ' '
        else: result += solve[i]
    return result

print(solveMos(data))