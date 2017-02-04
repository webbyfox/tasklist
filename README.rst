TaskList
========

A short description of the project.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: MIT


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ py.test

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Deployment
----------

The following details how to deploy this application.


Heroku
^^^^^^

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html


TODO
^^^^

* *Build a task list application in django.*
* *Users will first login to their accounts.*
* *Once they login, then should see a list of everyone’s tasks.*
* *There is an “Add” button to add a new todo item.*
* You can via the UI “Edit”, “Mark Done” or “Delete” a task.
* Edit: Is editing the task name, description and status (done/undone) (only your own)
* Mark Done: is changing the status of a task to “done” and record who did it.
* Delete: is deleting a task (only your own)
* There is a “Hide Completed tasks” button, click on that to filter out todo items that are already done.
* Tests for the application. (We value good testing over complicated features)

Additional notes:
^^^^^^^^^^^^^^^^^
* The frontend choices are entirely up to you.
* There is no time constraint, when you’re happy with it, send it to us as well as how much time you spent on it.
* Any extra feature you can add will be appreciated
* Whatever you do send please do it to the best of your abilities, please be proud of what you send. Quality > Quantity.
* (Optional) We appreciate when code is deployed somewhere public.
* Setup of the project should be easy and detailed.
