librot13.so: librot13/rot13.c librot13/rot13.h
	ggc -shared -o librot13.so librot13/rot13.c

rot13: librot13.so rot13encoder/main.c
	gcc -I ./librot13 -o rot13 -L. rot13encoder/main.c -lrot13

rot_aas: librot13.so rot13encoder/rot_aas.c
	gcc -I ./librot13 -L. -o rot_aas rot13encoder/rot_aas.c -lrot13

install: rot13 librot13.so
	install rot13 /usr/local/bin/rot13
	install rot_aas /usr/local/bin/rot_aas
	install librot13.so /lib64/

ALL: rot13 rot_aas
