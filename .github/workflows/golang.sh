#!/bin/bash

for dir in $(find . -type d -name '*'); do
    if [[-f "$dir/go.mod"]]; then
        echo "Running Tests in Directory: $dir"
        cd "$dir"
        go test -v ./...
        cd -
    fi

done