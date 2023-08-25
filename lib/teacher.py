#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def teach(self, firstname , lastname , knowledge):
        super().__init__(firstname , lastname)
        self.knowledge = knowledge

    def teach(self):
        randomid = random.randint(0 , len(self.knowledge) -1)
        return self.knowledge [randomid]
    