############################# Makefile ##########################
CC=gcc

all: main

main: main.o 
	$(CC) -o main main.o
main.o: main.c
	$(CC) -o main.o -c main.c -W -Wall
clean:
	rm -rf *.o
mrproper: clean
	rm -rf main