import click
from colored import fg, bg, attr

class Message:
	def __init__(self):
		pass

	def info(message):
		click.echo(f"{bg(27)}{fg(15)}{attr('bold')}INFO:{bg(0)} {message}");
	
	def warning(message):
		click.echo(f"{bg(220)}{fg(15)}{attr('bold')}WARNING:{bg(0)} {message}");
	
	def success(message):
		click.echo(f"{bg(40)}{fg(15)}{attr('bold')}SUCCESS:{bg(0)} {message}");
	
	def error(message):
		click.echo(f"{bg(9)}{fg(15)}{attr('bold')}ERROR:{bg(0)} {message}");