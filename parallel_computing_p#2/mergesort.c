#include <stdio.h>
#include <mpi.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int* merge(int *A, int *B, int asize, int bsize);
void mergesort(int *A, int min, int max);
int power(int i, int j);




int* sorted_data;
double start_time, stop_time;
int n;
int* merge(int *A, int *B, int asize, int bsize) {
	// TODO: fill in the code here to merge the sorted arrays
	int i = 0;
	int j = 0;
	int* tmpArray = (int *)malloc( (asize + bsize) * sizeof(int));
	int ind = 0;
	while(i < asize || j < bsize) {
		if(i == asize) {
			while(j < bsize){

				tmpArray[ind] = B[j];
				ind++;j++;
			}	
		}
		else if(j == bsize) {
			while(i < asize) {
				tmpArray[ind] = A[i];
				ind++;i++;
			}
		}
		else if(i < asize && j < bsize){
			if(A[i] < B[j]){
				tmpArray[ind] = A[i];
				ind++;i++;
			}
			else {
				tmpArray[ind] = B[j];
				ind++;j++;
			}
		}
	}

	return tmpArray;
	free(tmpArray);
}

void mergesort(int *A, int min, int max)			
{
	// TODO: fill in the code here to recursive divide the array
	// into two halves, sort and merge them
	int* tmp;
	tmp = (int *)malloc((max-min+1) * sizeof(int)); 
	if( min < max ) {
		int i, j;
		int mid = (min + max) / 2;

		mergesort(A, min, mid);
		mergesort(A, mid + 1, max);
		int* B = (int *)malloc( (mid - min + 1) * sizeof(int));
		int* C = (int *)malloc( (max - mid) * sizeof(int));
		for(i = min; i <= mid ; i++) 
			B[i-min] = A[i];
		for(j = mid + 1; j <= max; j++) 
			C[j-mid-1] = A[j];
		tmp = merge(B, C, mid - min + 1, max - mid);
		for(i = min; i <= max; i++) {
			A[i] = tmp[i-min];	
		}
		free(B);
		free(C);
	}
}

int main(int argc, char **argv)
{
	int* data;
	int* recv_data;
	int m, id, p, i, output;

	MPI_Status status;

	if (argc != 2) {
		printf("usage: %s <num_items>\n", argv[0]);
		return 1;
	}

	// Number of items to be sorted
	n = atoi(argv[1]);

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &id);
	MPI_Comm_size(MPI_COMM_WORLD, &p);
	int size = n / p;
	sorted_data = (int *)malloc(n * sizeof(int));


	if(id==0)							//MASTER
	{
		// data generation
		srandom(0);
		// Make sure that n is a multiple of p
		data = (int *)malloc(n*sizeof(int));
		for(i=0; i<n; i++){
			data[i] = random();
		}
	}
	recv_data = (int *)malloc(size * sizeof(int));

	start_time = clock();
	MPI_Scatter(data, size, MPI_INT, recv_data, size, MPI_INT, 0, MPI_COMM_WORLD); 
	MPI_Barrier(MPI_COMM_WORLD);
	// TODO: fill in the code here to 
	// (1) distribute the data across the processes
	// (2) sort the data
	// (3) merge sorted data

	mergesort(recv_data, 0, size-1);
	int level = 1;
	int activate_process = 1;
	int *partner_data; 
	int *recv_data2;
	while (p != 1 &&size < n) {
		partner_data = (int *)malloc(size * sizeof(int));
		if(activate_process == 1) {
			int j;
			int oper = power(2, level);
			if (id % oper != 0) {
				MPI_Send(recv_data, size, MPI_INT, id - power(2,level-1), level, MPI_COMM_WORLD);
				free(partner_data);
				break;
			}
			else {
				MPI_Recv(partner_data, size, MPI_INT, id + power(2, level -1), level, MPI_COMM_WORLD, &status);
				recv_data2 = merge(recv_data, partner_data, size, size);
				recv_data = (int *)realloc(recv_data2, 2* size *sizeof(int));
				level++;
				size *= 2;
			}	
		}
		free(partner_data);
		
	}

	if(size == n){
		int j;
		for(j = 0; j < n; j++)
			sorted_data[j] = recv_data[j];
	}

	stop_time = clock();

	if (id == 0)
	{
		FILE * fp;
		int i;

	//	for(i = 0;  i < n ; i++) printf("[DEBUG] %d sorted_data %d\n",i, sorted_data[i]);
		printf("%d procs, %d items, %f seconds\n", p, n, (stop_time-start_time)/CLOCKS_PER_SEC);

		if(sorted_data==NULL){
			printf("error: sorted_data does not exist\n");
		}
		else{
			for(i = 0; i < n - 1; i++){
				if(sorted_data[i] > sorted_data[i+1])
					printf("error: sorted_data[%d] is greater than sorted_data[%d]\n",i,i+1);
			}
		}
		free(data);
	}
	free(recv_data);
	free(sorted_data);
	MPI_Finalize();
}

int power(int i, int j) {
	int k;
	int t = 1;
	for( k = 0; k < j; k++)
		t *= i;
	return t;
}	
