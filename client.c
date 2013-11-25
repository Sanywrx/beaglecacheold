#include <stdio.h>
#include <curl/curl.h>
#include <errno.h>

int main(int argp, char** argv)
{
  CURL *curl = NULL;
  CURLcode res;
  CURLINFO info;

  FILE* logFile = NULL;

  double totTime = -1;
  int i;
  int numRequests;

  int requestNumber = 0;

  if(argp != 4)
  {
    printf("Usage: prog numRequests numProcesses logFile");
    return;
  }

  numRequests = atoi(argv[1]);

  /* Open the log file */
  if( !(logFile = fopen(argv[3], "a")) )
  {
    printf("Could not open logfile:\n");
    strerror(errno);
    return;
  }

  curl = curl_easy_init();

  if(curl) {
    for(i = 0; i < numRequests; i++)
    {
      curl_easy_setopt(curl, CURLOPT_URL, "http://140.211.167.51");
      /* Perform the request, res will get the return code */ 
      res = curl_easy_perform(curl);
      requestNumber++;

      /* Check for errors */ 
      if(res != CURLE_OK)
      {
        fprintf(stderr, "curl_easy_perform() failed: %s\n",
        curl_easy_strerror(res));
      }
      else
      {
          curl_easy_getinfo(curl, CURLINFO_TOTAL_TIME, &totTime);
          fprintf(logFile, "client pid: %d Request number: %d Time taken: %f\n", 
            (int) getpid(), requestNumber, totTime);
      }
    
    }
    /* always cleanup */ 
    curl_easy_cleanup(curl);
  }
  return 0;
}