import click 
from oalib.solutions import code_generator

#create a click group
@click.group()
def cli():
    pass

#create a click command
@cli.command("generate")
@click.argument('text')
@click.option('--language',"-l", default='python', help='The programming language for the code')
def generate_code(text, language):
    """This command generates code from a comment using the OpenAI API.
    
    Example: 
        python3 pythonTutorCli.py generate "Calculate the mean distance between an array of points" 
    """
    print(language)
    code = code_generator(text, language)
    print(code)

if __name__ == '__main__':
    cli()
