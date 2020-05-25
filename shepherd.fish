# to be run in data_utility directory
mkdir sub
set list2 ( ls 15**.xlsx )
for f in $list2
    cp $f sub/
end
