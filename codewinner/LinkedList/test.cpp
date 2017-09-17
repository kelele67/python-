#include <iostream>

using namespace std;

// 教科书上的实现
class Singleton {
	private:
		static Singleton *instance;
	protected:
		Singleton() {}
	public:
		Singleton *getInstance(){};
};
Singleton* Singleton::instance = NULL;
Singleton* Singleton::getInstance() {
	if (instance == NULL) {
		instance = new Singleton();
	}
	return instance;
}
// 改进，用时间换空间 懒汉模式
class Singleton {
	private:
		static Singleton *instance;
		Singleton() {}
	pulbic:
		static Singleton *getInstance() {
			if (instance == NULL) {
				instance = new Singleton();
			}
			return instance;
		}
};
// 改进懒汉式的，析构
class Singleton {
	private:
		static Singleton *instance;
		Singleton() {}
		class GC {
			public:
				~GC() {
					if (Singleton::instance) {
						delete Singleton::instance;
						}
		};
		static GC gc;
	public:
		static Singleton *getInstance() {
			if (instance == NULL) {
				instance = new Singleton();
			}
			return instance;
		}
};

// 饿汉式，空间换时间 局部静态变量
class Singleton {
	private:
		Singleton() {}
	public:
		static Singleton &getInstance() {
			static Singleton instance;
			return instance;
		}
		
};
// 但是在类拷贝调用的时候，编译器会自动生成一个类的默认构造函数
// 所以要返回指针
class Singleton {
	private:
		Singleton() {}
	public:
		static Singleton *getInstance() {
			static Singleton instance;
			return &instance;
		}
};

// 或者重载拷贝运算符
class Singleton {
	private:
		Singleton() {}
		Singleton(const Singleton&);
		Singleton &operator=(const Singleton&);
	public:
		static Singleton &getInstance() {
			static Singleton instance;
			return instance;
		}
}
int main(int argc, char *argv[]) {
	
}