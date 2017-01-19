# This executes all slides and then clears out their results. This a) serves as
# a bit of a smoke test, b) ensure that no output from previous runs is sticking
# around, and c) ensures that all notebooks are trusted.
#
# Basic usage: ./prep_slides.sh *.ipynb

for NOTEBOOK in $*; do
    echo "[ CONVERTING" $NOTEBOOK "]"
    jupyter nbconvert --execute --inplace --to notebook $NOTEBOOK
    jupyter nbconvert --ClearOutputPreprocessor.enabled=True  --inplace --to notebook $NOTEBOOK
    jupyter trust $NOTEBOOK
done
