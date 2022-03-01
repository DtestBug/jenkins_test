exit
echo "运行容器python执行自动化"
pwd
ls
python main.py
docker run --rm -w=$WORKSPACE --volumes-from=jenkins python:latest
echo "python执行自动化执行成功"