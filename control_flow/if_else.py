#!/usr/bin/env python3.6
# Python script if/else practice

"""
Print (ADMIN) followed by the user’s name if the user is an admin
Print ACTIVE - followed by the user’s name if the user is active
Print ACTIVE - (ADMIN) followed by the user’s name if the user is an admin and active
Print the user’s name if neither active nor an admin
"""

user = { 'admin': True, 'active': True, 'name': 'Homer' }
prefix = ""

if user['admin'] and user['active']:
    prefix = "ACTIVE - (ADMIN) "
elif user['admin']:
    prefix = " (ADMIN) "
elif user['active']:
    prefix = "ACTIVE - "

print(prefix + user['name'])
