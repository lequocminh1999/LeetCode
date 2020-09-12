#https://leetcode.com/problems/nim-game/

class Solution {
public:
    bool f[10001];
    bool canWinNim(int n) {
        if(n%4==0) return false;
        else return true;
        
    }
};