#include <bits/stdc++.h>
using namespace std;

unordered_map<string, vector<string>> m;

vector<string> contact(string word, vector<string> prev){
    for(int i=0;i<prev.size();++i){
        prev[i]+= " " + word;
    }
    return prev;
}

vector<string> wordBreak(string s, unordered_set<string>& dict) {
    vector<string> res;
    if (m.count(s)) 
        return m[s]; 
    if (dict.count(s)){ 
        res.push_back(s);
    }
    for (int i = 1; i < s.size(); i++){
        string word = s.substr(i);
        if (dict.count(word)){
            string str = s.substr(0,i);
            vector<string> prev = contact(word, wordBreak(str,dict));
            res.insert(res.end(), prev.begin(), prev.end());
        }
    }
    m[s]=res; 
    return res;
}

int countSpace(string s) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == ' ') {
        count++;
        }
    }
    return count;
}

void mincut(const string& str, const set<string>& dict)
{   
    int minSpace = 0;
    vector<string> res = wordBreak(str, dict);
    for (int i = 0; i < res.size(); i++) {
        if (countSpace(res[i]) < minSpace) {
            minSpace = countSpace(res[i]);
        }
    }
    return minSpace;
}


int main(int argc, const char * argv[])
{
    string strS;
    string dictStr;
    int nDict;
    set<string> dict;
    
    cin>>strS;
    cin>>nDict;
    for (int i = 0; i < nDict; i++)
    {
        cin>>dictStr;
        dict.insert(dictStr);
    }

    mincut(strS, dict);
    
    return 0;
}