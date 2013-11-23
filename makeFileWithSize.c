#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

int main(int argv, char** argc)
{
	int i = 0;
	int numBytes = atoi(argc[2]);
	char* filePath = argc[1];
	FILE* thisFile = NULL;

	if(argv != 3)
	{
		fprintf(stdout, "Usage: progName fileToWriteTo numBytes");
		return 0;
	}

	if(thisFile = fopen(filePath, "a+"))
	{
		for(; i < numBytes; i++)
		{
			fputc('j', thisFile);
		}
		fclose(thisFile);
	}
	else
	{
		strerror(errno);
		return 1;
	}
	
	return 0;
}