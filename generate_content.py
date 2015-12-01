"""Generates random post content for benchmarking Grow.

Based on jaden's Hugo benchmark:
https://gist.github.com/jaden/1ce5a7192d8ee8e4c112
"""

from datetime import datetime
import random
import string

OUT_DIR = 'content/post'
NUM_POSTS = 5000
NUM_CATEGORIES = 10


def generate_word():
  length = random.randint(1, 10)
  word = ''.join(random.choice(string.letters) for _ in range(length))
  return word


def generate_sentence(words):
  return ' '.join([generate_word() for i in range(words)])


def generate_date():
  year = random.choice(range(1950, 2015))
  month = random.choice(range(1, 13))
  day = random.choice(range(1, 29))
  hours = random.choice(range(0, 24))
  minutes = random.choice(range(0, 60))
  seconds = random.choice(range(0, 60))
  return datetime(year, month, day, hours, minutes, seconds).strftime('%Y-%m-%d_%H-%M-%S')


def create_post(out_dir, categories):
  title = generate_sentence(8)
  desc = generate_sentence(20)
  cat = random.choice(categories)
  slug = title.replace(' ', '-').lower()
  slug = ''.join(c for c in slug if c.isalnum() or c == '-')
  path = '{}/{}.md'.format(out_dir, generate_date())
  with open(path, 'w') as f:
    f.write('---\n')
    f.write('$title: "{}"\n'.format(title))
    f.write('$description: "{}"\n'.format(desc))
    f.write('$categories: [\n "{}"\n]\n'.format(cat))
    f.write('$date: "{}"\n'.format(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S-00:00')))
    f.write('$slug: "{}"\n'.format(slug))
    f.write('---\n\n')
    num_paragraphs = random.randint(5, 10)
    for i in range(num_paragraphs):
      f.write(generate_sentence(random.randint(50, 100)))
      f.write('\n\n')


def main():
  categories = [generate_word() for i in range(NUM_CATEGORIES)]
  for i in range(NUM_POSTS):
    create_post(OUT_DIR, categories)


if __name__ == '__main__':
  main()
