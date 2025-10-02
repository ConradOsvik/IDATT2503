#include <iostream>
#include <string>

using namespace std;

string replace_string(const string &str) {
    string result;
    for (char c : str) {
        switch (c) {
            case '<': result += "&lt;"; break;
            case '>': result += "&gt;"; break;
            case '&': result += "&amp;"; break;
            default: result += c; break;
        }
    }
    return result;
}

int main() {
    string str;
    getline(cin, str);
    string replaced = replace_string(str);
    cout << replaced << endl;
    return 0;
}