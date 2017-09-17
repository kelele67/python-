#include <iostream>

using namespace std;
int add(int a, int b) {
	return a + b;
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
cout << sizeof(int) << sizeof(float) << sizeof(double) << sizeof(char *) << sizeof(long);
return 0;
}