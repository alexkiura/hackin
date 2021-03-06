#!/usr/bin/env python

import eventlet
from flask import Flask, render_template

import os
from app import create_app, db
from app.models import User, CodeSessions
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app)


def make_shell_context():
    return {app: app, db: db, User: User, CodeSessions: CodeSessions}
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':   
    manager.run()
