#include<iostream>
using namespace std;

int fib_cpp(int n) {
    if (n <= 1) {
        return n;
    } else {
        return fib_cpp(n-1) + fib_cpp(n-2);
    }
}

int main() {
    int n;
    cout << "Enter n: ";
    cin >> n;
    cout << "Fibonacci(" << n << ") = " << fib_cpp(n) << endl;
    return 0;
}
