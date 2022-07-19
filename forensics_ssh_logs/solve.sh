#!/bin/bash
grep Invalid auth.log | cut -d" " -f 9 | egrep -v 'zwischen|den|Zeilen|lesen' | tr -d "\n"
