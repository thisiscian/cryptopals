# Cryptopals Python

My launchpad for solving the cryptopals crypto problems in python

## Setup
To try to solve these yourselves, using my tests, first:

1. Clone this repository, `git clone https://github.com/thisiscian/cryptopals/`
2. Run `python setup.py`, which pulls the freshest cryptopals info and sets up
   your `challenge` directory.

## Usage

* Pick a challenge to start on. Normally this is Challenge 1 from Set 1, 
  [Convert hex to base64](https://cryptopals.com/sets/1/challenges/1).
* Open `challenges/challenge_N.py` in your preferred editor. You'll see the 
  problem title and url in the comments at the top.
* Once you're satisfied your solution is correct, run `python test.py N` to
  check to see that it passes the testcases supplied by cryptopals.
* If you'd like to run all tests, run `python test.py` with no argument.
* You can see my solutions (such as they are) by switching to the `solutions`
  branch with `get checkout solutions`.
