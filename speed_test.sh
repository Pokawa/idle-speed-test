#!/bin/bash

script_path=`realpath $0`

remove_schedule () {
	crontab -l | grep "#speedtest" -v > tmp
	crontab tmp && echo successfully removed
	rm tmp
}

setup_schedule () {
	remove_schedule
	crontab -l > tmp
	echo "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/pi/bin #speedtest" >> tmp
	echo "*/$1 * * * * $script_path test #speedtest" >> tmp
	crontab tmp && echo successfully set up
	rm tmp
}

perform_test (){
	file="`dirname $script_path`/`iwgetid -r`.csv"
	if [ ! -f $file ]; then
        	echo time,`speedtest --csv-header | cut -f 3,6,7,8 -d "," | tr '[:upper:]' '[:lower:]'` > $file
	fi
	{ echo -n `date +"%F %T"`, & speedtest --csv | cut -f 3,6,7,8 -d ","; } >> $file
}

print_help () {
	echo speed_test setup TIME_SPAN
	echo "    setup schedule in crontab with TIME_SPAN minutes span between tests"
	echo 
	echo speed_test remove 
	echo "    remove setup"
	echo 
	echo speed_test test
	echo "    perform a test"
	echo 
	echo speed_test help
	echo "    show this message"
}

case $1 in
	"remove") remove_schedule ;;
	"setup") setup_schedule $2 ;;
	"test") perform_test ;;
	"help") print_help ;;
	*) perform_test	
esac
