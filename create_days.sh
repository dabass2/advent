cd 2022

for i in {1..25}
do
  echo "Creating day $i"
  mkdir ./day$i
  touch ./day$i/test.file
  touch ./day$i/input.file
  cp ../template.py ./day$i/
done