// Container with Most Wwater

pub fn max_area(height: Vec<i32>) -> i32 {
    let mut res: i32 = 0;

    let mut l = 0;
    let mut r = height.len() - 1;

    while l < r {
        let area = (r - l) as i32 * std::cmp::min(height[l], height[r]);
        res = res.max(area);

        if height[l] < height[r] {
            l += 1;
        } else {
            r -= 1;
        }
    }
    res
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_container_water_1() {
        let height = vec![1, 8, 6, 2, 5, 4, 8, 3, 7];
        let result = max_area(height);
        let expected = 49;
        assert_eq!(result, expected);
    }

    #[test]
    fn test_container_water_2() {
        let height = vec![1, 1];
        let result = max_area(height);
        let expected = 1;
        assert_eq!(result, expected);
    }
}
