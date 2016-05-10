# [START imports]
import os
import urllib
import logging
import random

import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]

class Section(object):
	#A main model for representing an individual section entry.
	def __init__(self, section):
		self.section = section
		path = os.path.join(os.path.dirname(__file__), 'stories' + os.path.sep + section)
		stories = os.listdir(path)
		self.stories = []
		for filename in stories:
			#logging.info("Filename: " + filename + " for section: " + self.section)
			story = Story(section + os.path.sep + filename)
			self.stories.append(story)

	def __str__(self):
		return "Section: " + self.section + "Stories: " + self.stories


class Story(object):
    #A main model for representing an individual story entry.
	def __init__(self, filename):
		fullFilename = os.path.join(os.path.dirname(__file__), 'stories' + os.path.sep + filename)
		#logging.info("Filename: " + filename + " fullFilname: " + fullFilename)
		file = open(fullFilename, "r")
		self.filename = filename
		self.title = file.readline()
		self.fullTitle = file.readline()
		self.image = file.readline()
		self.article = file.read()
		#self.article = self.article.replace('\t','<p/>')
		file.close()
		#date = ndb.DateTimeProperty(auto_now_add=True)
	def __str__(self):
		return "Filename: " + self.filename + "\nTitle: " + self.title + "Description: " + self.fullTitle + "Image: " + self.image + "Article: " + self.article
	
# [START main_page] Another idea for legitimate news: What if I do real stories but have headlines completely blown out of porportion in sarcasm while the body explains how stupid the news story is.
#Perhaps something similar to cracked 'bs news articles of the week'
class MainPage(webapp2.RequestHandler):

  def get(self):
	path = os.path.join(os.path.dirname(__file__), 'stories')
	filenames = os.listdir(path)
	#filenames.sort()
	#random.shuffle(filenames,random.random)
	logging.info(filenames)
	stories = []
	sections = []
	ads = []
	chosenStory = self.request.get("story")
	logging.info("ChosenStory: " + chosenStory)
	i = randomNum = 0
	for filename in filenames:
		#logging.info("Filename: " + filename)
		#randomNum = i if filename == chosenStory else randomNum
		#story = Story(filename)
		#stories.append(story)
		ads.append("Ad" + str(i))
		section = Section(filename)
		sections.append(section)
		for story in section.stories:
			if story.filename == chosenStory:
				randomNum = i
			logging.info("Story filename: " + story.filename + " equal " + str(story.filename == chosenStory))	
			stories.append(story)
			i+=1
	#randomNum = random.randint(0, len(stories) - 1)
	featureStory = stories[randomNum]
	logging.info(("Chosen" if chosenStory else "Random") + " story is: " + str(featureStory) + " because randomNum is: " + str(randomNum))
	template = JINJA_ENVIRONMENT.get_template('index.html')
	template_values = {
		'sections': sections,
		'stories': stories,
		'featureStory': featureStory,
		'ads': ads
	}
	self.response.write(template.render(template_values))
# [END main_page]

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
