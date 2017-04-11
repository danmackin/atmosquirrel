#!/bin/bash
##set -x

if [ $# -ne 0 ]
then
	echo usage: $0:
	exit 0
fi

bin_dir=/bin
data_dir=/home/dan/atmosquirrel/data
logs_dir=/home/dan/atmosquirrel/logs
wx_bin_dir=/home/dan/atmosquirrel

if [ ! -d $data_dir ]
then
	echo Data directory, $data_dir, does not exist.
	exit 0
fi

log=$logs_dir/wxdata_collect-`${bin_dir}/date +%F`.log

echo Starting wxdata_collect.pl

$wx_bin_dir/wxdata_collect.pl $data_dir/msg-udp-srch.dat $data_dir/msg-tcp-nowrec-req.dat $data_dir/ewpdata.dat >> $log 2>&1
