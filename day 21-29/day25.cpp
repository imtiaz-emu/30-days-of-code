/*
Problem Statement: https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
Author: Imtiaz Emu
Language: C++
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int is_prime(long number){
    if(number == 1) return false;
    if(number == 2) return true;
    if(number % 2 == 0) return false;
    for(long J = 3; J*J <= number; J+=2){
        if(number % J == 0)
            return false;
    }
    return true;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    long test, T, number;
    cin >> test;
    for(T = 0; T < test; T++){
        cin >> number;
        if(is_prime(number)){
            cout << "Prime" << endl;
        }else{
            cout << "Not prime" << endl;
        }
    }
    return 0;
}
