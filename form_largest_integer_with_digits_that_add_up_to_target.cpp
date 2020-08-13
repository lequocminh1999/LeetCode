//https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/

class Solution {
public:
    int f[5001];
    stringstream ss;
    string tostr(int i){
        ss.str("");
        ss<<i;
        return ss.str();
    }
    string largestNumber(vector<int>& cost, int target) {
        f[0]=1;
        
        string s="";
        for(int i=1;i<=target;++i) f[i]=0;
        for(int j=0;j<9;++j){
            for(int i=0;i<=target;++i){
                if((i+cost[j])<=target && f[i]>0){
                    f[i+cost[j] ]=max(f[cost[j]+i],f[i]+1);
                }
            }
        }
        int cur=target;
        if(f[target]==0) return "0";
        
        while(cur>0){
            for(int i=9;i>=1;--i){
                if(cost[i-1]>cur) continue;
                if(f[cur]==(f[cur -cost[i-1] ]+1)){
                    cur=cur-cost[i-1];
                    s=s+tostr(i);
                    break;
                }
            }
        }
        return s;
    }
};