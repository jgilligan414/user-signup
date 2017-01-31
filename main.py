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
import webapp2

def build_page(user_input):
    user_label = "<label>Username\t</label>"
    user = "<input type='text' name='user'/>"
    user_error = "<span></span>"
    user_area = user_label + user + user_error

    password_label = "<label>Password\t</label>"
    password = "<input type='text' name='password'/>"
    password_error = "<span></span>"
    password_area = password_label + password + password_error

    verify_label = "<label>Verify Password\t</label>"
    verify = "<input type='text' name='verify'/>"
    verify_error = "<span></span>"
    verify_area = verify_label + verify + verify_error

    email_label = "<label>Email (optional)\t</label>"
    email = "<input type='text' name='email'/>"
    email_error = "<span></span>"
    email_area = email_label + email + email_error

    submit = "<input type='submit'/>"

    form = "<form method='post'>" + user_area + "<br/>" + password_area + "<br/>" + verify_area + "<br/>" + email_area + "<br/>" + submit
    header = "<h1>Sign-Up</h1>"

    return header + form


class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")
        self.response.write(content)

    def post(self):
        user = self.request.get("user")

        self.response.write("Welcome, " + user)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
