let grid = [];
function createSudokuGrid() {
    let table = document.getElementById("sudoku-grid");
    for (let i = 0; i < 9; i++) {
        let row = document.createElement("tr");
        for (let j = 0; j < 9; j++) {
            let cell = document.createElement("td");
            let input = document.createElement("input");
            input.type = "text";
            input.maxLength = "1";
            input.pattern = "[1-9]";
            input.onkeypress = function(e) { return /[1-9]/.test(String.fromCharCode(e.keyCode)); };
            cell.appendChild(input);
            row.appendChild(cell);
        }
        table.appendChild(row);
    }
}

function solveSudoku() {
    let table = document.getElementById("sudoku-grid");
    for (let i = 0; i < 9; i++) {
        let row = [];
        for (let j = 0; j <9; j++) {
            let input = table.rows[i].cells[j].querySelector("input").value;
            row.push(input === "" ? 0 : parseInt(input));
        }
        grid.push(row);
    }
    solve(grid);
    // console.log(grid);
}

window.onload = createSudokuGrid;

function solve(board){
    for(let i=0;i<9;i++){
        for(let j=0;j<9;j++){
            if(board[i][j] === 0){
                for(let c=1;c<=9;c++){
                    if(isValid(board,i,j,c)){
                        board[i][j] = c;
                        if(solve(board) === true)
                            return true;
                        board[i][j] = 0;
                    }
                }
                return false;
            }
        }
    }
    updateSudokuGrid()
    return true;
}

function isValid(board, row, col, val) {
    for (let i = 0; i < 9; i++) {
        if (board[row][i] === val)
            return false;
        if (board[i][col] === val)
            return false;
        if (board[Math.floor(row / 3) * 3 + Math.floor(i / 3)][Math.floor(col / 3) * 3 + i % 3] === val)
            return false;
    }
    return true;
}

function updateSudokuGrid() {
    let table = document.getElementById("sudoku-grid");
    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            table.rows[i].cells[j].querySelector("input").value = grid[i][j];
        }
    }
}