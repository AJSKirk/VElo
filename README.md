# VElo

Simple python tool to rank a list of items using the Elo ranking system.
Originally built to rank lists of books for [Visiting
Enki](http://visitingenki.com), hence the name.

### Usage

```bash
python velo.py -i <infile> -o <outfile>
```

* *infile* should be a plaintext list of names, one line per name.
* *outfile* will be a .csv file of names and scores, with no header
