# exabgp_stuck_example

This is test environment to reproduce ExaBGP freeze behavior.  
Just run `docker-compose up` on any linux/amd64 compatible machine with docker-compose and wait from 5 to 7 minutes.  
ExaBGP parent process will be completly stuck, with no ability to attach any kind of python debugger.  

_You'll need to export env `DOCKER_DEFAULT_PLATFORM=linux/amd64` in advance to make it work correctly with multiarch docker daemon(eg MacOS with ARM CPU)._

To reproduce it you really need a running BGP-session, thats why BIRD is running next to ExaBGP.  
This bug is well-reproducible with actual healthchecks and reasonable check intervals, but synthetic flapping `check.py` makes reproduction much faster and predictable.

Tested on kernels `4.18.0-408.el8.x86_64` and `5.15.49-linuxkit`.
