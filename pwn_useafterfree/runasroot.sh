#!/bin/sh
echo "core.%p" > /proc/sys/kernel/core_pattern
ulimit -c unlimited
