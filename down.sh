declare -i i=11

while read -r line;
do
    # result=$(echo $line | sed -n 's/.*\(seg.*ts\).*/\1/p')
    # curl "$line" --output "$result"
    curl "$line" --output "$i.ts"
    ((++i))
done

python3 script.py $1
mv $1 ../
rm *.ts