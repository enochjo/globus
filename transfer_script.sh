#!/bin/bash

# module load globus-tools
source_ep=ba87aabe-30f6-433d-b4a5-19434c595e0f
dest_ep=6bdc7956-fc0f-4ad2-989c-7aa5ee643a79
globus transfer $source_ep $dest_ep --batch plist_252068.txt
