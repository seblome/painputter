# PaInputter 1.0.0
The PaInputter allows manual addition of estimates to concatenated PsychoPy experiment data.
The current version is adapted to a specific PsychoPy project used to investigate conditioning effects in pain percecption. 
Future versions will open up the program for a broader usage.

# Instructions
Download PaInputter and place a /data/ folder inside the workspace in which you will place all .psydat files.
The PaInputter will automatically generate a .csv dataset containing the specified estimates of interest from the chosen subject.
For every new participant, the dataset will be concatenated with the new data, which allows for hypothesis testings of interest.

# Required external python modules
- psychopy
- numpy
- pandas

# Future functions
- Storage of multiple files
- Selection of items to keep from .psydat file in new dataset
- Specifying estimates of interest to be added
