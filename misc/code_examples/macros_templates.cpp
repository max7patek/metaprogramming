

#include <iostream>
#include <algorithm>

#define max(a, b) (a > b ? a : b)
#define MAXINT 2147483647
#define MAX(n) (n == MAXINT)
#define SQUARE(x) x * x
#define SQUARE2(x) ((x)*(x))
#define RELU(x) if (x < 0) x = 0


using namespace std;


template <int X, int Y> // X Y must be effectively const
struct Adder { 
	enum { result = X + Y }; 
};			//	^^ must be constexpr

template <unsigned int n> // n must be constexpr
struct Factorial {
	enum { value = n * Factorial<n - 1>::value }; 
}; 			//  ^^^ must be constexpr ^^^
template <> 
struct Factorial<0> {  // base case specialization
	enum { value = 1 }; 
};


int main() {
    cout << MAXINT << endl;
    cout << MAX(2147483647) << endl;
    cout << SQUARE(1 + 1) << endl;
    int x = 1;
    cout << SQUARE2(++x) << endl;
    if (true) 
        RELU(x);
    else
        cout << "unreachable" << endl;
    cout << x << endl;
    cout << max(x, 5) << endl;
    cout << Adder<3, 4>::result << endl;
    cout << Factorial<10>::value << endl;
    return 0;
}