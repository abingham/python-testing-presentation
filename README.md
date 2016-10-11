# Installation

First you need to install the Python stuff (probably in a virtual environment):

```
pip install -r requirements.txt
```

After this install the jupyter extensions. Note that you may need to reactivate your virtual environment for your shell to properly see the commands:

```
jupyter-nbextension install rise --py --sys-prefix
jupyter-nbextension enable rise --py --sys-prefix
```

# Running
First start the notebook.

```
jupyter notebook
```

This will open a browser window with a list of notebooks. It should only contain one, so click it.

Then look for the icon in the notebook toolbar for running the presentation.
