# Quick start
1. Clone this repository on your local machine
2. Make the setup and run scripts executatables:
```
cd dev_search
chmod u+x setup.sh run.sh
```
3. Setup the installation:
```
./setup.sh
```
4. Add an alias to run `ds` (for `dev search`) to your `PATH` (in your `.bashrc` or relevant file):
```
alias ds=". /<PATH_TO_DIR>/run.sh"
# in my case I have:
# alias ds=". $HOME/dev_search/run.sh"
```

Start searching! 🎉
```
ds
```


# Dev & contribute
## Create venv
```
python3 -m venv env
```


## Activate venv
```
source env/bin/activate
```


## Install libs
```
pip3 install -r requirements.txt
```
