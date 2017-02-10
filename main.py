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
import re
import cgi

def build_page(user_input = {"user" : "", "password":"", "verify": "", "email":"", "user_error":"", "password_error":"", "verify_error":"", "email_error":""}):
    user_label = "<label>Username\t</label>"
    user = "<input type='text' name='user' value='%(user)s'/>"
    user_error = "<span>%(user_error)s</span>"
    user_area = user_label + user + user_error

    password_label = "<label>Password\t</label>"
    password = "<input type='text' name='password'/>"
    password_error = "<span>%(password_error)s</span>"
    password_area = password_label + password + password_error

    verify_label = "<label>Verify Password\t</label>"
    verify = "<input type='text' name='verify'/>"
    verify_error = "<span>%(verify_error)s</span>"
    verify_area = verify_label + verify + verify_error

    email_label = "<label>Email (optional)\t</label>"
    email = "<input type='text' name='email' value='%(email)s'/>"
    email_error = "<span>%(email_error)s</span>"
    email_area = email_label + email + email_error

    submit = "<input type='submit'/>"

    form = "<form method='post'>" + user_area + "<br/>" + password_area + "<br/>" + verify_area + "<br/>" + email_area + "<br/>" + submit
    header = "<h1>Sign-Up</h1>"

    return header + form % user_input

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    if email == "":
        return True
    return  email and EMAIL_RE.match(email)


class Index(webapp2.RequestHandler):
    def get(self):
        content = build_page()
        self.response.write(content)

    def post(self):
        success = True
        user = cgi.escape(self.request.get("user"))
        password = cgi.escape(self.request.get("password"))
        verify = cgi.escape(self.request.get("verify"))
        email = cgi.escape(self.request.get("email"))

        user_input = {"user" : user, "email": email, "user_error" : "", "password_error" : "","email_error" : "","verify_error" : ""}
        if not valid_username(user):
            #self.response.write("User Failed")
            user_input["user_error"] = "Invalid Username"
            success = False

        if not valid_password(password):
            #self.response.write("password failed")
            user_input["password_error"] = "Invalid Password"
            success = False

        if not valid_email(email):
            user_input["email_error"] = "Invalid Email"
            success = False

        if password != verify:
            user_input["verify_error"] = "Passwords do not match"
            success = False

        if success==False:
             content = build_page(user_input)
             self.response.write(content)
        else:
            self.redirect("/welcome?user=" + user)



class Welcome(webapp2.RequestHandler):
    def get(self):
        user = self.request.get("user")

        self.response.write("Welcome, {}!".format(user))

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/welcome', Welcome)
], debug=True)
