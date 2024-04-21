#!/bin/bash

STREAM_JAR=$1
INPUT=$2
OUTPUT=$3
LOCAL_INP=$4

MAPPER_SCRIPT="mapper.py"
REDUCER_SCRIPT="reducer.py"

# Set the pattern
PATTERN=$5

# Delete existing output directory
# hadoop fs -rm -r -skipTrash "$OUTPUT_DIR"

hdfs dfs -rm -r /output
hdfs dfs -rm -r /input

hdfs dfs -mkdir -p /user/root
hdfs dfs -put ./input/${INPUT}
# Run Hadoop Streaming
hadoop jar $STREAM_JAR \
    -files "$MAPPER_SCRIPT,$REDUCER_SCRIPT" \
    -mapper "python3 mapper.py" \
    -reducer "python3 reducer.py" \
    -input $INPUT \
    -output $OUTPUT \
    -cmdenv PATTERN=$PATTERN \
    -numReduceTasks 3

# Display the output
hadoop fs -cat $OUTPUT/part-*