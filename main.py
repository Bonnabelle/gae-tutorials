#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2, jinja2, os, sys

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

sys.dont_write_bytecode = 1 # Should tell system to stop writing .pyc files

class MemeHandler(webapp2.RequestHandler):
    visits = 0
    def get(self):
        MemeHandler.visits += 1 # Static variable
        t = jinja_env.get_template("meme.html")
        response = t.render(visits=self.visits)
        self.response.write(response)

class TutorialHandler(webapp2.RequestHandler):
    def get(self):
        t = jinja_env.get_template("tutorial.html")
        response = t.render()
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', MemeHandler),
    ('/tutorial',TutorialHandler)
], debug=True)
