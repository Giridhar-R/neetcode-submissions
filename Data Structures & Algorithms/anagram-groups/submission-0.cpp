class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        if(strs.size()==0){
            return {{}};
        }
        else if (strs.size()==1){
            return{{strs[0]}};
        }

        else {

            unordered_map<string, vector<string>> map;
            

            for(const string& s : strs){

                string key = s;

                sort(key.begin(),key.end());

                
                map[key].push_back(s);
            }

            vector<vector<string>> anagram;
            anagram.reserve(map.size());

            for(auto& it : map){
                anagram.push_back(move(it.second));
            }


            return anagram;
        }

        
    }
};
