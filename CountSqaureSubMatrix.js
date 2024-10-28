var countSquareSubMatrix=(matrix)=>{
    let row=matrix.length;
    let col=matrix[0].length;

    for(let i=1;i<row;i++)
    {
        for(let j=1;j<col;j++)
        {
            if(matrix[i][j]==1)
            {
                matrix[i][j]=Math.min(matrix[i-1][j-1],Math.min(matrix[i-1][j],matrix[i][j-1]))

            }
        }

    }

    let square_count=0;
    for(let i=0;i<row;i++)
    {
        for(let j=0;j<col;j++)
        {
            sqaure_count+=matrix[i][j];
        }
    }

    return square_count;
}

let result=countSquareSubMatrix([
    [0,1,1,1],
    [1,1,1,1],
    [0,1,1,1]
  ]);
  console.log(result);