#Code is written by ÖZER TANRISEVER
#Credit : https://www.linkedin.com/in/ozer-tanrisever/

from termcolor import colored, cprint


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
    
    print(colored(singleColorLength*'_', 'yellow', attrs = ['bold']), end ='')
    print(colored(singleColorLength*'_', 'red', attrs = ['bold']), end ='')
    print(colored(singleColorLength*'_', 'blue', attrs = ['bold']), end ='')
    print(colored(singleColorLength*'_', 'green', attrs = ['bold']), end ='')
    
#EXAMPLE USAGE

#print_error()
#print_warning()
#print_success()
#print_mix_colored_line(5)



