import requests
import click



@click.command()
@click.option('--test', help='Number of greetings.')
@click.option('--url', prompt='Enter target url:',help='scrap the website.')

def scrapper(test,url):
    """A simple scrapper that scraps the html content of a website. Created by adarshreddy(vengixLabs)"""
    a=url
    r=requests.get(a)
    r.encoding
    click.echo(r.text)

if __name__ == '__main__':
    scrapper()


#a=input()

#r = requests.get(a)

#r.encoding
#print(r.text)