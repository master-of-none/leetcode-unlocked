//
// Created by Shrikrishna Bhat on 2/7/24.
//

#include <iostream>
#include <cassert>
using namespace std;

class Solution {
public:
    static vector<int> twoSum(vector<int>&nums, int target){
        unordered_map<int, int> map;

        for(int i=0; i<nums.size(); i++){
            int diff = target - nums[i];

            if(map.find(diff) != map.end()){
                return {map[diff], i};
            }
            map.insert({nums[i], i});
        }
        return {};
    }
};

class SolutionTest {
public:
    static void test1(){
        Solution solution;
        vector<int> nums = {2,7,11,15};
        vector<int> expected = {0,1};
        assert(solution.twoSum(nums, 9) == expected);
    }

    static void test2(){
        Solution solution;
        vector<int> nums = {3,2,4};
        vector<int> expected = {1,2};
        assert(solution.twoSum(nums, 6) == expected);
    }


    static void test3(){
        Solution solution;
        vector<int> nums = {3,3};
        vector<int> expected = {0,1};
        assert(solution.twoSum(nums, 6) == expected);
    }
};

int main(){
    SolutionTest::test1();
    SolutionTest::test2();
    SolutionTest::test3();
    cout << "All tests passed successfully\n";
}
