#!/bin/bash

# 启动 rsync 同步任务
rsync -av --delete . /python_api/

# 启动 inotifywait 监控文件变化并同步到容器内
while inotifywait -r -e modify,create,delete,move .; do
    rsync -av --delete . /python_api/
done
