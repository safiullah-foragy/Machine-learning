// #include <bits/stdc++.h>
// using namespace std;

// void dfs(int node, int parent, vector<int> adj[]) 
// {
//     cout << node << " "; 

//     for (int child : adj[node]) 
//     {
//         if (child != parent) 
//         { 
//             dfs(child, node, adj); 
//         }
//     }
// }

// int main() 
// {
//     int n = 5;
//     vector<int> adj[n + 1];

//     adj[1] = {2, 3};
//     adj[2] = {1, 4, 5};
//     adj[3] = {1};
//     adj[4] = {2};
//     adj[5] = {2};

//     cout << "DFS (Recursive): ";
//     dfs(1, -1, adj); 

//     return 0;
// }


//DFS (Iterative Method) — using Stack

#include <bits/stdc++.h>
using namespace std;

void dfs_iterative(int start, vector<int> adj[], int n) 
{
    vector<bool> visited(n + 1, false);
    stack<int> st;
    st.push(start);

    while (!st.empty()) 
    {
        int node = st.top();
        st.pop();

        if (visited[node]) continue;
        visited[node] = true;
        cout << node << " ";

        for (int i = adj[node].size() - 1; i >= 0; i--) 
        {
            int child = adj[node][i];
            if (!visited[child])
            {
                st.push(child);
            }
        }
    }
}

int main() 
{
    int n = 5;
    vector<int> adj[n + 1];

    adj[1] = {2, 3};
    adj[2] = {1, 4, 5};
    adj[3] = {1};
    adj[4] = {2};
    adj[5] = {2};

    cout << "DFS (Iterative): ";
    dfs_iterative(1, adj, n);

    return 0;
}

