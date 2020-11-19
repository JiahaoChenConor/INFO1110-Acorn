#! /usr/bin/env sh
echo "##########################"
echo "### Running e2e tests! ###"
echo "##########################\n"
count=0 # number of test cases run so far

# Assume all `.in` and `.out` files are located in a separate `tests_e2e` directory

#  single test
#  python3 run.py tests_e2e/1.config play < tests_e2e/1.in | diff - tests_e2e/1.out
#  about the .out file,
#  each time you follow the new map, put the updated first line after the last line printed before the update
#  give a new line at the end of .out file

for test in tests_e2e/*.in; do
    name=$(basename $test .in)
    expected=tests_e2e/$name.out
    filename=tests_e2e/$name.config

    # if I want to use variable, use $ before the name
    python3 run.py $filename <  $test | diff - $expected || echo "Test $name: failed!\n"
    count=$((count+1))
done

echo "Finished running $count tests!"

