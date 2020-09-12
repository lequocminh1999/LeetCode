#https://leetcode.com/problems/hamming-distance/

class Solution {
public:
    int hammingDistance(int x, int y) {
        int cnt=0;
        for(int i=0;i<31;++i){
            if((x>>i)%2!=(y>>i)%2) ++cnt;
        }
        return cnt;
    }
};