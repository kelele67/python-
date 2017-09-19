#include <iostream>
#include <cmath>
using namespace std;
//int add(int a, int b) {
//	return a + b;
//}
int fibonacci(int n)  
{  
	int f1 = 2, f2 = 3, fn = 0;  
	if (n < 0)  
	{  
		return fn;  
	}  
	else if (n == 1)  
	{  
		return f1;  
	}  
	else if (n == 2)  
	{  
		return f2;  
	}  
	else  
	{  
		//迭代实现  
		for (int i = 2; i < n; i++)  
		{  
			fn = f1 + f2;  
			f1 = f2;  
			f2 = fn;  
		}  
  
		return fn;  
	}  
}

int Func(int n) { 
	if(n<0) {  return -1; } 
	if(n==0) {  return 0; } 
	return pow(2,(n/2))+pow(2,((n-(n/2)))-1);
} 
int main(int argc, char *argv[]) {
//	int x = 6;
//	int y = 7;
//	int z = 8;
//	int r = add(add(x, y), z--);
//	cout << r;
//const int i = 0;
//int *j = (int *)&i;
//*j = 2;
//cout << i << "," << *j ;
//int a[3][4]={1,2,3,4,5,6,7,8,9,10};
//(*p)[4] = a;
//*q[3] = {a[0], a[1], a[2]};
//**r = q;
//char a[10];
//cout << sizeof(a);
//int a = 1;
//int b = *(int*)(&(*(float *)(&a)));
//float c = (*(float *)(&a));
//cout << b;
//cout << " ";
//cout << c;
//int i = 1;
//sizeof(i++);
//cout << i;
//cout << sizeof(int) << sizeof(float) << sizeof(double) << sizeof(char *) << sizeof(long);
//int x = fibonacci(13);
//int y = Func(3);
//cout << y;
//cout << x;
//unsigned int a = 0x1234;
//unsigned char b = *(unsigned char *)&a;
//cout << b;
struct T {};
cout << sizeof(T);
return 0;
}