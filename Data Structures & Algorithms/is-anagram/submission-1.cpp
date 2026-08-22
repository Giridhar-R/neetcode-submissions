class Solution {
public:
    bool isAnagram(string s, string t) {

        if(s.size()!=t.size()){
            return false;
        }

        sort(s.begin(), s.end(), greater<char>());
        sort(t.begin(), t.end(), greater<char>());

        if(s==t){
            return true;
        }
        else {
            return false;
        }






        
    }
};
