# causal-cmd-python-wrapper

This repository shows how to build command line calls to causal-command (that is, to run Tetrad algorithms at the command line) and use os.sys() calls in Python to run the commands, obtain the causal-command output files, and then load these outputs into causal-learn Python general graph objects using the txt2generalgraph command in causal-learn.

To run this, you will need to do the following:

1. Install Python and maybe possibly some IDE like PyCharm.
1. Install the causal-learn Python package usign pip--i.e., make sure pip is installed and then type "pip install causal-learn".
1. Install a recent Java JDK. Version 1.8 is assumed, but later versions should work fine. Doesn't have to be Oracle, could be Amazon Corretto for instance.
1. Clone this repository (or in PyCharm, just make a project using the URL of this repository, https://github.com/cmu-phil/causal-cmd-python-wrapper.
1. In your IDE (or at the command line in Python), run the file "test_tetrad_cmd_algs.py". This should run the included example file/graph and output the causal-cmd result, time-stamped, in the "causal_cmd_results" directory, then load up the graph in that result and print it, along with some graph statistics.
1. By varying the commenting in the file "test_tetrad_cmd_algs.py" you can get causal-cmd to run various algorithms.

Once you get the pattern, you should be able to modify the code for various more specific purposes.
