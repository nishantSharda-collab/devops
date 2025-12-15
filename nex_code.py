1.	/* 
2.	 * C Program to Sort an Integer Array using LSDRadix Sort Algorithm
3.	 */
4.	#include <stdio.h>
5.	 
6.	int min =0, count =0, array[100]={0}, array1[100]={0};
7.	 
8.	void main()
9.	{
10.	int k,i, j, temp, t, n;
11.	 
12.	printf("Enter size of array :");
13.	scanf("%d",&count);
14.	printf("Enter elements into array :");
15.	for(i=0;i< count;i++)
16.	{
17.	scanf("%d",&array[i]);
18.	        array1[i]= array[i];
19.	}
20.	for(k =0; k <3; k++)
21.	{
22.	for(i=0;i< count;i++)
23.	{
24.	            min = array[i]%10;/* To find minimum lsd */
25.	            t =i;
26.	for(j =i+1; j < count;j++)
27.	{
28.	if(min >(array[j]%10))
29.	{
30.	                    min = array[j]%10;
31.	                    t = j;
32.	}
33.	}
34.	            temp = array1[t];
35.	            array1[t]= array1[i];
36.	            array1[i]= temp;
37.	            temp = array[t];
38.	            array[t]= array[i];
39.	            array[i]= temp;
40.	 
41.	}
42.	for(j =0; j < count;j++)/*to find MSB */
43.	            array[j]= array[j]/10;
44.	}
45.	printf("Sorted Array (lSdradix sort) : ");
46.	for(i=0;i< count;i++)
47.	printf("%d ", array1[i]);
48.	}
