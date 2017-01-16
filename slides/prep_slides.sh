for NAME in Introduction unittest mock pytest hypothesis cosmic-ray; do
    FNAME=$NAME.ipynb
    echo "*** CONVERTING" $FNAME
    jupyter nbconvert --execute --inplace --to notebook $FNAME
    jupyter nbconvert --ClearOutputPreprocessor.enabled=True  --inplace --to notebook $FNAME
    jupyter trust $FNAME
done
