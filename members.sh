#!/bin/bash -

# 20160314 - ccaputo
#
# Convert tab-separated file members.txt to members.md
#
# members.txt
#
#   orgname\tasn
#   orgname\tasn
#
# Handled escaping for pipe character for markdown tables.
#

INPUT=members.txt
TARGET=members.md
TEMPLATE=members.md.template
COUNT=`cat $INPUT | wc -l | tr -d " "`

rm -f $TARGET.new
cat $TEMPLATE | sed "s/MEMBERCOUNT/$COUNT/g" > $TARGET.new

cat $INPUT              |
    sed 's/|/\&#124;/g' |
    sort -f             |
    tr '\t' '|'         >> $TARGET.new && mv $TARGET.new $TARGET

