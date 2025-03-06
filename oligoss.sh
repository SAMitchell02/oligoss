#!/bin/bash

while getopts "i:o:r:" flag
    do
        case "${flag}" in
            i) INPUT_PARAMS=${OPTARG};;
            o) OUTPUT_DIR=${OPTARG};;
            r) RIPPER=${OPTARG};;
        esac
    done

if [ -z "${INPUT_PARAMS}" ]; then
    echo "No input parameters (-i) given"
    return 1
fi
if [ -z "${OUTPUT_DIR}" ]; then
    echo "No output directory (-o) given"
    return 1
fi
if [ -z "${RIPPER}" ]; then
    echo "No input data directory (-r) given"
    return 1
fi

echo $INPUT_PARAMS
echo $OUTPUT_DIR
echo $RIPPER

docker run -it --mount source=$INPUT_PARAMS,target=/input_parameters.json,type=bind \
    -v $RIPPER:/data \
    -v $OUTPUT_DIR:/output \
    oligoss:latest