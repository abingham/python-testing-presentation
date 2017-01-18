# This executes all slides and then clears out their results. This a) serves as
# a bit of a smoke test, b) ensure that no output from previous runs is sticking
# around, and c) ensures that all notebooks are trusted.

for NAME in Introduction unittest mock pytest hypothesis cosmic-ray; do
    FNAME=$NAME.ipynb
    echo "*** CONVERTING" $FNAME
    jupyter nbconvert --execute --inplace --to notebook $FNAME
    jupyter nbconvert --ClearOutputPreprocessor.enabled=True  --inplace --to notebook $FNAME
    jupyter trust $FNAME
done
