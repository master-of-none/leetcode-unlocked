// Valid Sudoku

use std::collections::HashMap;
use std::collections::HashSet;

pub fn valid_sudoku(board: Vec<Vec<char>>) -> bool {
    let mut rows: HashMap<usize, HashSet<char>> = HashMap::new();
    let mut cols: HashMap<usize, HashSet<char>> = HashMap::new();
    let mut squares: HashMap<(usize, usize), HashSet<char>> = HashMap::new();

    for r in 0..9 {
        for c in 0..9 {
            let cell = board[r][c];

            if cell == '.' {
                continue;
            }

            if rows.entry(r).or_insert(HashSet::new()).contains(&cell)
                || cols.entry(c).or_insert(HashSet::new()).contains(&cell)
                || squares
                    .entry((r / 3, c / 3))
                    .or_insert(HashSet::new())
                    .contains(&cell)
            {
                return false;
            }

            rows.entry(r).or_insert(HashSet::new()).insert(cell);
            cols.entry(c).or_insert(HashSet::new()).insert(cell);
            squares
                .entry((r / 3, c / 3))
                .or_insert(HashSet::new())
                .insert(cell);
        }
    }
    true
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sudoku_1() {
        let board: Vec<Vec<char>> = vec![
            vec!['5', '3', '.', '.', '7', '.', '.', '.', '.'],
            vec!['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            vec!['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            vec!['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            vec!['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            vec!['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            vec!['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            vec!['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            vec!['.', '.', '.', '.', '8', '.', '.', '7', '9'],
        ];

        assert!(valid_sudoku(board));
    }

    #[test]
    fn test_sudoku_2() {
        let board: Vec<Vec<char>> = vec![
            vec!['8', '3', '.', '.', '7', '.', '.', '.', '.'],
            vec!['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            vec!['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            vec!['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            vec!['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            vec!['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            vec!['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            vec!['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            vec!['.', '.', '.', '.', '8', '.', '.', '7', '9'],
        ];

        assert!(!valid_sudoku(board));
    }
}
