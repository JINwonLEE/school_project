mkdir results
for p in 1 2 4 8 16 32
do
  n=`echo "($p-1)/16+1" | bc`
  qsub -V -N mpi.$p -o results/mpi.$p.o -e results/mpi.$p.e -v p=$p -l nodes=$n:ppn=16 -l walltime=01:00:00 ./run.sh 

done
