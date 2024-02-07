//
// Created by Shrikrishna Bhat on 2/7/24.
//

#include <iostream>
#include <cassert>

using namespace std;

class Solution {
public:
    static bool isAnagram(string s, string t){
        if(s.size() != t.size()){
            return false;
        }

        unordered_map<char, int> smap;
        unordered_map<char, int> tmap;

        for(int i=0; i < s.size(); i++){
            smap[s[i]] ++;
            tmap[t[i]] ++;
        }

        return smap == tmap;
    }
};

class SolutionTest {
public:
    static void isTrue(){
        Solution solution;
        string s = "anagram";
        string t = "nagaram";
        assert(solution.isAnagram(s,t) == true);
    }

    static void isFalse(){
        Solution solution;
        string s = "rat";
        string t = "bat";
        assert(solution.isAnagram(s,t) == false);
    }
};
int main(){
    SolutionTest::isTrue();
    SolutionTest::isFalse();
    cout << "All tests passed successfully" << endl;
}