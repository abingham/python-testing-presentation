This is a presentation/workshop on various testing technologies in Python. It's built using (RISE)[https://github.com/damianavila/RISE], a jupyter notebook-based presentation system using reveal.js.

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

This will open a browser window with a list of notebooks. The relevant notebooks are:

 - unittest.ipynb
 - mock.ipynb
 - pytest.ipynb
 - hypothesis.ipynb
 - cosmic-ray.ipynb

Click on any of these to open them in your browser.

Then look for the icon in the notebook toolbar for running the presentation.
(Hint: it looks a bit like a histogram.)
