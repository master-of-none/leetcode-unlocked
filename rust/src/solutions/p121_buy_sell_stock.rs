pub fn max_profit(prices: Vec<i32>) -> i32 {
    let mut l = 0;
    let mut max_p = 0;

    for r in 0..prices.len() {
        if prices[l] < prices[r] {
            let profit = prices[r] - prices[l];
            max_p = max_p.max(profit);
        } else {
            l = r;
        }
    }
    max_p
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_stock_1() {
        let prices = vec![7, 1, 5, 3, 6, 4];

        assert_eq!(max_profit(prices), 5);
    }

    #[test]
    fn test_stock_2() {
        let prices = vec![7, 6, 4, 3, 1];

        assert_eq!(max_profit(prices), 0);
    }
}
