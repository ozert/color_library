#Code is written by ÖZER TANRISEVER
#Credit : https://www.linkedin.com/in/ozer-tanrisever/

from termcolor import colored, cprint
from math import ceil

def print_warning(warning_text = 'Warning => Things might go wrong!' ):
    text = '\n___________________________________________________\n'
    print(colored(text, 'yellow', attrs = ['bold']))

    print(colored(warning_text,'yellow', attrs = ['bold']))

    text = '___________________________________________________\n'
    print(colored(text, 'yellow', attrs = ['bold']))


def print_success(success_text = 'Process Succesful!'):
    text = '\n___________________________________________________\n'
    print(colored(text, 'green', attrs = ['bold']))

    print(colored(success_text,  'green', attrs = ['bold']))

    text = '___________________________________________________\n'
    print(colored(text, 'green', attrs = ['bold']))


def print_error(error_text = 'An error occured!'):
    text = '\n___________________________________________________\n'
    print(colored(text, 'red', attrs = ['bold']))

    print(colored(error_text, 'red', attrs = ['bold']))

    text = '___________________________________________________\n'
    print(colored(text, 'red', attrs = ['bold']))

def print_colored_red(text = None):
    
    print(colored(text, 'red', attrs = ['bold']), end ='')

def print_colored_green(text = None):
    
    print(colored(text, 'green', attrs = ['bold']), end ='')

def print_colored_yellow(text = None):
    
    print(colored(text, 'yellow', attrs = ['bold']), end ='')

def print_colored_blue(text = None):
    
    print(colored(text, 'blue', attrs = ['bold']), end ='')

def print_mix_colored_line(singleColorLength=0):
    assert isinstance(singleColorLength, (int,)) #Cannot use other than int variable
    print(colored(singleColorLength*'_', 'yellow', attrs = ['bold']), end ='')
    print(colored(singleColorLength*'_', 'red', attrs = ['bold']), end ='')
    print(colored(singleColorLength*'_', 'blue', attrs = ['bold']), end ='')
    print(colored(singleColorLength*'_', 'green', attrs = ['bold']), end ='\n')
    
def titleMaker(textTuple,baseLineLength,lineType,firstColor,secondColor,beforeTheLineText=''):

    assert len(lineType)!=0 #At least a character should be given to produce a line
    assert int(baseLineLength) > 0 # If raises error, the line below doesn't exists.
    assert len(textTuple)==2 # If raises error, that means the tuple is not in correct form.
    assert firstColor in ["blue","yellow", "red","green"] #Choose a color in this list.
    assert secondColor  in ["blue","yellow", "red","green"] #Choose a color in this list.
    assert len(beforeTheLineText) <2 #Only one character is allowed
    formattedTextLength=(len(textTuple[0])+2+len(textTuple[1])+2+5)
    beforeAndAfterSpace= ceil((baseLineLength-formattedTextLength)/2)

    print(int(beforeAndAfterSpace-1)*' ',end='')
    print(colored((formattedTextLength+1)*str(lineType),secondColor, attrs = ['bold']))
    print(int(beforeAndAfterSpace-1)*' ',end='')
    print(colored('| ',secondColor, attrs = ['bold']),end='')
    print(colored('['+textTuple[0]+']: ',firstColor, attrs = ['bold']),end='')
    print(colored('['+textTuple[1]+'] |',secondColor, attrs = ['bold']))
    if beforeTheLineText == '':
        print(colored(baseLineLength*lineType,secondColor, attrs = ['bold']))
    else:
        print(colored(beforeTheLineText,secondColor, attrs = ['bold']),end='')
        print(colored((baseLineLength-1)*lineType,secondColor, attrs = ['bold']))
    
#EXAMPLE USAGE

#print_error()
#print_warning()
#print_success()
#print_mix_colored_line(5)
#titleMaker(text,50,'-','green','yellow')



