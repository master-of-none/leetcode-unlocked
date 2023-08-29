use std::cmp::Ordering;

pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
    let rows = matrix.len();
    let cols = matrix[0].len();

    let mut top = 0;
    let mut bot = rows - 1;

    while top <= bot{
        let row = top + (bot - top) / 2;

        if target > matrix[row][cols - 1]{
            top = row + 1;
        }
        else if target < matrix[row][0] {
            bot = row - 1;
        }
        else {
            break;
        }

        if top > bot {
            return false;
        }
    }

    let row = top + (bot - top) / 2;

    let mut l = 0;
    let mut r = cols - 1;

    while l <= r {
        let m = l + (r - l) / 2;

        // if target > matrix[row][m]{
        //     l = m + 1;
        // }
        // else if target < matrix[row][m] {
        //     r = m - 1;
        // }
        // else{
        //     return true;
        // }

        match target.cmp(&matrix[row][m]){
            Ordering::Greater => {
                l = m + 1;
            }
            Ordering::Less => {
                r = m - 1;
            }
            Ordering::Equal => {
                return true;
            }
        }
    }
    false
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_matrix_1(){
        let matrix: Vec<Vec<i32>> = vec![
            vec![1, 3, 5, 7],
            vec![10, 11, 16, 20],
            vec![23, 40, 34, 60],
        ];

        let target:i32 = 3;

        assert!(search_matrix(matrix, target));

    }
    #[test]
    fn test_matrix_2(){
        let matrix: Vec<Vec<i32>> = vec![
            vec![1, 3, 5, 7],
            vec![10, 11, 16, 20],
            vec![23, 40, 34, 60],
        ];

        let target:i32 = 2;

        assert!(!search_matrix(matrix, target));

    }
}