// Given a square matrix mat, return the sum of the matrix diagonals.

// Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

// Example 1:


// Input: mat = [[1,2,3],
//               [4,5,6],
//               [7,8,9]]
// Output: 25
// Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
// Notice that element mat[1][1] = 5 is counted only once.
// Example 2:

// Input: mat = [[1,1,1,1],
//               [1,1,1,1],
//               [1,1,1,1],
//               [1,1,1,1]]
// Output: 8
// Example 3:

// Input: mat = [[5]]
// Output: 5
 

// Constraints:

// n == mat.length == mat[i].length
// 1 <= n <= 100
// 1 <= mat[i][j] <= 100.

const result=(matrix)=>{
    const row=matrix.length;
    const col=matrix[0].length;
    let sum_diagonal=0;
    for(let i=0;i<row;i++){
        for(let j=0;j<col;j++){
            if(i===j||(i+j+1)===row){
                sum_diagonal+=matrix[i][j];
            }
        }
    }
    return sum_diagonal;
}

function main(){
    let res=result([[1,2,3],
        [4,5,6],
        [7,8,9]]);
        console.log(res);
}

main()

console.log(Math.floor(3/2))