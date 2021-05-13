sign_go:
	nohup python3 -u /root/My/chaoxin/sign_main.py & 

remind_go:
	nohup python3 -u /root/My/chaoxin/remind_parse.py &

reload:
	./kill.sh
	nohup python3 -u /root/My/chaoxin/remind_parse.py &
	nohup python3 -u /root/My/chaoxin/sign_main.py & 

sync:
	rsync -azv cent:/root/My/chaoxin/ .

upload:
	rsync -azv ./ cent:/root/My/chaoxin