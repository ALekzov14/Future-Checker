import os
import re

def process_file(input_file, output_file):
  with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
      line = line.strip()
      if line.startswith('https'):
        match = re.search(r'^(?:\S+[\s:|;])?(login|[^\s:|;]+)(?:(?::|;|\s|[|])([^ ]+))$', line)
        if match:
          login = match.group(1)
          password = match.group(2)
          outfile.write(f"{login}:{password}\n")
      else:
        match = re.search(r'^(?:\S+[\s:|;])?(login|[^\s:|;]+)(?:(?::|;|\s|[|])([^ ]+))$', line)
        if match:
          login = match.group(1)
          password = match.group(2)
          outfile.write(f"{login}:{password}\n")

process_file('../input_nursultan.txt', '../txt/output_for_bad_romover_nursultan.txt')
exec(open('Bad_Remover_Nursultan.py').read())
os.system('Bad_Remover_Nursultan.py')