# to be run in data_utility directory
set list2 (ls --width=0 fomd2)
echo $list2
mkdir fomd3
mv fomd1/* fomd3/ 

for f in $list2
    # output file starting from the second line
    tail --lines=+2 fomd2/$f >> fomd3/$f
end

