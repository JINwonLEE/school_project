MPICC  = mpicc
MPICXX = mpiic++
MPIFC  = mpiif77

MPICFLAGS = -O3

TARGETS = mergesort

all : $(TARGETS)

mergesort : mergesort.c
	$(MPICC) $(MPICFLAGS) mergesort.c -o mergesort

clean :
	rm -rf $(TARGETS) 

