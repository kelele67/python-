#include <iostream>

using namespace std;
bool isGroupSum(int *arr, int target, int start){
	/*Base condition*/
	if(start >= arr.length)
	     return (target == 0);
 
	/*we found the target sum, return true*/
	if(target == 0)
	     return true;
 
	/*else, check if sum can be obtained by any of the following
		1) Including the current element
		2) Excluding the current element*/
	return isGroupSum(arr, target - arr[start], start+1)
		   || isGroupSum(arr, target,start+1);
}

bool findSum(int *arr, int n, int target)
{
	int sum = arr[0], start = 0, i;
	for (i = 1; i <= n; i++)
	{
		while(sum > target && start < i-1)
		{
			sum = sum - arr[start];
			start++;
		}
		if(sum == target)
		{
			return true;
		}
		if(i < n)
		  sum = sum + arr[i];
	}
	return false;
}

int maxTime(int *arr, int n, int time) {
	
}

int main(int argc, char *argv[]) {
	
}