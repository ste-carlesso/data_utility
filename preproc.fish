# to be run in data_utility directory
set list2 (ls --width=0 fomd2)
echo $list2
mkdir input
# the destination folder is called input because the new.py script expects this
mv fomd1/* input/ 

for f in $list2
    # output file starting from the second line
    tail --lines=+2 fomd2/$f >> input/$f
end

