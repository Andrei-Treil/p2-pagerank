## Breakdown
 If it is not blatantly obvious (to a human who is not you), please indicate where in your source code the PageRank algorithm exists.
- The code for the actual pagerank algorithm (based off psuedocode): ```line 33 -> line 63```
- The rest of the code is for reading and writing to txt files

## Description 
Provide a description of system, design tradeoffs, etc., that you made. Focus on how you implemented the the loop and checked for convergence.
- The code relies on Python dictionaries for speed of accessing ranks
  - This can make sorting more difficult, but sorting does not happen frequently in the code
- For the main loop of the pagerank algorithm, I use a bool variable ```not_converged``` in a while loop
  - After a single iteration of the algorithm, I use ```math.dist()``` to find the Euclidean distance between res_pr (new pagerank) and curr_pr (old pagerank)
    - If the distance is <= tau, not_converged is set to false and I sorted res_pr by value (descending) and stored it in ```sorted_pr``` 
- Finally, curr_pr is updated to the values of res_pr

## Libraries 
List the software libraries you used, and for what purpose. Implementation must be your own work. If you are thinking of using any other libraries for this assignment, please send us an email to check first.
- sys: allowing custom input according to P2 instructions
- gzip: open the gzip files
- defaultdict: make counting inlinks and initializing pages structure easier
- math: calculate Euclidean distance

## Dependencies
Provide instructions for downloading dependencies of the code. Not expecting anything here.
- Python version >= 3.9.13

## Building 
Provide instructions for building the code.
- Download the code
- Make sure Python version >= 3.9.13

## Running
Provide instructions for running the code
- CD into the directory which contains ```pagerank.py```
- In terminal, run the command "python pagerank.py" followed by optional args: ```"inputFile" "lambda_val" "tau" "inLinksFile" "pagerankFile"```
