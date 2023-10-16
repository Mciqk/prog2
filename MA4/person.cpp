// fib.cpp
#include <cstdlib>

class Person {
public:
    Person(int n) : n(n) {}

    long long fib() {
        if (n <= 1) {
            return n;
        }

        long long a = 0, b = 1;
        for (int i = 2; i <= n; ++i) {
            long long temp = b;
            b = a + b;
            a = temp;
        }

        return b;
    }

private:
    int n;
};

extern "C" {
    Person* Person_new(int n) { return new Person(n); }
    long long Person_fib(Person* person) { return person->fib(); }
    void Person_delete(Person* person) { delete person; }
}
