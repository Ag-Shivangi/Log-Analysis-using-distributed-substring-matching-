#!/usr/bin/bash 

SS_CHUNCK_SIZE=$1
SS_FILE=$2
PATTERN_CHUNK_SIZE=$3
PATTERN_FILE=$4

MAP_RED_ALGO=$5

NUM_REDUCER=$6

python3 make_input_ready.py ${SS_CHUNCK_SIZE} ${SS_FILE} ${PATTERN_CHUNK_SIZE} ${PATTERN_FILE} tmp_input.txt
echo "Chunking done"

hadoop fs -rm -r /input_files
hadoop fs -rm -r /output_files
hadoop fs -mkdir /input_files
hadoop fs -put tmp_input.txt /input_files
echo "Hadoop files added"

hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -numReduceTasks ${NUM_REDUCER} -input /input_files -output /output_files -mapper ./${MAP_RED_ALGO}/mapper.py -file ./${MAP_RED_ALGO}/mapper.py -reducer ./${MAP_RED_ALGO}/reducer.py -file ./${MAP_RED_ALGO}/reducer.py 
echo "Map reduce complete"

hadoop fs -cat /output_files/part-* > tmp_output.txt
echo "Copied output to local"

echo "Starting index of matches:"
python3 finalize_output.py < tmp_output.txt`:`

rm tmp_input.txt tmp_output.txt
