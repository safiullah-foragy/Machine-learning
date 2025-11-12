#include <bits/stdc++.h>
using namespace std;

void dfs_recursive_style(vector<int> adj[], vector<bool> &visited, int node) {
    if (visited[node]) return;
    visited[node] = true;
    cout << node << " ";

    for (int child : adj[node]) {
        if (!visited[child])
            dfs_recursive_style(adj, visited, child);
    }
}

int main() {
    vector<int> adj[6];
    adj[1] = {2, 3};
    adj[2] = {1, 4, 5};
    adj[3] = {1};
    adj[4] = {2};
    adj[5] = {2};

    vector<bool> visited(6, false);
    cout << "DFS (Recursive Style): ";
    dfs_recursive_style(adj, visited, 2);
}
