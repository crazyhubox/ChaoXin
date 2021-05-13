build:
	go build -o ./build/clean_mac main.go  
log_sign:
	./build/newfiles.sh sign
log_reminds:
	./build/newfiles.sh reminds
clean_logs_mac:
	./build/clean_mac -folder=../Logger/logs
clean_logs_server:
	./build/clean_logs -folder=../Logger/logs