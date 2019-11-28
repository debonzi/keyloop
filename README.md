# Key Loop
## Development
 * Create a 3.7 python virtual env using you prefered tool and activate it

```
$ pip install -e .[dev]
$ pre-commit install
```

The code style is done by *black* and there is a pre-commit hook that runs it and will stop the commit in case changes are made by *black*. Black should be run before commit and the pre commit hook is there just to help you in case you forget it.
If that in mind, the workflow would be something like:

```
$ # Do your coding
$ black .
$ git diff # check your work
$ git add <files>
$ git commit
```
