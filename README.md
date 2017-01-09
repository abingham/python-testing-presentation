This is a presentation/workshop on various testing technologies in Python. It's built using [RISE](https://github.com/damianavila/RISE), a jupyter notebook-based presentation system using reveal.js.

# Installation

First you need to install the Python stuff (probably in a virtual environment):

```
pip install -r requirements.txt
```

## Installing the RISE slideshow extension

After this install the RISE jupyter extensions. Note that you may need to
reactivate your virtual environment for your shell to properly see the commands:

```
jupyter nbextension install rise --py --sys-prefix
jupyter nbextension enable rise --py --sys-prefix
```

## Installing the Jupyter "contrib" extensions

If you want the slideshows to automatically run certain initialization cells
(hint: you probably do) then you need to install the "initialization cells"
extension from the Jupyter contrib extensions:

```
jupyter contrib nbextension install --user
jupyter nbextension enable init_cell/main
```

Get more info on these extensions
at
[the project page](https://github.com/ipython-contrib/jupyter_contrib_nbextensions).

**NB:** Running initialization cells requires that you "trust" the notebooks.
You'll probably need to do this for each slideshow notebook for which you want
initialization cells.

# Running
First start the notebook.

```
cd slides
jupyter notebook
```

This will open a browser window with a list of notebooks. The relevant notebooks are:

 - unittest.ipynb
 - mock.ipynb
 - pytest.ipynb
 - hypothesis.ipynb
 - cosmic-ray.ipynb

Click on any of these to open them in your browser.

Then look for the icon in the notebook toolbar for running the presentation.
(Hint: it looks a bit like a histogram.)
