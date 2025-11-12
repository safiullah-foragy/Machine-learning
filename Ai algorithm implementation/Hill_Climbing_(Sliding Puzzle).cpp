#include <bits/stdc++.h>
using namespace std;

struct Puzzle {
    vector<vector<int>> board;
    int h; // heuristic

    Puzzle(vector<vector<int>> b) {
        board = b;
        h = 0;
        int goal[3][3] = {{1,2,3},{4,5,6},{7,8,0}};
        for(int i=0;i<3;i++)
            for(int j=0;j<3;j++)
                if(board[i][j]!=0 && board[i][j]!=goal[i][j]) h++;
    }

    bool operator<(const Puzzle &p) const { return h < p.h; }
};

vector<Puzzle> getNeighbors(Puzzle &p) {
    vector<Puzzle> neighbors;
    int dx[4]={-1,1,0,0}, dy[4]={0,0,-1,1};
    int x,y;
    // find blank
    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            if(p.board[i][j]==0) x=i, y=j;

    for(int k=0;k<4;k++){
        int nx=x+dx[k], ny=y+dy[k];
        if(nx>=0 && nx<3 && ny>=0 && ny<3){
            vector<vector<int>> newBoard = p.board;
            swap(newBoard[x][y], newBoard[nx][ny]);
            neighbors.push_back(Puzzle(newBoard));
        }
    }
    return neighbors;
}

Puzzle hillClimbing(Puzzle start) {
    while(true){
        vector<Puzzle> neighbors = getNeighbors(start);
        Puzzle best = start;
        for(auto &n: neighbors){
            if(n.h < best.h) best = n;
        }
        if(best.h >= start.h) break; // no improvement
        start = best;
    }
    return start;
}

void printBoard(Puzzle &p){
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++) cout<<p.board[i][j]<<" ";
        cout<<"\n";
    }
}

int main() {
    vector<vector<int>> startBoard = {
        {2,8,3},
        {1,6,4},
        {7,0,5}
    };

    Puzzle start(startBoard);
    Puzzle solution = hillClimbing(start);

    cout<<"Final heuristic: "<<solution.h<<"\n";
    printBoard(solution);
}
