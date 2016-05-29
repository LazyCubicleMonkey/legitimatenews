# [START imports]
import os
# import urllib
import logging
# import random

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)


# [END imports]


class Section(object):
	# A main model for representing an individual section entry.
	def __init__(self, section):
		self.section = section
		path = os.path.join(os.path.dirname(__file__), 'stories' + os.path.sep + section)
		stories = os.listdir(path)
		self.stories = []
		for filename in stories:
			# logging.info("Filename: " + filename + " for section: " + self.section)
			story = Story(section + os.path.sep + filename)
			self.stories.append(story)

	def __str__(self):
		return "Section: " + self.section + "Stories: " + self.stories


class Story(object):
	# A main model for representing an individual story entry.
	def __init__(self, filename):
		full_filename = os.path.join(os.path.dirname(__file__), 'stories' + os.path.sep + filename)
		# logging.info("Filename: " + filename + " fullFilname: " + full_filename)
		template = open(full_filename, "r")
		self.filename = filename
		self.title = template.readline()
		self.fullTitle = template.readline()
		self.image = template.readline()
		self.hype = template.readline()
		if "hype:" in self.hype:
			self.claims = []
			line = template.readline()
			while "source:" not in line:
				hype = Hype(line)
				self.claims.append(hype)
				line = template.readline()
			self.source = template.readline()
		self.article = template.read()
		template.close()
	# date = ndb.DateTimeProperty(auto_now_add=True)

	def __str__(self):
		return "Filename: " + self.filename + "\nTitle: " + self.title + "Description: " + self.fullTitle + "Image: " + self.image


class Hype(object):
	# Represents the hyped up claim of each source. Has the URL and the title/claim
	def __init__(self, line):
		index = line.find(" ")
		self.link = line[:index]
		self.title = line[index:]

	def __str__(self):
		return "Claim: " + self.link + "\nLink: " + self.link

# [START main_page] Another idea for legitimate news: What if I do real stories but have headlines completely blown out
# of proportion in sarcasm while the body explains how stupid the news story is.
# Perhaps something similar to cracked 'bs news articles of the week'

class MainPage(webapp2.RequestHandler):
	def get(self):
		path = os.path.join(os.path.dirname(__file__), 'stories')
		# filenames = os.listdir(path)
		filenames = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
		# filenames.sort()
		# random.shuffle(filenames,random.random)
		logging.info(filenames)
		stories = []
		sections = []
		ads = []
		chosen_story = self.request.get("story")
		logging.info("ChosenStory: " + chosen_story)
		i = random_num = 0
		for filename in filenames:
			# logging.info("Filename: " + filename)
			# random_num = i if filename == chosen_story else random_num
			# story = Story(filename)
			# stories.append(story)
			ads.append("Ad" + str(i))
			section = Section(filename)
			sections.append(section)
			for story in section.stories:
				if story.filename == chosen_story:
					random_num = i
				logging.info("Story filename: " + story.filename + " equal " + str(story.filename == chosen_story))
				stories.append(story)
				i += 1
		# random_num = random.randint(0, len(stories) - 1)
		feature_story = stories[random_num]
		logging.info(("Chosen" if chosen_story else "Random") + " story is: " + str(
			feature_story) + " because random_num is: " + str(random_num))
		template = JINJA_ENVIRONMENT.get_template('index.html')
		template_values = {
			'sections': sections,
			'stories': stories,
			'feature_story': feature_story,
			'ads': ads
		}
		self.response.write(template.render(template_values))


# [END main_page]

app = webapp2.WSGIApplication([
	('/', MainPage),
], debug=True)
