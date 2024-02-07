//
// Created by Shrikrishna Bhat on 2/6/24.
//

#include <iostream>
#include <unordered_set>
#include <cassert>

using namespace std;

class Solution {
public:
    static bool containsDuplicate(vector<int>&nums){
        unordered_set<int> s;

        for(int num : nums){
            if(s.find(num) != s.end()) {
                return true;
            }
            s.insert(num);
        }
        return false;
    }
};

class SolutionTest {
public:
    static void isFalse() {
        Solution solution;
        vector<int> nums = {1,2,3,4,5};
        assert(solution.containsDuplicate(nums) == false);
    }

    static void isTrue(){
        Solution solution;
        vector<int> nums ={1,2,3,1};
        assert(solution.containsDuplicate(nums) == true);
    }
};
int main() {

    SolutionTest::isFalse();
    SolutionTest::isTrue();
    cout << "All tests successfully passed" << endl;
    return 0;
}

