echo $(date +%F%n%T) > time

function rand(){   
    min=$1   
    max=$(($2-$min+1))   
    num=$(date +%s%N)   
    echo $(($num%$max+$min))   
}   
     
rnd=$(rand 1 10)   
echo $rnd   

if (( $rnd >5  ))
then
    git add .
    git commit -m "init"
    git push

fi 
