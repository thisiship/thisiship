#!/bin/bash

PERSONAL_PRIO="8"

echo "Personal Promotion. Set to Priority $PERSONAL_PRIO:"
for promoted in "elephino" "the english project" "the forest dwellers" "the honey smugglers" "honey smugglers"
do
	echo $promoted
	#																	need to use variable here
	grep -il "$promoted" jsondump/* | xargs sed -i -e 's/"priority": "[0-9]"/"priority": "8"/g'
done

