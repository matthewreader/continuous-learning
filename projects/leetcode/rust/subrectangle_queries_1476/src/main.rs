struct SubrectangleQueries {
    rectangle: Vec<Vec<i32>>
}


impl SubrectangleQueries {
    fn new(rectangle: Vec<Vec<i32>>) -> Self {
        Self { rectangle }
    }
    
    fn update_subrectangle(&mut self, row1: i32, col1: i32, row2: i32, col2: i32, new_value: i32) {
    	for i in row1..row2 + 1 {
    		for j in col1..col2 + 1 {
    			self.rectangle[i as usize][j as usize] = new_value;
    		}
    	}
    }
    
    fn get_value(&self, row: i32, col: i32) -> i32 {
        self.rectangle[row as usize][col as usize]
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_get_value() {
        let mut rectangle = SubrectangleQueries::new(vec![vec![1,2,1],vec![4,3,4],vec![3,2,1],vec![1,1,1]]);
        assert_eq!(1, rectangle.get_value(0, 2))
    }
    
}