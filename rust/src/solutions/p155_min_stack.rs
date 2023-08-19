// Min Stack O(1) approach

#[allow(dead_code)]
struct MinStack {
    stack: Vec<i32>,
    min_stack: Vec<i32>,
}

impl MinStack {
    #[allow(dead_code)]
    fn new() -> Self {
        MinStack {
            stack: Vec::new(),
            min_stack: Vec::new(),
        }
    }

    #[allow(dead_code)]
    fn push(&mut self, val:i32){
        self.stack.push(val);

        if let Some(&min_val) = self.min_stack.last() {
            self.min_stack.push(std::cmp::min(val, min_val));
        } else {
            self.min_stack.push(val);
        }
    }

    #[allow(dead_code)]
    fn pop(&mut self) {
        self.stack.pop();
        self.min_stack.pop();
    }

    #[allow(dead_code)]
    fn top(&self) -> i32 {
        *self.stack.last().unwrap_or(&0)
    }

    #[allow(dead_code)]
    fn get_min(&self) -> i32 {
        *self.min_stack.last().unwrap_or(&0)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_min_stack() {
        let mut min_stack = MinStack::new();
        min_stack.push(-2);
        min_stack.push(0);
        min_stack.push(-3);
        assert_eq!(min_stack.get_min(), -3);
        min_stack.pop();
        assert_eq!(min_stack.top(), 0);
        assert_eq!(min_stack.get_min(), -2);
    }
}