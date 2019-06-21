#!/usr/bin/env python3.6
# List iteration practice

"""
Print (ADMIN) followed by the user’s name if the user is an admin
Print ACTIVE - followed by the user’s name if the user is active
Print ACTIVE - (ADMIN) followed by the user’s name if the user is an admin and active
Print the user’s name if neither active nor an admin
"""

users = [
    { 'admin': True, 'active': True, 'name': 'Homer' },
    { 'admin': True, 'active': False, 'name': 'Marge' },
    { 'admin': False, 'active': True, 'name': 'Lisa' },
    { 'admin': False, 'active': False, 'name': 'Bart' },
]

line = 1

for user in users:
    prefix = f"{line} "

    if user['admin'] and user['active']:
        prefix += "ACTIVE - (ADMIN) "
    elif user['admin']:
        prefix += "(ADMIN) "
    elif user['active']:
        prefix += "ACTIVE - "

    print(prefix + user['name'])
    line += 1
