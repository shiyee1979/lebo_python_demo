# echo "argument $# $@"
if [ "$#" -le "0" ] || [ "$1" == "gen" ]; then
    echo "GENERATE protobuf files"
    cd ../share/proto
    protoc --proto_path=. --python_out=../../demo vision_detection.proto zss_cmd.proto zss_debug.proto
elif [ "$1" == "clean" ]; then
    echo "CLEAN protobuf files"
    rm -f *_pb2.py
else   
    echo "DO NOTHING"
    echo "Usage : $0 [gen|clean]"
fi
