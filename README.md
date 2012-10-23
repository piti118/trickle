<pre>
usage: trickle [-h] [--simulate] [-n MAXQUE] [-q QUE] jobfiles [jobfiles ...]

positional arguments:
  jobfiles              job files

optional arguments:
  -h, --help            show this help message and exit

  --simulate            turn on simulation mode

  -n MAXQUE, --maxque MAXQUE
                        execute commands only if the que has less than this
                        job in que

  -q QUE, --que QUE     que name to determine the job in the que. If not
                        specified, it used the sum of all que
</pre>
