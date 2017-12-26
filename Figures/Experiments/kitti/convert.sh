for f in *.svg; do
  mkdir ./pdf
  inkscape ./"$f" --export-pdf=./pdf/"${f%.jpg}.pdf"
done

a=1
for i in ./pdf/b-*.pdf; do
  new=$(printf "./pdf/b-%04d.pdf" "$a") #04 pad to length of 4
  mv -i -- "$i" "$new"
  let a=a+1
done

a=1
for i in ./pdf/bird-*.pdf; do
  new=$(printf "./pdf/bird-%04d.pdf" "$a") #04 pad to length of 4
  mv -i -- "$i" "$new"
  let a=a+1
done
